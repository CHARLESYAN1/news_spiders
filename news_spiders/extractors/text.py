from ..utils import RegexType
from .base import BaseMarks, BaseExtractors


class TextExtractors(BaseMarks, BaseExtractors):
    def __init__(self, selector, config):
        BaseMarks.__init__(self, config=config)
        BaseExtractors.__init__(self, selector=selector)

    def extract(self, partial_name, with_tags=False):
        args_query = self.__getattr__(partial_name)

        for query in args_query:
            if isinstance(query, RegexType):
                result = self.extract_with_regex(regex=query)
            else:
                result = self.extract_with_selector(query=query, with_tags=with_tags)

            if result:
                return result
        return u''

    title = property(lambda self: self.extract(partial_name='title'))
    date = property(lambda self: self.extract(partial_name='date'))
    auth = property(lambda self: self.extract(partial_name='auth'))
    text = property(lambda self: self.extract(partial_name='text'))

