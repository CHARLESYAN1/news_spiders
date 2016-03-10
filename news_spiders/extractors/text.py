from scrapy import Selector

from ..utils import RegexType
from .base import BaseExtractors
from ..urlsresolver import BaseLinksResolver as _BLR


class TextExtractors(BaseExtractors):
    def __init__(self, selector, config):
        super(TextExtractors, self).__init__(selector=selector, config=config)

    def extract(self, partial_name, with_tags=False):
        self.remove_regex_node()
        args_query = self.__getattr__(partial_name)

        for query in args_query:
            if isinstance(query, RegexType):
                result = self.extract_with_regex(regex=query)
            else:
                result = self.extract_with_selector(query=query, with_tags=with_tags)

            if result:
                return result
        return u''

    @property
    def multipages_urls(self):
        urls = []
        blr = _BLR(self._selector)
        multipages_query = self.marks_multipages
        html = self._selector.response.body_as_unicode()

        for _query in multipages_query:
            if isinstance(_query, RegexType):
                m = _query.search(html)

                if m is not None:
                    html = html[m.end() + 1:]
                    text = m.groupdict().get('multi_page', '')
                    urls.extend(Selector(text=text).xpath('//a/@href').extract())
            else:
                css_selector, index, _ = self.converter(_query)
                links = self._selector.css(css_selector)[index].css('.//a/href').extract()
                urls.extend([blr.join_url(_link) for _link in links])
        return urls

    title = property(lambda self: self.extract(partial_name='title'))
    date = property(lambda self: self.extract(partial_name='date'))
    auth = property(lambda self: self.extract(partial_name='auth'))
    text = property(lambda self: self.extract(partial_name='text'))


