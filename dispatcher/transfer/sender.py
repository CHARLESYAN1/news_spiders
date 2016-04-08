import os
import sys
import signal
import logging
from os.path import abspath as _abs
from multiprocessing.dummy import Pool as ThreadPool

from ..utils import CsfPickle
from ..utils import JobBase
from .. import app, logger

self = JobBase()
console = logging.getLogger(__name__)
console.setLevel(logging.INFO)


def handle_signals(signum, frame, _self=self):
    console.info('\nSignal type: <{}>, frame: <{}>'.format(signum, frame))
    CsfPickle().dump(_self.cached)
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signals)
signal.signal(signal.SIGTERM, handle_signals)


def transport(sftp, dir_path, filename, which):
    """
    :param sftp: sftp property of SmoothTransfer class
    :param dir_path: hot news ot full news path
    :param filename: just file name
    :param which: int, if which is 1, transfer hot news, else transfer full news
    """
    abs_local_path = dir_path + filename

    try:
        if self.is_filtering(filename):
            s3_key = self.s3_key(dir_path, filename)
            self.bucket.put(s3_key, abs_local_path)

            if self.is_migrate is not None:
                sftp.put(abs_local_path, abs_local_path)
            else:
                # transfer news file to redis
                self.ptq.send_message(abs_local_path, which)
    except Exception as e:
        logger.info('Transfer file between two PC or Upload S3 or Push message to redis Queue on SGP server error: '
                    'type <{}>, msg <{}>, file <{}>'.format(e.__class__, e, _abs(__file__)))


@app.scheduled_job(trigger='interval', seconds=5, misfire_grace_time=5)
def send_files():
    """ this function transfer crawled news file to analytic server and aws s3 bucket """
    if not os.path.exists(self.hot_news_path):
        os.makedirs(self.hot_news_path)

    if not os.path.exists(self.full_news_path):
        os.makedirs(self.full_news_path)

    sftp = self.goosy

    # pool = ThreadPool(16)
    # pool.map(lambda h_fn: transport(sftp, self.hot_news_path, h_fn, which=1), os.listdir(self.hot_news_path))
    # pool.map(lambda f_fn: transport(sftp, self.full_news_path, f_fn, which=2), os.listdir(self.full_news_path))
    # pool.close()
    # pool.join()

    total_fns = []
    # sftp = self.goosy.sftp
    total_fns.extend([(self.hot_news_path, fn, 1) for fn in os.listdir(self.hot_news_path)])
    total_fns.extend([(self.full_news_path, fn, 2) for fn in os.listdir(self.full_news_path)])

    for t_args in total_fns:
        transport(sftp, *t_args)
    sftp.close()

