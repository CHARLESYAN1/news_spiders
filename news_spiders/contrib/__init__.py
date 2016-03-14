from ..conf import news_config
from .pyredis.cached import RedisCached

if news_config.settings['PLATFORM']:
    redis_cached = set()
else:
    redis_cached = RedisCached().get()

__all__ = ['RedisCached']
