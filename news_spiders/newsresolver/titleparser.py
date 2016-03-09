# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from .base import BaseParser
from ..eggs import logger_pprint


class TitleParser(BaseParser):
    def __init__(self, context, tags_tit_values, tags_remove=None):
        """
        :param tags_remove: tuple or list, css selector or regex, remove redundant tags
        :param tags_tit_values: tuple or list of tuple, which in including two fields
        like as :
            ((tag_or_regex1, index1), (tag_or_regex2, index2), ...)
        """
        self._tags_title = tags_tit_values
        super(TitleParser, self).__init__(context, tags_remove)

    @staticmethod
    def remove_whitespace(text):
        return re.compile(r'\s+', re.S).sub(' ', text).strip()

    def resolve(self):
        for tag_value in self._tags_title:
            args = tag_value if isinstance(tag_value, (tuple, list)) else (tag_value, )
            tag, index = (lambda _tag, _eq=None: (_tag, _eq))(*args)
            text_tit = self.remove_whitespace(self.text(tag, index))
            logger_pprint.debug('tit: [%s]' % text_tit)

            if self.identity_encoding(text_tit):
                return text_tit
        return ''
