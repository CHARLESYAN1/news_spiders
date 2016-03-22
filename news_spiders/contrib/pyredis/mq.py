from redis import (ConnectionError,
                   DataError,
                   ResponseError,
                   TimeoutError,
                   InvalidResponse
                   )

from . import logger
from .base import Base


class MessageQueue(Base):
    """
    The class mainly handle sgp news that including part hot news and full news to migrate Beijing Amazon or Office 207
    """
    def push(self, message, typ):
        """
        Here two queue, `sgp_hot_mq` push part foreign site hot news Or
        `sgp_news_mq` push part foreign site full news from amazon sgp server

        :param message: json, which have two element, and every element have many data to related queue name
        :param typ: if typ = 1, that is `sgp_hot_mq`, else `sgp_news_mq`
        """
        _queue = self.queues(typ)

        try:
            self.redis.lpush(_queue, message)
        except (ConnectionError, DataError, ResponseError, TimeoutError, InvalidResponse) as e:
            logger.info('Push message to Queue error: redis key <{}>, type <{}>, msg <{}>, file <{}>'.format(
                _queue, e.__class__, e, __file__[:-1]))

    def get_message(self, typ):
        """
        Obtain queue all messages from redis related queue
        :param typ: Only 1 or 2, if typ =1, that is `sgp_hot_mq`, else typ = 2, is `sgp_news_mq`
        """
        _queue = self.queues(typ)

        try:
            return self.redis.rpop(_queue)
        except (ConnectionError, DataError, ResponseError, TimeoutError, InvalidResponse) as e:
            logger.info('Get message from Queue error: redis key <{}>, type <{}>, msg <{}>, file <{}>'.format(
                _queue, e.__class__, e, __file__[:-1]))
            return []

    def queues(self, typ):
        if typ == 1:
            return self.sgp_hot_mq
        elif typ == 2:
            return self.sgp_news_mq
        raise ValueError("Don't typ is %s queue!" % typ)

