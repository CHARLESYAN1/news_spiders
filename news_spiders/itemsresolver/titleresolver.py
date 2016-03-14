import re

from .base import BaseResolver as _Base


class TitleResolver(_Base):
    def __init__(self, title):
        self.__title = title

    @staticmethod
    def remove_whitespace(text):
        return re.compile(r'\s+', re.S).sub(' ', text).strip()

    def resolve(self):
        title = self.remove_whitespace(self.__title)

        if self.identity_encoding(title):
            return title
        return u''




