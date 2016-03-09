# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import Levenshtein

from .base import BaseParser, BaseURi
from ..configs import LINE_BREAK
from .urlsparser import CommonURLResolver
from ..eggs import logger_pprint, files_config
from ..eggs.utils.utils import TagsClean
from ..eggs.utils.download import DownloadHtml, BasePyQueryHtml


class UriTrash(object):
    __file_configs = files_config

    def is_trash(self, _url=None):
        """ return value first is flag, second is site key, third is related trash """
        domain_trash = self.__file_configs.multi_uri_trash
        flag, domain, trashes = False, None, None

        if _url is None:
            return flag, domain, trashes

        for _domain, _trash in domain_trash.iteritems():
            if _domain in BaseURi.hostname(_url):
                # _domain could not as return value
                return True, _domain, _trash
        return flag, domain, trashes

    def multi_uri_trash(self, old_multi_uris):
        new_urls = []
        multi_uris = old_multi_uris
        __url = multi_uris[0] if multi_uris else None
        flag, domain, trash = self.is_trash(__url)

        for _uri in multi_uris:
            if flag and any([_uri_trash in _uri for _uri_trash in trash]):
                # like as `ftchinese` site have rest full text and full text, which is filter as trash
                # the situation url is discarded
                continue
            else:
                new_urls.append(_uri)
        return new_urls


class MultiPageText(BaseParser, UriTrash):
    def __init__(self, context, con_tag, multi_attr, url, remove_tags):
        """
        :param con_tag: css selector or regex
        :param multi_attr: css selector or regex, obtain href from context
        """
        # self._current_document = context
        self._url = url
        self._con_tag = con_tag
        # self._tags_remove = remove_tags
        self._multi_attr = multi_attr if multi_attr else ()

        super(MultiPageText, self).__init__(context, remove_tags)

    def remove_pagination_text(self):
        # remove pagination tags
        for _css_selector in self._multi_attr:
            self._document(_css_selector).remove()

    def get_pagination_links(self):
        # So far, obtain href is css selector eq
        multi_page_urls = []

        if isinstance(self._multi_attr, (tuple, list)):
            # So far, just have one css selector in `self._multi_attr` tuple or list
            multi_attrs = self._multi_attr
        else:
            multi_attrs = (self._multi_attr, )

        for page_tag in multi_attrs:
            temp_urls = CommonURLResolver(
                context=self._document,
                block=page_tag,
                index=None,
                page_url=self._url
            ).resolve()

            if temp_urls:
                multi_page_urls.extend(temp_urls)
                break

        if self._url in multi_page_urls:
            multi_page_urls = multi_page_urls[multi_page_urls.index(self._url) + 1:]

        return self.multi_uri_trash(multi_page_urls[:])

    @property
    def single_text(self):
        inner = (lambda _tag, _sub=None, _eq=None: (_tag, _sub, _eq))
        self.remove_pagination_text()

        for tags in self._con_tag:
            args = tags if isinstance(tags, (tuple, list)) else (tags, )
            tag_or_regex, sub_selector, index = inner(*args)

            con_origin = self.text(tag_or_regex, index, sub_selector, True)
            _text = TagsClean(con_origin).sanitize()

            if _text:
                return _text
        return ''

    def total_text(self):
        # notice that behind `other_urls` in `text_list`
        other_urls = self.get_pagination_links()
        text_list = [self.single_text]
        is_similarity = (lambda a, b: int(Levenshtein.ratio(a, b) * 1000) >= 996)

        for url in other_urls:
            html = DownloadHtml().get_html(url)
            self._document = BasePyQueryHtml().populate_document(html)

            text = self.single_text

            # Judgment Text Similarity
            if not is_similarity(text_list[-1], text) and \
                    not is_similarity(''.join(text_list), text):
                # generate to new Paragraph
                text_list.append(LINE_BREAK + text)
        return ''.join(text_list)


class DeepTextResolver(object):
    """
    Some redundant text can't rid by tags,
    So only through specific text position with cutting the text you need
    """
    def __init__(self, con_text, url, title=None):
        self.__url = url
        self.__tit = title
        self.__con_text = con_text

    @property
    def domains(self):
        """ Could add  site domain on latter """
        _domains = {'takungpao', 'qq', 'wallstreetcn', '163', 'people', '17ok', 'kxt'}
        return _domains

    def __split_text(self, _domain):
        """ According to special text to split news content, extract the content that you want to """
        split_endswith_config = files_config.endswith_text.copy()

        if _domain in split_endswith_config:
            # First to deal with site to split specific text of content,
            # which locate to end of content, like as `qq`, `wallstreetcn`
            # here use regex to spit is better
            for shield_item in split_endswith_config[_domain]:
                pattern = re.compile(r'%s' % shield_item, re.S)
                self.__con_text = pattern.split(self.__con_text, maxsplit=1)[0]
        elif _domain in BaseURi.hostname(self.__url):
            # Second to deal with site, witch need some rule to cut content.
            # Split to content with `title`, generally locate to top of content,
            # like as `takungpao`, could use regex is better
            pass

    def __sub_text(self, _domain):
        """ According to special text to replace news content with blank """
        sub_text_config = files_config.sub_text.copy()

        if _domain in sub_text_config:
            # Notice that replace text must add parentheses
            # Match regex must also complete the regular expression, else replace error
            for _regex_text in sub_text_config[_domain]:
                pattern = re.compile(r'%s' % _regex_text, re.S)
                self.__con_text = pattern.sub(self.__repl, self.__con_text)

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
        return self.__con_text.strip(''.join([LINE_BREAK, ' ']))


class ContentParser(MultiPageText):
    def __init__(self, context, tags_con_values, tags_remove, url, title=None, multi_attr=None):
        """
        :param tags_con_values: css selector or regex, format is as follows:
            selector_or_regex: css selector or regex, must param
            sub_selector1:  css selector, option param
            index: option, but must param when selector_or_regex have many values
            ((selector_or_regex, sub_selector, index), ...)
        :param tags_remove: tuple or list, css selector or regex, remove redundant tags
        """
        self._title = title

        super(ContentParser, self).__init__(
                context=context,
                con_tag=tags_con_values,
                multi_attr=multi_attr,
                url=url,
                remove_tags=tags_remove
        )

    def resolve(self):
        con_text = self.total_text()

        logger_pprint.debug('content text: [%s]' % con_text)
        if self.identity_encoding(con_text):
            return DeepTextResolver(
                    con_text=con_text,
                    url=self._url,
                    title=self._title
            ).deep_text()
        return ''

