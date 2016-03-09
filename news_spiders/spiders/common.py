from scrapy import Spider, Selector
from scrapy import Request

from ..urlsresolver import PageUri
from ..urlsresolver import UrlsResolver
from ..exceptions import NotExistSiteError
from ..conf import InitConfigs as _InitConfigs
from ..utils.utils import populate_md5, deepcopy


class Collector(object):
    config_instance = _InitConfigs()

    def unique_name(self, name):
        return name in self.config_instance.names

    def get_start_urls(self):
        """ get total url as start_urls to offer Spiders, then populate related site configs """
        _configs = {}
        _start_urls = []

        required_configs = self.config_instance.total_configs

        for _config in required_configs:
            site_name = _config['site']
            base_conf = {_key: _value for _key, _value in _config.iteritems() if _key != 'urls'}

            for url_conf in _config['urls']:
                cate = url_conf['cate']
                base_url = url_conf['page_url']
                url_fill_rule = url_conf['first']
                start_page = url_conf.get('start', 1)
                total_page = url_conf.get('pages', 1) + 1

                while start_page < total_page:
                    # Deal with turning page to site link
                    # Populate config to each page url
                    required_url = PageUri(
                        site_name=site_name,
                        base_url=base_url,
                        url_fill_rule=url_fill_rule,
                        page=start_page
                    ).get_page_url()

                    _conf_key = populate_md5(required_url)
                    _start_urls.append(required_url)
                    _configs[_conf_key] = deepcopy(base_conf)
                    _configs[_conf_key]['cate'] = cate

                    start_page += 1
                    url_fill_rule = url_conf['suffix'] or url_fill_rule

        return _start_urls, _configs


class BaseCommonSpider(Spider):
    """
     Here using Spider class, If inherit CrawlSpider class, so then not convenient to control config
    """
    name = 'news_spiders'
    collector = Collector()
    start_urls, config = collector.get_start_urls()

    def __init__(self, name=None, url=None, **kwargs):
        self.start_urls = []

        if name is None and url is None:
            # crawl config of all site web, then get total urls as start_urls
            self._start_urls()
        elif name and url is None:
            # crawl specified site, then get all urls as start_urls
            if self.collector.unique_name(name):
                self._start_urls(name)
            else:
                raise NotExistSiteError("Don't existed this name <%s> in site configs" % name)
        elif name and url:
            # just get the url news to specified site, this url as start_urls
            self.start_urls = [url]

        super(BaseCommonSpider, self).__init__(name=self.name, **kwargs)

    def _start_urls(self, name=None):
        class_start_urls = self.__class__.start_urls
        urls_mapping = {populate_md5(_url): _url for _url in class_start_urls}

        if name is None:
            self.start_urls = class_start_urls
            return

        for _url_md5, _config in self.config.iteritems():
            site_name = _config['site']
            if name == site_name:
                self.start_urls.append(urls_mapping[_url_md5])

    def parse(self, response):
        conf_value = populate_md5(response.url)
        total_urls = UrlsResolver(
            selector=Selector(response),
            config=self.config[conf_value],
        ).resolve()

        for _each_url in total_urls:
            yield Request(_each_url, self.parse_news, meta={self.conf_key: conf_value})

    @property
    def conf_key(self):
        return self.settings['CONFIG_KEY']

    def parse_news(self, response):
        raise NotImplementedError





