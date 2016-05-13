# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from ..urlsresolver import BaseURi
from .base import BaseResolver as _Base


class AuthResolver(_Base):
    def __init__(self, auth, date_value, url=None, reverse=False, or_index=None):
        """
        :param date_value: long, crawl date value
        :param reverse: bool, date previous, then auth latter, which is False, otherwise True
        Description th same as `DateParser` class
        """
        self.__url = url
        self.__auth = auth or ''
        self.__reverse = reverse
        self.__date_value = str(date_value)
        self.__or_index = or_index or 0

        super(AuthResolver, self).__init__()

    def clear_date(self, auth_text):
        year = self.__date_value[:4]
        rest = self.__date_value[4:]
        other = [rest[i * 2: (i + 1) * 2] for i in range(len(rest) / 2)]

        if self.__reverse:
            return auth_text[:auth_text.find(year)]

        if year not in auth_text:
                return auth_text

        for item in [year] + other:
            index = auth_text.find(item)
            if index != -1:
                auth_text = auth_text[index + len(item):].strip()
        return auth_text

    @staticmethod
    def remove_tags(auth_text):
        return re.compile(r'<.*?>', re.S).sub('', auth_text)

    @staticmethod
    def clear_verbose(auth_text_list):
        new_auth_list = []
        redundancy = [u'|', u'&nbsp;', u'&nbsp']

        for item in auth_text_list:
            for repl in redundancy:
                item = item.replace(repl, u'').strip()

            if not item:
                continue
            new_auth_list.append(item)
        return new_auth_list

    @staticmethod
    def _clear_delimiters(_auth_text_list):
        delimiters = [u':', u'：']
        auth_text_temp_list = []

        for temp_auth in _auth_text_list:
            is_delimit = False

            for _delimit in delimiters:
                index = temp_auth.find(_delimit)

                if index != -1:
                    is_delimit = True
                    new_temp_auth = temp_auth[index:].strip(u''.join([_delimit, u' ']))

                    if new_temp_auth:
                        auth_text_temp_list.append(new_temp_auth)

            if not is_delimit:
                auth_text_temp_list.append(temp_auth)
        return auth_text_temp_list

    def _get_auth(self, auth_origin):
        author = ''
        auth_text = self.clear_date(auth_origin)
        auth_text_list = [t for t in re.compile(r'\s+|\u3000| ', re.S).split(auth_text) if t]

        auth_text_temp_list = self._clear_delimiters(auth_text_list)
        new_auth_text_list = self.clear_verbose(auth_text_temp_list)

        try:
            author = self.remove_tags(new_auth_text_list[self.__or_index])
        except (IndexError, ) as e:
            pass
        else:
            pass
        return author

    def parser_by_url(self):
        host_name = BaseURi.hostname(self.__url)
        site_auth_dicts = self._settings['URL_DETERMINE_AUTH'].copy()

        for site_key, auth in site_auth_dicts.iteritems():
            if site_key in host_name:
                if 'qq' == site_key:
                    if 'lenjing' in self.__url:
                        # Not all the tencent news need such deal with, just to deal `lengjing` site
                        return auth
                elif 'p5w' == site_key and 'ircs' in host_name:
                    return auth
                else:
                    return auth
            else:
                # 如果domain不在url里， 那么一定不要添加代码， 否则解析 `auth` 字段错误
                pass

    def resolve(self):
        auth_by_url = self.parser_by_url()

        if auth_by_url is not None:
            return auth_by_url
        else:
            auth_text = self._get_auth(self.__auth)

            if auth_text:
                # Here no use `self.identity_encoding(...)` method, because of
                # `title` is determined, and also can't use this method to filter for `yahoo` site
                return auth_text
        return u''

