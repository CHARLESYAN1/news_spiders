from ..utils import JobBase
from .. import app, logger
from news_spiders.exceptions import get_exce_info


@app.scheduled_job(trigger='interval', seconds=5, misfire_grace_time=5)
def receive_files():
    """ Receive message from redis queue, then convert to file """
    self = JobBase()
    hot_path = self.hot_news_path
    full_path = self.full_news_path

    try:
        if self.is_migrate is True:
            self.uptf.convert_message(hot_path, mq_typ=1)
            self.uptf.convert_message(full_path, mq_typ=2)
    except Exception:
        logger.info(logger.exec_msg.format(
            msg='Receive message from redis yield file error',
            exec_info=get_exce_info())
        )

