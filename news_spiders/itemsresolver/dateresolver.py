# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import time
from datetime import datetime, date

from ..urlsresolver import BaseURi
from .base import BaseResolver as _Base


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
        hostname = BaseURi.hostname(url)
        for _domain in self.domains:
            if _domain in hostname:
                try:
                    find_date = self.date_pattern.findall(datestr)
                    date_list = list(find_date[0])
                    year = date_list.pop(2)
                    return '-'.join([year] + date_list)
                except IndexError:
                    datestr = ''

        # 处理微信文章的发布时间， 转未见戳为标准格式
        if 'weixin' in hostname and 'qq' in hostname:
            try:
                ltime = time.localtime(int(datestr))
                datestr = time.strftime('%Y-%m-%d %H:%M:%S', ltime)
            except (ValueError, TypeError):
                datestr = ''
        return datestr


class DateResolver(_Base, BaseDateUtil):
    def __init__(self, pub_date, url):
        self.__url = url
        self.__pub_date = pub_date or ''

    def pre_process(self, date_digit):
        if self.__url and 'yahoo' in BaseURi.hostname(self.__url):
            _date = date_digit[:8]
            _hour = date_digit[8: 10]
            _other = date_digit[10:]
            temp_hour = int(_hour) + 8

            new_hour = str(temp_hour - 24) if temp_hour > 24 else str(temp_hour)
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
        return u''

    @staticmethod
    def is_valid(pub_dt):
        if not pub_dt:
            return False

        y, mo, d = pub_dt[:4], pub_dt[4:6], pub_dt[6:8]
        h, mi, s = pub_dt[8:10], pub_dt[10:12], pub_dt[12:]

        if (len(y) == 4 and y <= str(date.today()).split('-')[0]) and \
            (len(mo) == 2 and '01' <= mo <= '12') and \
            (len(d) == 2 and '01' <= d <= '31') and \
            (len(h) == 2 and '00' <= h <= '23') and \
            (len(mi) == 2 and '00' <= mi <= '59') and \
            (len(s) == 2 and '00' <= s <= '59'):
            return True
        return False

    def resolve(self):
        if self.__pub_date.isdigit() and len(self.__pub_date) == 14:
            return self.__pub_date

        origin_date = self.replace_verbose(self.__pub_date)
        pub_date = self._get_date(self.parse(origin_date, self.__url))

        if pub_date:
            return pub_date
        return u''
