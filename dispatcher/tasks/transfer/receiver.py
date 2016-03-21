from .. import app
from .base import Base


@app.scheduled_job(trigger='interval', seconds=5)
def receive_files():
    """ Receive message from redis queue, then convert to file """
    self = Base()
    hot_path = self.hot_news_path
    full_path = self.full_news_path

    if self.is_migrate is True:
        self.uptf.convert_message(hot_path, mq_typ=1)
        self.uptf.convert_message(full_path, mq_typ=2)

