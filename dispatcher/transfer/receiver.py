from os.path import abspath as _abs

from ..utils import JobBase
from .. import app, logger


@app.scheduled_job(trigger='interval', seconds=5)
def receive_files():
    """ Receive message from redis queue, then convert to file """
    self = JobBase()
    hot_path = self.hot_news_path
    full_path = self.full_news_path

    try:
        if self.is_migrate is True:
            self.uptf.convert_message(hot_path, mq_typ=1)
            self.uptf.convert_message(full_path, mq_typ=2)
    except Exception as e:
        info = (e.__class__, e, _abs(__file__))
        logger.info('Receive message from redis yield file error: type <{}>, msg <{}>, file <{}>'.format(*info))

