from collections import defaultdict
from scrapy import Spider, Selector
from scrapy import Request

from ..conf import news_config
from ..urlsresolver import PageUri
from ..urlsresolver import UrlsResolver
from ..exceptions import NotExistSiteError
from ..utils import populate_md5, deepcopy


class Collector(object):
    configs = {}
    start_urls = defaultdict(list)

    def __init__(self):
        self.__config_instance = news_config
        self.__init_config()

    def unique_name(self, name):
        return name in self.__config_instance.names

    def __init_config(self):
        """ get total url as start_urls to offer Spiders, then populate related site configs """
        required_configs = self.__config_instance.total_configs

        for _config in required_configs:
            site_name = _config['site']
            base_conf = {_key: _value for _key, _value in _config.iteritems() if _key != 'urls'}

            for url_conf in _config['urls']:
                base_url = url_conf['page_url']
                url_fill_rule = url_conf['first']
                start_page = url_conf.get('start', 1)

                while start_page < url_conf.get('pages', 1) + 1:
                    # Deal with turning page to site link, and Populate config to each page url
                    required_url = PageUri(site_name, base_url, url_fill_rule, start_page).get_page_url()

                    _conf_key = populate_md5(required_url)
                    self.start_urls[site_name].append(required_url)
                    self.configs[_conf_key] = deepcopy(base_conf)
                    self.configs[_conf_key].update(cate=url_conf['cate'])

                    start_page += 1
                    url_fill_rule = url_conf['suffix'] or url_fill_rule

    def get_config(self, site_name, cate='test'):
        for _config in self.__config_instance.total_configs:
            if site_name == _config['site']:
                required_config = {_key: _value for _key, _value in _config.iteritems() if _key != 'urls'}
                required_config.update(cate=cate)
                return required_config
        raise ValueError("Not existed site name: <%s> in configs" % site_name)


class BaseCommonSpider(Spider):
    """
     Here using Spider class, If inherit CrawlSpider class, so then not convenient to control config
    """
    name = 'news_spiders'
    collector = Collector()

    def __init__(self, name=None, url=None, **kwargs):
        self.start_urls = []
        self.config = self.collector.configs

        if name is None and url is None:
            # crawl config of all site web, then get total urls as start_urls
            # self._start_urls()
            self.start_urls = [_url for _url in self.collector.start_urls.itervalues()]
        elif name and url is None:
            # crawl specified site, then get all urls as start_urls
            if self.collector.unique_name(name):
                # self._start_urls(name)
                self.start_urls = [_url for _url in self.collector.start_urls[name]]
            else:
                raise NotExistSiteError("Don't existed this name <%s> in site configs" % name)
        elif name and url:
            # just get the url news to specified site, this url as start_urls
            self.single = True
            self.start_urls = [url]
            self.config[populate_md5(url)] = self.collector.get_config(name)

        super(BaseCommonSpider, self).__init__(name=self.name, **kwargs)

    def start_requests(self):
        for url in self.start_urls:
            if not getattr(self, 'single', False):
                yield Request(url=url, callback=self.parse)
            else:
                yield Request(
                    url=url,
                    callback=self.parse_news,
                    meta={self.conf_key: populate_md5(url)}
                )

    def parse(self, response):
        conf_value = populate_md5(response.url)
        norm = (lambda _uri, _pub='', _auth='': (_uri, _pub, _auth))
        total_urls = UrlsResolver(Selector(response), self.config[conf_value]).resolve()
        print total_urls, self.config[conf_value]

        for _each_url in total_urls:
            url, pub_dt, auth = norm(*_each_url)
            yield Request(
                url=url,
                callback=self.parse_news,
                meta={
                    'auth': auth,
                    'pub_dt': pub_dt,
                    self.conf_key: conf_value,
                })

    @property
    def conf_key(self):
        return self.settings['CONFIG_KEY']

    def parse_news(self, response):
        raise NotImplementedError





