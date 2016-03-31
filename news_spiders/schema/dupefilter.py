from scrapy.dupefilters import BaseDupeFilter

from . import connection
from ..utils import populate_md5


class RFPDupeFilter(BaseDupeFilter):
    """Redis-based request duplication filter"""
    default_dupefilter_key = 'url_tit_key'

    def __init__(self, server, key):
        """
        Initialize duplication filter

        :param server: Redis instance
        :param key : str, Where to store fingerprints
        """
        self.server = server
        self.key = key

    @classmethod
    def from_settings(cls, settings):
        server = connection.from_settings(settings)

        # class as standalone dupefilter with scrapy's default scheduler
        # if scrapy passes spider on open() method this wouldn't be needed
        key = settings.get('SCRAPY_DUPEFILTER') or cls.default_dupefilter_key
        return cls(server, key)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def request_seen(self, request):
        # Default we us finger print to filter request, but just use url too enough
        # fp = request_fingerprint(request)
        # print 'Res:', request.url
        if request.meta.get('dupefilter', True):
            fp = populate_md5(request.url)
            added = self.server.sadd(self.key, fp)
            return not added

