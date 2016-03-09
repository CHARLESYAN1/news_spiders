# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import urlparse

from ..eggs import logger_error
from ..eggs.utils.download import BasePyQueryHtml
from ..eggs.utils.utils import Types


class BaseParser(object):
    def __init__(self, context, tags_remove=None):
        if not Types.is_pyquery_element(context):
            raise TypeError('Context is not pyquery object in file:[%s]' % __file__)

        self._document = context
        self._tags_remove = () if tags_remove is None else tags_remove

    def erase_tags(self):
        """
            This function you must notice that if News have more page text, when you crawl the second page or latter,
            you must use the latest document that is the second page, else News content error.
        """
        regex_tags, selector_tags = [], []

        # To prevent the lack of document, especially in more page news
        self.__ship_document = self._document

        for _erase_tag in self._tags_remove:
            if Types.is_regex_method(_erase_tag):
                regex_tags.append(_erase_tag)
            else:
                selector_tags.append(_erase_tag)

        for _css_tag in selector_tags:
            self.__ship_document(_css_tag).remove()

        if regex_tags:
            html = self.__ship_document.html()
            for _regex_tag in regex_tags:
                html = _regex_tag.sub('', html)
            self.__ship_document = BasePyQueryHtml().populate_document(html)

    @staticmethod
    def identity_encoding(text):
        for char in text:
            if re.compile(r'[\u4e00-\u9fbf]', re.S).search(char) is not None:
                return True
        return False

    def __text_by_css_selector(self, tag, index, sub_selector):
        try:
            if sub_selector is None:
                return self.__ship_document(tag).eq(index).text()
            else:
                return self.__ship_document(tag)(sub_selector).eq(index).text()
        except (TypeError, AttributeError, IndexError) as e:
            logger_error.info('CSS parser element error: [{}], \n\tin file: [{}]\t'.format(e, __file__))
        return ''

    def __text_by_regex(self, regex):
        try:
            _html = self.__ship_document.html()
            return regex.findall(_html)[0]
        except (IndexError, AttributeError):
            pass
        return ''

    def __html_by_identity(self, tag_or_regex, index, sub_selector):
        # Must get html, because of separating the paragraph
        # Must notice that multi page content to `self.__ship_document`

        if Types.is_regex_method(tag_or_regex):
            return self.__text_by_regex(tag_or_regex)

        try:
            if sub_selector is None:
                _document = self.__ship_document(tag_or_regex)
            else:
                _document = self.__ship_document(tag_or_regex)(sub_selector)

            if index:
                return _document.eq(index).html()
            else:
                html = ''

                for _index in range(_document.length):
                    html += _document.eq(_index).html()
                return html
        except (TypeError, AttributeError, IndexError) as e:
            logger_error.info('CSS parser content error: [{}], \n\tin file: [{}]\t'.format(e, __file__))
        return ''

    def text(self, tag_or_regex, index=None, sub_selector=None, identity=None):
        """
        :param tag_or_regex: css selector or regex pattern, if it is regex pattern,
            `self._document(tag_or_regex)` is PyQuery object, but it is nothing, no text
        :param sub_selector: None or css selector, especially get pub_date and author
        :param index: int, get pos text if tag_or_regex css selector
        :param identity: None or bool, if it is None, get title, pub_date or author, otherwise content
        """
        index = index or 0
        self.erase_tags()

        if identity is None:
            if Types.is_regex_method(tag_or_regex):
                return self.__text_by_regex(tag_or_regex)
            else:
                return self.__text_by_css_selector(tag_or_regex, index, sub_selector)
        return self.__html_by_identity(tag_or_regex, index, sub_selector)


class BaseURi(object):
    @staticmethod
    def hostname(url):
        no_include = {'com', 'cn', 'www', 'net'}
        _hostname = urlparse.urlparse(url).hostname

        urlsplit = _hostname.split('.') if _hostname else []
        return set([_hn for _hn in urlsplit if _hn not in no_include])







