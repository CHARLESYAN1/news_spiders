import re
import copy
import simplejson

from ..utils import RegexType
from ..itemsresolver import DateResolver
from .base import BaseLinksResolver as Base, BaseURi


class LinksJsonResolver(Base):
    def __init__(self, selector, json_data):
        self._json_data = json_data.copy()
        super(LinksJsonResolver, self).__init__(selector)

    def to_python(self):
        json_data_with_tags = self._context
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

    def no_canonization_url(self, url):
        host_name = BaseURi.hostname(url)
        canon_map = self.settings['NO_CANONIZATION_URLS'].copy()

        for domain, s_url in canon_map.items():
            if domain in host_name:
                url = s_url.format(url=url)
                return url
        return url

    def resolve(self):
        """
        :return: list, format is [[url, pub_date, auth], [url, pub_date, auth], ...]
        """
        urls = []
        python_data = self.to_python()
        result_data = copy.deepcopy(python_data)
        join_url = self._json_data.get('join_key')
        url_key = self._json_data.get('url_key', 'url')
        data_key = self._json_data.get('data_key', 'Data').split('.')

        if isinstance(python_data, list):
            return self.normalize(python_data)

        for _data_key in data_key:
            result_data = result_data.get(_data_key, {})

        for k, each_dict in enumerate(result_data or []):
            try:
                # maybe have datetime and author information
                pub_date = self.pub_date_info(each_dict)
                auth = self.auth_info(each_dict)

                if join_url:
                    url = self.join_url(join_url.format(url=each_dict[url_key]))
                else:
                    url = self.join_url(each_dict[url_key])

                if url is not None:
                    urls.append([url, pub_date, auth])
            except (KeyError, ValueError):
                pass
        return self.normalize(urls)


class LinksRegexResolver(Base):
    def __init__(self, selector, block_regex):
        # assert 'url' in wrappers or 'date' in wrappers or 'auth' in wrappers

        # self._wrappers = wrappers
        self._block_regex = block_regex
        super(LinksRegexResolver, self).__init__(selector)

    def parse_date(self, default_context):
        """
        So far separate `pub_date` and `url`, just to date css selector
        :param default_context:string, date text
        """
        try:
            pub_date = DateResolver(
                pub_date=default_context,
                url=self._page_url
            ).resolve()

            return pub_date
        except (IndexError, ValueError, AttributeError):
            pass

    def parse(self, group_dict):
        group_dict = group_dict or {}
        hostname = BaseURi.hostname(self._page_url)

        base_url = group_dict.get('url')
        pub_date = group_dict.get('date', '')

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
            url = self.join_url(base_url)
            _pub_date = self.parse_date(pub_date)
            return url, _pub_date

    def resolve(self):
        urls = []
        html = self._context

        while True:
            # like as site 'yahoo' at hk news, we just want to get `url`
            # but site 'chiefgroup' at usa news, we must get `date` and `url`
            # Notice that element order of `wrappers`, you can use Regex `groupdict` to parse
            m_regex = self._block_regex.search(html)

            try:
                link = self.parse(m_regex.groupdict())
                html = html[m_regex.end() + 1:]

                if link is not None:
                    urls.append(link)
            except (AttributeError, ValueError):
                break
        return self.normalize(urls)


class LinksSelectorResolver(Base):
    def __init__(self, selector, block_css, config=None):
        self._block_css = block_css
        self._config = config or {}
        super(LinksSelectorResolver, self).__init__(selector)

    @staticmethod
    def convert_css(query):
        converter = (lambda _css, _index=None: (_css, _index))

        if isinstance(query, (tuple, list)):
            css, index = converter(*query)
        else:
            css, index = converter(query)
        return css, index

    def convert_xpath(self, query):
        pass

    @property
    def is_weixin(self):
        belong = self._config.get('belong')

        if belong and belong == 'weixin':
            return True
        return False

    @staticmethod
    def _get_weixin_links(selector):
        base_url = 'http://mp.weixin.qq.com'
        links = selector.xpath('//@hrefs').extract()
        return [base_url + _link for _link in links]

    def resolve(self):
        urls = []
        css, index = self.convert_css(self._block_css)
        extractors_list = self._selector.css(css)

        if index is None:
            extractors_copy = extractors_list[:]
        else:
            extractors_copy = extractors_list and [extractors_list[index]]

        for _selector in extractors_copy:
            if not self.is_weixin:
                links = _selector.xpath('descendant-or-self::a/@href').extract()
            else:
                links = self._get_weixin_links(_selector)

            for _each_url in links:
                new_url = self.join_url(_each_url)
                if new_url and new_url not in urls:
                    urls.append(new_url)
        return self.normalize(urls)


class UrlsResolver(Base):
    def __init__(self, selector, config):
        self._config = config
        self.__default_key = 'block_attr'
        super(UrlsResolver, self).__init__(selector)

    def resolve(self):
        urls = []
        json_data = self._config.get('json')

        if json_data:
            return LinksJsonResolver(
                selector=self._selector,
                json_data=json_data
                ).resolve()

        for block in self._config.get(self.__default_key, []):
            # handle three  situation of `block_attr` value:
            # (1):  just css_selector
            # (2):  tuple of css_selector and index
            # (3):  regex to search href

            if isinstance(block, RegexType):
                links_by_regex = LinksRegexResolver(
                    selector=self._selector,
                    block_regex=block
                    ).resolve()
                urls.extend(links_by_regex)
            else:
                links_by_selector = LinksSelectorResolver(
                    selector=self._selector,
                    block_css=block,
                    config=self._config
                    ).resolve()
                urls.extend(links_by_selector)

        return urls


