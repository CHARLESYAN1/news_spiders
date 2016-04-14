from scrapy.utils.reqser import request_from_dict, request_to_dict

try:
    import cPickle as pickle
except ImportError:
    import pickle


class QueueBase(object):
    def __init__(self, redis, queue_key, spider):
        """
        :param redis: redis object
        :param queue_key: redis queue key
        :param spider: spider instance
        """
        self.redis = redis
        self.queue_key = queue_key
        self.spider = spider

    def push(self, request):
        raise NotImplementedError

    def pop(self, timeout=0):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def clear(self):
        self.redis.delete(self.queue_key)

    def _encode_request(self, request):
        """ Encode a request object """
        return pickle.dumps(request_to_dict(request, self.spider), protocol=-1)

    def _decode_request(self, encoded_request):
        """ Decode an request previously encoded """
        return request_from_dict(pickle.loads(encoded_request), self.spider)


class PriorityQueue(QueueBase):
    def __len__(self):
        return self.redis.zcard(self.queue_key)

    def push(self, request):
        print self.redis
        value = self._encode_request(request)
        pairs = {value: -request.priority}
        self.redis.zadd(self.queue_key, **pairs)

    def pop(self, timeout=0):
        pipe = self.redis.pipeline()
        pipe.multi()
        pipe.zrange(self.queue_key, 0, 0).zremrangebyrank(self.queue_key, 0, 0)
        results, count = pipe.execute()
        if results:
            return self._decode_request(results[0])





