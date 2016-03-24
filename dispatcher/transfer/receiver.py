import os.path

from .. import app, logger
from .base import Base


@app.scheduled_job(trigger='interval', seconds=5)
def receive_files():
    """ Receive message from redis queue, then convert to file """
    self = Base()
    try:
        hot_path = self.hot_news_path
        full_path = self.full_news_path

        if self.is_migrate is True:
            self.uptf.convert_message(hot_path, mq_typ=1)
            self.uptf.convert_message(full_path, mq_typ=2)
    except Exception as e:
        logger.info('Receive message from redis yield file error: type <{}>, msg <{}>, file <{}>'.format(
            e.__class__, e, os.path.abspath(__file__)))

