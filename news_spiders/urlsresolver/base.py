import urlparse
from datetime import date


class PageUri(object):
    def __init__(self, site_name, base_url, url_fill_rule, page):
        """
         :param base_url: string, a basic base
         :param url_fill_rule: rule of string's format
         :param page: int
         :return string: complete page url to crawl uri in this web page
         :param site_name: string, site name of site configs
         """
        self.__site_name = site_name
        self.__base_url = base_url
        self.__url_fill_rule = url_fill_rule
        self.__page = page

    @property
    def websites(self):
        """ Need special handle web site page url, like as `hot_sina2` that have date time """
        website_names = {'hot_sina_2'}
        return website_names

    def pre_process_uri(self):
        if self.__site_name in self.websites:
            if self.__site_name == 'hot_sina_2':
                page_uri = self.__base_url
                return page_uri % str(date.today()).replace('-', '')

    def get_page_url(self):
        try:
            page_uri = self.pre_process_uri()

            if page_uri is not None:
                return page_uri

            pagination_url = self.__base_url % (self.__url_fill_rule % self.__page)
            return pagination_url
        except (TypeError, ):
            pass

        pagination_url = self.__base_url % self.__url_fill_rule
        return pagination_url


class BaseURi(object):
    @staticmethod
    def hostname(url):
        no_include = {'com', 'cn', 'www', 'net'}
        _hostname = urlparse.urlparse(url).hostname

        urlsplit = _hostname.split('.') if _hostname else []
        return set([_hn for _hn in urlsplit if _hn not in no_include])

    @staticmethod
    def uniform_hostname(a, b):
        return urlparse.urlparse(a).hostname == urlparse.urlparse(b).hostname


class BaseLinksResolver(object):
    """ get every page all urls to news that you need, which have 3 situation:
        (1): site is ajax or json data type;
        (2): don't find news url, need regex;
        (3): find class or id by css
    """
    def __init__(self, selector, page_url=None):
        self._selector = selector
        self._context = selector.response.body_as_unicode()
        self._page_url = page_url or selector.response.url

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

    @staticmethod
    def normalize(links):
        new_links = []
        norm = (lambda _url, _pub=None, _auth=None: (_url, _pub, _auth))

        for _link in links:
            if isinstance(_link, (list, tuple)):
                new_links.append(norm(*_link))
            else:
                new_links.append(norm(_link))
        return new_links

