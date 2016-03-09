# -*- coding: utf-8 -*-
import re
import sys
import time
import linecache

LINE_BREAK = u'#&#'


def get_tags(default_date_tag, default_auth_tag):
    def wrapper_func(func):
        def tag_wrapper(self, *args, **kwargs):
            tag_names = [default_date_tag, default_auth_tag]
            for key, value in self.details.iteritems():
                if not tag_names[1] and '_'.join(['pyq', tag_names[0]]) == key:
                    return func(self, *(args + (value,)), **kwargs)

                sby = sort_by_tag(key, tag_names)
                if all(tag_names) and sby is not None:
                    return func(self, *(args + (value, sby)), **kwargs)
            else:
                raise TypeError("Don't parse element key [`%s`] in `%s` site" % (
                    '_'.join(tag_names), self.__site_name))
        return tag_wrapper
    return wrapper_func


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
