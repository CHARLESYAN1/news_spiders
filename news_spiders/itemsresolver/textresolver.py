# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import Levenshtein

from ..utils import RegexType
from ..urlsresolver import BaseURi
from .base import BaseResolver as _Base
from ..decorators.decorators import parse_table_tags


class TagsClean(object):
    def __init__(self, text_with_tags, repl='#&#'):
        self._text = text_with_tags or ''
        self._repl = repl

    def remove_tags(self):
        # js , style, and comment tags must remove
        flags = re.S | re.I
        remove_tags_lists = [
            re.compile(r'<!--\[if !IE\]>.*?<!\[endif\]-->'),
            re.compile(r'<!--.*?-->', flags),
            re.compile(r'<!.*?>', flags),
            re.compile(r'<script.*?>.*?</script>', flags),
            re.compile(r'<style.*?>.*?</style>', flags),
            re.compile(r'<noscript.*?>.*?</noscript>', flags),
            re.compile(r"<img.*?>", flags)
        ]

        for re_value in remove_tags_lists:
            self._text = re_value.sub('', self._text)

    @parse_table_tags
    def paragraph(self):
        regex_paragraph = [
            re.compile(r'<p.*?>', re.S | re.I),
            re.compile(r'<br.*?>', re.S | re.I),
            re.compile(r'<div.*?>', re.S | re.I),
        ]

        repls = [
            '&nbsp;', '&hellip;', '&#183;', '&middot;',  '&quot;', '&#160;', '&ensp;', '&#13;', '&amp;',
            '&ldquo;', '&rdquo;', '&gt;', '&rsquo;', '&lsquo;', '&plusmn;', '&mdash;', '&lt;/p&gt;', 'lt;',
        ]

        for subst in regex_paragraph + repls:
            if isinstance(subst, RegexType):
                self._text = subst.sub(self._repl, self._text)
            else:
                self._text = self._text.replace(subst, '')
        self._text = re.compile(r'<.*?>', re.S).sub('', self._text)

    def sanitize(self):
        self.remove_tags()
        self.paragraph()

        text = re.compile(r'\s+|\u3000+| +', re.S).sub(' ', self._text)

        verbose_patterns = [r'(%s)+', r'(%s\s+)+', r'(\s+%s)+']

        for _pattern in verbose_patterns:
            text = re.compile(_pattern % self._repl, re.S).sub(self._repl, text)
        text_final = re.compile(r'\s+', re.S).sub(' ', text)
        return text_final.strip(''.join([self._repl, ' ']))


class DeepTextResolver(_Base):
    """
    Some redundant text can't rid by tags,
    So only through specific text position with cutting the text you need
    """
    def __init__(self, text_list, url, title=None):
        self.__url = url
        self.__title = title
        self.__text_list = text_list
        super(DeepTextResolver, self).__init__()

        self._text = self.total_text()

    def total_text(self):
        new_text_list = []
        line_break = self._settings['LINE_BREAK']
        similarity = (lambda a, b: int(Levenshtein.ratio(a, b) * 1000) >= 995)

        for _text in self.__text_list:
            _text = TagsClean(text_with_tags=_text, repl=line_break).sanitize()

            # Judgment Text Similarity
            if not new_text_list:
                new_text_list.append(_text)
            else:
                if not similarity(new_text_list[-1], _text) and \
                        not similarity(''.join(new_text_list), _text):
                    new_text_list.append(line_break + _text)
        return ''.join(new_text_list)

    @property
    def domains(self):
        """ Could add  site domain on latter """
        _domains = {
            'takungpao', 'qq', 'wallstreetcn', '163', 'people', '17ok',
            'kxt', 'ifeng', 'weixin', 'gw', '52steel',
        }
        return _domains

    def __split_text(self, _domain):
        """ According to special text to split news content, extract the content that you want to """
        split_endswith_config = self._settings['ENDSWITH_TEXT'].copy()

        if _domain in split_endswith_config:
            # First to deal with site to split specific text of content,
            # which locate to end of content, like as `qq`, `wallstreetcn`
            # here use regex to spit is better
            for shield_item in split_endswith_config[_domain]:
                pattern = re.compile(r'%s' % shield_item, re.S)
                self._text = pattern.split(self._text, maxsplit=1)[0]
        elif _domain in BaseURi.hostname(self.__url):
            # Second to deal with site, witch need some rule to cut content.
            # Split to content with `title`, generally locate to top of content,
            # like as `takungpao`, could use regex is better
            pass

    def __sub_text(self, _domain):
        """ According to special text to replace news content with blank """
        sub_text_config = self._settings['SUB_TEXT'].copy()

        if _domain in sub_text_config:
            # Notice that replace text must add parentheses
            # Match regex must also complete the regular expression, else replace error
            for _regex_text in sub_text_config[_domain]:
                pattern = re.compile(r'%s' % _regex_text, re.S)
                self._text = pattern.sub(self.__repl, self._text)

    @staticmethod
    def __repl(m):
        match_text = m.group()

        for _sub_text in m.groups():
            match_text = match_text.replace(_sub_text, '')
        return match_text

    def deep_text(self):
        for domain in self.domains:
            self.__split_text(domain)
            self.__sub_text(domain)
        return self._text.strip().strip(self._settings['LINE_BREAK'])


class TextResolver(DeepTextResolver):
    def __init__(self, text_list, url, title=None):
        super(TextResolver, self).__init__(text_list=text_list, url=url, title=title)

    def resolve(self):
        if self.identity_encoding(self._text):
            return self.deep_text()
        return ''


