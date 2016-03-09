# -*- coding: utf-8 -*-
import re
import copy
import urlparse
import simplejson

from .base import BaseURi
from .dateparser import DateParser
from ..eggs.utils.download import BasePyQueryHtml
from ..eggs.utils.utils import Types
from ..eggs import logger_error


class BaseURLResolver(object):
    """ get every page all urls to news that you need, which have 3 situation:
        (1): site is ajax or json data type;
        (2): don't find news url, need regex;
        (3): find class or id by css
    """
    def __init__(self, context, page_url, block=None, index=None):
        self._context = context
        self._page_url = page_url
        self._block = block
        self._index = index

    def _net_location(self):
        results = [t for t in urlparse.urlparse(self._page_url) if t]
        slash_path = results[-1]
        url_level = ['://'.join(results[:2])]
        url_level.extend([v for v in slash_path[:slash_path.rfind('/')].split('/') if v])
        return url_level

    def __parse_especial_url(self, _net_loc, _url):
        """
        :param _net_loc: list, split to page url
        :param _url, string, need to join url
        """
        # Special site name 'hot_wjs',  notice to parse url
        if 'wsj' in BaseURi.hostname(self._page_url):
            return '/'.join(_net_loc[:2] + [_url])

    def join_url(self, path_url):
        path_url = path_url.strip()
        net_loc = self._net_location()
        dot_pos, level_len = 0, len(net_loc)

        if not path_url or '|' in path_url or '///' in path_url or 'javascript' in path_url:
            return None

        if path_url.startswith('http'):
            return path_url

        if path_url.startswith('?'):
            return self._page_url + path_url

        if path_url.startswith('/') or (not path_url.startswith('/') and
                                        not path_url.startswith('./') and not path_url.startswith('../')):
            especial_url = self.__parse_especial_url(net_loc, path_url)

            return urlparse.urljoin(net_loc[0], path_url) if not especial_url else especial_url

        if path_url.startswith('./'):
            return '/'.join(net_loc) + path_url[1:]

        for k in range(level_len - 1):
            if path_url.startswith('../'):
                path_url = path_url[3:]
                dot_pos += 1
        return '/'.join(net_loc[:level_len - dot_pos] + [path_url])


class CommonURLResolver(BaseURLResolver):
    def __init__(self, context, block, index, page_url, sub_link=None):
        self.__sub_link = sub_link
        super(CommonURLResolver, self).__init__(context, page_url, block, index)

    def _url_from_regex(self):
        """ So far handle to `hk-yahoo` site """
        # regex resolve url is very complicated, maybe you obtain date and url
        # maybe you just obtain url, so you must be detailed analysis site so that get what you want

        urls = []
        html = self._context.html()

        while True:
            # like as site 'yahoo' at hk news, we just want to get `url`
            # but site 'chiefgroup' at usa news, we must get `date` and `url`
            # Notice that element order of `wrappers`, you can use Regex `groupdict` to parse
            m_regex = self._block.search(html)

            try:
                if m_regex is None:
                    break

                wrappers = URLRegexResolver(
                    wrappers=m_regex.groupdict(),
                    page_url=self._page_url,
                    sub_link=self.__sub_link
                ).resolve()

                if wrappers is not None:
                    urls.append(wrappers)

                html = html[m_regex.end() + 1:]
            except (AttributeError, ValueError) as e:
                logger_error.info('Regex Url Error: [{}], err msg: [{}]'.format(e.__class__, e))
                break
        return urls

    def _url_from_pyq(self):
        """ deal with generic web html """
        urls = []

        if self._index is None:
            href_nodes = self._context(self._block)
        else:
            href_nodes = self._context(self._block).eq(self._index)

        for tag_href in href_nodes.items('a'):
            url = self.join_url(tag_href.attr('href'))
            if url and url not in urls:
                urls.append(url)
        return urls

    def resolve(self):
        urls = []

        if Types.is_regex_method(self._block):
            urls.extend(self._url_from_regex())

        try:
            urls.extend(self._url_from_pyq())
        except (TypeError, AttributeError):
            pass
        return urls


class URLJsonResolver(BaseURLResolver):
    def __init__(self, context, page_url, json_data):
        self._json_data = json_data.copy()
        super(URLJsonResolver, self).__init__(context, page_url)

    def to_python(self):
        json_data_with_tags = self._context.html()
        left_index = json_data_with_tags.find('{')
        right_index = json_data_with_tags.rfind('}') + 1
        origin_json_str = json_data_with_tags[left_index: right_index]

        try:
            return simplejson.loads(origin_json_str)
        except (simplejson.JSONDecodeError, ):
            pass

        regex = r'http://.*?\.shtml'
        return [u for u in re.compile(regex, re.S).findall(origin_json_str)]

    def pub_date_info(self, info_dict):
        date_key = self._json_data.get('date_key')

        if date_key is not None:
            return info_dict[date_key]
        return 0L

    def auth_info(self, info_dict):
        auth_key = self._json_data.get('auth_key')

        if auth_key is not None:
            return info_dict[auth_key]
        return u''

    def resolve(self):
        urls = []
        python_data = self.to_python()
        result_data = copy.deepcopy(python_data)
        url_key = self._json_data.get('url_key', 'url')
        data_key = self._json_data.get('data_key', 'Data').split('.')

        if isinstance(python_data, list):
            return python_data

        for _data_key in data_key:
            result_data = result_data.get(_data_key, {})

        for k, each_dict in enumerate(result_data or []):
            try:
                # maybe have datetime and author information
                pub_date = self.pub_date_info(each_dict)
                auth = self.auth_info(each_dict)
                url = self.join_url(each_dict[url_key])

                if url is not None:
                    urls.append([url, pub_date, auth])
            except (KeyError, ValueError):
                pass
        return urls


class URLRegexResolver(BaseURLResolver):
    def __init__(self, wrappers, page_url=None, sub_link=None):
        assert 'url' in wrappers or 'date' in wrappers or 'auth' in wrappers

        self._wrappers = wrappers
        self.__sub_link = sub_link
        super(URLRegexResolver, self).__init__('None', page_url)

    def parse_date(self, default_context):
        """
        So far separate `pub_date` and `url`, just to date css selector
        :param default_context:string, date text
        """
        try:
            pub_date = DateParser(
                context=BasePyQueryHtml().populate_document(default_context),
                tags_date_values=(),
                url=self._page_url,
                default_flag=True
            ).resolve()

            return pub_date
        except (IndexError, ValueError, AttributeError):
            pass

    def resolve(self):
        hostname = BaseURi.hostname(self._page_url)

        base_url = self._wrappers.get('url')
        pub_date = self._wrappers.get('date', '')

        if 'yahoo' in hostname:
            url = base_url.replace(r'\/news\/', '/news/')

            if url.startswith('/news/'):
                try:
                    url = self.join_url(url)
                except (UnicodeDecodeError, UnicodeEncodeError):
                    url = self.join_url(url.decode('unicode-escape'))

                if url is not None:
                    return url, pub_date
        else:
            if self.__sub_link:
                url = self.__sub_link % base_url
            else:
                url = self.join_url(base_url)

            _pub_date = self.parse_date(pub_date)
            return url, _pub_date

