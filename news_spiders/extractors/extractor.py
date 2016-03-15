from .base import BaseExtractor
from ..utils import RegexType
from ..urlsresolver import PageLinks


class NewsExtractor(BaseExtractor):
    def __init__(self, selector, config):
        self._page_url = selector.response.url
        super(NewsExtractor, self).__init__(selector=selector, config=config)

    def extract(self, partial_name, with_tags=False):
        self.clean_obstacle_node()
        args_query = self.dispatch(partial_name)

        for query in args_query:
            if isinstance(query, RegexType):
                result = self.extract_with_regex(regex=query)
            else:
                result = self.extract_with_xpath(query=query, with_tags=with_tags)

            if result:
                return result
        return u''

    @property
    def pagination_urls(self):
        return PageLinks(
            selector=self._selector,
            page_tags=self.marks_multipages,
            page_url=self._page_url
        ).get_page_links()

    title = property(lambda self: self.extract(partial_name='title'))
    date = property(lambda self: self.extract(partial_name='date'))
    auth = property(lambda self: self.extract(partial_name='auth'))
    text = property(lambda self: self.extract(partial_name='text', with_tags=True))


