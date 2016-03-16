from redis import (AuthenticationError,
                   BusyLoadingError,
                   ConnectionError,
                   DataError,
                   InvalidResponse,
                   PubSubError,
                   ReadOnlyError,
                   RedisError,
                   ResponseError,
                   TimeoutError,
                   WatchError
                   )

from .base import Base


class RedisCached(Base):
    def set(self, *value):
        """
        add url or title value of news to set
        :param value: string, md5 value
        """
        try:
            self.redis.sadd(self.scrapy_filter_key, *value)
        except (AuthenticationError, BusyLoadingError, ConnectionError, DataError, InvalidResponse,
                ReadOnlyError, RedisError, ResponseError, TimeoutError, WatchError) as e:
            pass
            # logger_error.info('Set value to Redis Set Error: [{}]'.format(e))

    def get(self):
        """ get all members from set of specified key """
        try:
            return self.redis.smembers(self.scrapy_filter_key)
        except (AuthenticationError, BusyLoadingError, ConnectionError, DataError, InvalidResponse,
                ReadOnlyError, RedisError, ResponseError, TimeoutError, WatchError) as e:
            pass
            # logger_error.info('Get value from Redis Set Error: [{}]'.format(e))
        return set()

