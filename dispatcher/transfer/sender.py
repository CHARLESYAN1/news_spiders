import os
import sys
import signal
import logging
from os.path import abspath as _abs
from multiprocessing.dummy import Pool as ThreadPool

from ..utils import CsfPickle
from ..utils import JobBase
from .. import app, logger

console = logging.getLogger(__name__)
console.setLevel(logging.INFO)


class SenderFilesJobs(object):
    cls_job = JobBase()

    def __init__(self):
        self.smooth = self.cls_job.smooth

    @classmethod
    def handle_signals(cls, signum, frame):
        console.info('\nSignal type: <{}>, frame: <{}>'.format(signum, frame))
        CsfPickle().dump(cls.cls_job.cached)
        sys.exit(0)

    def transport(self, hot_path, full_path, remote_hot_path=None, remote_full_path=None):
        """
        Send news files to analysis server

        :param hot_path: related hot news directory, eg: /data/news/csf_news/
        :param full_path: related full news directory, eg: /data/news/csf_news/
        :param remote_hot_path: the same as hot_path
        :param remote_full_path: the same as full_path
        """
        remote_h_path = hot_path if remote_hot_path is None else remote_hot_path
        remote_f_path = full_path if remote_full_path is None else remote_full_path

        push_args = [(hfn, hot_path + hfn, remote_h_path + hfn, 1) for hfn in os.listdir(hot_path)]
        push_args.extend([(ffn, full_path + ffn, remote_f_path + ffn, 2) for ffn in os.listdir(full_path)])

        for fn, abs_local, abs_remote, mq_type in push_args:
            try:
                if self.cls_job.is_filtering(fn):
                    if self.cls_job.is_migrate is not None:
                        self.smooth.put(abs_local, abs_remote)
                    else:
                        self.cls_job.ptq.send_message(abs_local, mq_type)
            except Exception as e:
                logger.info(
                    'Transfer file between two PC or Upload S3 or Push message to redis Queue on SGP server error: '
                    'type <{}>, msg <{}>, file <{}>'.format(e.__class__, e, _abs(__file__)))
        self.smooth.close()


@app.scheduled_job(trigger='interval', seconds=5, misfire_grace_time=5)
def send_files():
    """ this function transfer crawled news file to analytic server and aws s3 bucket """
    self = JobBase()
    hot_path = self.hot_news_path
    full_path = self.full_news_path

    if not os.path.exists(hot_path):
        os.makedirs(hot_path)

    if not os.path.exists(full_path):
        os.makedirs(full_path)

    SenderFilesJobs().transport(hot_path, full_path)

signal.signal(signal.SIGINT, SenderFilesJobs.handle_signals)
signal.signal(signal.SIGTERM, SenderFilesJobs.handle_signals)

