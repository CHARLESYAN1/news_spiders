import os
import signal
import sys
from os.path import abspath as _abs

from ..utils import CsfPickle
from ..utils import JobBase
from .. import app, logger

self = JobBase()


def handle_signals(signum, frame, _self=self):
    CsfPickle().dump(_self.cached)
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signals)

if not self.config.get('PLATFORM'):
    signal.signal(signal.SIGKILL, handle_signals)


def transport(dir_path, filename, which):
    """
    :param self: Base class instance
    :param dir_path: hot news ot full news path
    :param filename: just file name
    :param which: int, if which is 1, transfer hot news, else transfer full news
    """
    local_path = dir_path + filename

    try:
        if self.is_filtering(filename):
            s3_key = self.s3_key(dir_path, filename)
            self.bucket.put(s3_key, local_path)

            if self.is_migrate is True:
                self.goosy.put(local_path, dir_path)

            if self.is_migrate is None:
                # transfer news file to redis
                self.ptq.send_message(local_path, which)
    except Exception as e:
        logger.info('Transfer file between two PC or Upload S3 or Push message to redis Queue on SGP server error: '
                    'type <{}>, msg <{}>, file <{}>'.format(e.__class__, e, _abs(__file__)))


@app.scheduled_job(trigger='interval', seconds=5)
def send_files():
    """ this function transfer crawled news file to analytic server and aws s3 bucket """
    if not os.path.exists(self.hot_news_path):
        os.makedirs(self.hot_news_path)

    if not os.path.exists(self.full_news_path):
        os.makedirs(self.full_news_path)

    for filename in os.listdir(self.hot_news_path):
            transport(self.hot_news_path, filename, which=1)

    for filename in os.listdir(self.full_news_path):
            transport(self.full_news_path, filename, which=2)

