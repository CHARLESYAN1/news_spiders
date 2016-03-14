from __future__ import unicode_literals
import re

from ..conf import InitConfigs as _Init


class BaseResolver(object):
    def __init__(self):
        self.__settings = _Init().settings

    @staticmethod
    def identity_encoding(text):
        for char in text:
            if re.compile(r'[\u4e00-\u9fbf]', re.S).search(char) is not None:
                return True
        return False
