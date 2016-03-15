from ..conf import news_config
from .pyredis.cached import RedisCached

if news_config.settings['PLATFORM']:
    redis_cached = set()
    print 'redis_cached:', redis_cached, id(redis_cached)
else:
    redis_cached = RedisCached().get()

__all__ = ['RedisCached']
