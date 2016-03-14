from __future__ import unicode_literals
import re

from ..conf import news_config


class BaseResolver(object):
    def __init__(self):
        self._settings = news_config.settings

    @staticmethod
    def identity_encoding(text):
        for char in text:
            if re.compile(r'[\u4e00-\u9fbf]', re.S).search(char) is not None:
                return True
        return False
