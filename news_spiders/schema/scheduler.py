from scrapy.utils.misc import load_object
# from scrapy.core.scheduler import Scheduler

from . import connection
from .dupefilter import RFPDupeFilter


# default values
SCHEDULER_PERSIST = False
QUEUE_KEY = 'scheduler_queue:requests'
QUEUE_CLASS = '.queue.PriorityQueue'
DUPEFILTER_KEY = 'dupefilter'
IDLE_BEFORE_CLOSE = 0


class Scheduler(object):
    """ Scheduler base on Redis"""

    def __init__(self, redis,
                 scheduler_persist,
                 scheduler_queue_class,
                 scheduler_queue_key,
                 dupefilter_key,
                 idle_before_close
                 ):
        """
        Initialize scheduler

        :param redis: Redis object
        :param scheduler_persist: weather persist or not
        :param scheduler_queue_key: scheduler queue key
        :param scheduler_queue_class: scheduler queue class
        :param dupefilter_key: filter url queue key
        :param idle_before_close:
        """
        self.redis = redis
        self.persist = scheduler_persist
        self.queue_class = scheduler_queue_class
        self.queue_key = scheduler_queue_key
        self.dupefilter_key = dupefilter_key
        self.idle_before_close = idle_before_close
        self.stats = None

    @classmethod
    def from_settings(cls, settings):
        persist = settings.get('SCHEDULER_PERSIST', SCHEDULER_PERSIST)
        queue_key = settings.get('SCHEDULER_QUEUE_KEY', QUEUE_KEY)
        queue_class = load_object(settings.get('SCHEDULER_QUEUE_CLASS', QUEUE_CLASS))
        dupefilter_key = settings.get('DUPEFILTER_KEY', DUPEFILTER_KEY)
        idle_before_close = settings.get('SCHEDULER_IDLE_BEFORE_CLOSE', IDLE_BEFORE_CLOSE)
        return cls(
            redis=connection.from_settings(settings),
            scheduler_persist=persist,
            scheduler_queue_class=queue_class,
            scheduler_queue_key=queue_key,
            dupefilter_key=dupefilter_key,
            idle_before_close=idle_before_close
        )

    @classmethod
    def from_crawler(cls, crawler):
        instance = cls.from_settings(crawler.settings)
        # FIXME: for now, stats are only supported from this constructor
        instance.stats = crawler.stats
        return instance

    def open(self, spider):
        setattr(self, 'spider', spider)
        setattr(self, 'queue', self.queue_class(self.redis, self.queue_key, spider))
        setattr(self, 'dupefilter', RFPDupeFilter(self.redis, self.dupefilter_key))

        if self.idle_before_close < 0:
            self.idle_before_close = 0

        # notice if there are requests already in the queue to resume the crawl
        if len(self.queue):
            spider.log("Resuming crawl (%d requests scheduled)" % len(self.queue))

    def close(self, reason):
        if not self.persist:
            self.queue.clear()

    def enqueue_request(self, request):
        if not request.dont_filter and self.dupefilter.request_seen(request):
            return
        if self.stats:
            self.stats.inc_value('scheduler/enqueued/redis', spider=self.spider)
        self.queue.push(request)

    def next_request(self):
        block_pop_timeout = self.idle_before_close
        request = self.queue.pop(block_pop_timeout)
        if request and self.stats:
            self.stats.inc_value('scheduler/dequeued/redis', spider=self.spider)
        return request

    def has_pending_requests(self):
        return len(self) > 0

    def __len__(self):
        return len(self.queue)
