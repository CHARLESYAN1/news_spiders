# -*- coding: utf-8 -*-
import re
from scrapy import Selector

LINE_BREAK = u'#&#'


def remove_script_style(func):
    flags = re.S | re.I
    remove_tags_lists = [
        re.compile(r'<script.*?>.*?</script>', flags),
        re.compile(r'<style.*?>.*?</style>', flags),
        re.compile(r'<noscript.*?>.*?</noscript>', flags)
    ]

    def remove_tags(*args, **kwargs):
        self = args[0]
        _html = self._selector.response.body_as_unicode()

        if not self.is_script:
            # if value of self.is_script is False, remove all style and script tags
            for re_value in remove_tags_lists:
                _html = re_value.sub('', _html)
            self._selector = Selector(text=_html)
        return func(*args, **kwargs)
    return remove_tags


def parse_table_tags(func):
    def wrapper(*args, **kwargs):
        # this decorator is only remove all `br` tags in table,
        # but so far, we discard this news when encounter with `table` tags
        self = args[0]
        pattern_table = re.compile(r'<table.*?>.*?</table>', re.S)
        pattern_table_line = [re.compile(r'<tr.*?>', re.S), re.compile(r'<th.*?>', re.S)]

        if pattern_table.search(self._text):
            # Handle html with `table` tags, because of issue of showing style on mobile dev
            # So far we discard the news when encountering with this issue
            # If really need such news later, we special hand with it
            self._text = u''

            parser_table_after = []
            text_table_list = pattern_table.findall(self._text)

            for k, text_table_temp in enumerate(text_table_list):
                self._text = pattern_table.sub(u'{%s}' % k, self._text, count=1)

                for _regex in pattern_table_line:
                    text_table_temp = _regex.sub(LINE_BREAK, text_table_temp)
                parser_table_after.append(re.compile(r'<.*?>', re.S).sub(u' ', text_table_temp))

            self._text = self._text.format(*parser_table_after)
        return func(*args, **kwargs)
    return wrapper
