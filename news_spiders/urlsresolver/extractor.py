from scrapy.link import Link as _Link
from scrapy import Selector as _Selector
from scrapy.linkextractors import LinkExtractor as _LinkExtractor

from ..utils.utils import populate_md5


class ProcessorUri(object):
    @staticmethod
    def process_value():
        pass


class NewsLinkExtractors(_LinkExtractor):
    def __init__(self, required_css, *args, **kwargs):
        self.required_css = required_css
        super(NewsLinkExtractors, self).__init__(*args, **kwargs)

    def extract_links(self, response):
        # deal with general url and regex url,time
        # selector = _Selector(response)

        _link = _Link('http://finance.qq.com/original/caijingguancha/f1582.html')
        _link.text = populate_md5(response.url)
        return [_link]



