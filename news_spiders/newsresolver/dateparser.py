# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
from datetime import datetime
from .base import BaseParser, BaseURi
from ..eggs import logger_pprint


class BaseDateUtil(object):
    # chineseworldnet` web site, like as '02/15/2016 10:25'
    date_pattern = re.compile(r'(\d{2})/(\d{2})/(\d{4}).*?(\d{2}):(\d{2})')

    @staticmethod
    def recognise_format(datestr):
        pass

    @staticmethod
    def hms_digits(*hms):
        hms_list = []

        for _hms in hms:
            hms_str = str(_hms)
            hms_list.append(hms_str if len(hms_str) == 2 else '0' + hms_str)
        return ''.join(hms_list)

    @property
    def domains(self):
        domain = {'chineseworldnet'}
        return domain

    def parse(self, datestr, url):
        for _domain in self.domains:
            if _domain in BaseURi.hostname(url):
                try:
                    find_date = self.date_pattern.findall(datestr)
                    date_list = list(find_date[0])
                    year = date_list.pop(2)
                    return '-'.join([year] + date_list)
                except IndexError:
                    datestr = ''
        return datestr


class DateParser(BaseParser, BaseDateUtil):
    def __init__(self, context, tags_date_values, tags_remove=None, url=None, default_flag=False):
        """
        :param tags_date_values: list or tuple, format is as follows:
            selector_or_regex: css selector or regex, must param
            sub_selector1:  css selector, option param
            index: int, option, but must param when selector_or_regex have many values
            (
                (selector_or_regex1, sub_selector1, index1),
                (selector_or_regex2, sub_selector2, index2),
                ...
            )
        :param tags_remove: tuple or list, css selector or regex, remove redundant tags
        """
        self._url = url
        self._tags_date = tags_date_values
        self._default_flag = default_flag
        super(DateParser, self).__init__(context, tags_remove)

    def pre_process(self, date_digit):
        if self._url and 'yahoo' in BaseURi.hostname(self._url):
            _date = date_digit[:8]
            _hour = date_digit[8: 10]
            _other = date_digit[10:]

            new_hour = str(int(_hour) + 8)
            _hour = '0' + new_hour if len(new_hour) < 2 else new_hour
            return ''.join([_date, _hour, _other])
        else:
            # if date_digit is just date string, need to add hour, minutes and seconds
            remain_datetime = date_digit[8:]
            if not remain_datetime:
                now = datetime.now()
                date_digit += self.hms_digits(now.hour, now.minute, now.second)
                return date_digit

        if len(date_digit) < 14:
            date_digit += '0' * (14 - len(date_digit))
        return date_digit

    @staticmethod
    def replace_verbose(date_origin):
        default_replace_list = ['10%', '21世纪经济报道']

        for _repl in default_replace_list:
            date_origin = date_origin.replace(_repl, '')
        return date_origin

    def _get_date(self, date_text):
        number_list = re.compile(r'\d+', re.S).findall(date_text)
        regex_year = re.compile(r'\d{4}', re.S).search(date_text)

        if regex_year is not None:
            date_string = ''

            try:
                index = number_list.index(regex_year.group())
                new_number_list = number_list[index:]

                for i, digit in enumerate(new_number_list, 1):
                    if len(date_string) < 14:
                        if i == 1:
                            date_string += digit
                        else:
                            date_string += '0' * (2 - len(digit)) + digit
            except (ValueError, IndexError):
                pass

            return self.pre_process(date_string)
        return 0L

    def resolve(self):
        inner = (lambda _tag, _sub=None, _eq=None: (_tag, _sub, _eq))

        if self._default_flag:
            last_date = self.parse(self._document.html(), self._url)
            return self._get_date(last_date)

        for tags in self._tags_date:
            args = tags if isinstance(tags, (tuple, list)) else (tags, )

            tag_date, sub_selector, index = inner(*args)
            temp_origin = self.text(tag_date, index, sub_selector)
            origin = self.replace_verbose(temp_origin)
            date_text = self._get_date(self.parse(origin, self._url))

            logger_pprint.debug('Date origin: [%s], final:[%s]' % (origin, date_text))

            if date_text:
                return date_text
        return 0L
