from ..conf import news_config
from .aws.bucket import Bucket
from .pyredis.cached import RedisCached
from .pyredis.convert import PickleToQueue
from .pyredis.convert import UnpickleToFile
from .transfer.goosy import GoosyTransfer


if news_config.settings['PLATFORM']:
    redis_cached = set()
    print 'redis_cached:', redis_cached, id(redis_cached)
else:
    redis_cached = RedisCached().get()

__all__ = ['Bucket', 'RedisCached', 'GoosyTransfer', 'PickleToQueue', 'UnpickleToFile', 'GoosyTransfer']
