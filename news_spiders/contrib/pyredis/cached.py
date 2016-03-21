from redis import (AuthenticationError,
                   BusyLoadingError,
                   ConnectionError,
                   DataError,
                   InvalidResponse,
                   ReadOnlyError,
                   RedisError,
                   ResponseError,
                   TimeoutError,
                   WatchError
                   )

from .base import Base


class RedisCached(Base):
    def set(self, default_key=None, *value):
        """
        add url or title value of news to set
        :param value: string, md5 value
        :param default_key: None|string, set key to redis
        """
        set_key = default_key or self.scrapy_filter_key

        try:
            self.redis.sadd(set_key, *value)
        except (AuthenticationError, BusyLoadingError, ConnectionError, DataError, InvalidResponse,
                ReadOnlyError, RedisError, ResponseError, TimeoutError, WatchError) as e:
            pass
            # logger_error.info('Set value to Redis Set Error: [{}]'.format(e))

    def get(self, default_key=None):
        """
        get all members from set of specified key
        :param default_key: None|string, set key to redis
        """
        set_key = default_key or self.scrapy_filter_key

        try:
            return self.redis.smembers(set_key)
        except (AuthenticationError, BusyLoadingError, ConnectionError, DataError, InvalidResponse,
                ReadOnlyError, RedisError, ResponseError, TimeoutError, WatchError) as e:
            pass
            # logger_error.info('Get value from Redis Set Error: [{}]'.format(e))
        return set()

