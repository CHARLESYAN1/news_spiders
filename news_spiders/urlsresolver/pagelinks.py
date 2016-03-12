from scrapy import Selector as _Sl

from .base import BaseURi
from ..settings import news_settings
from ..utils import converter, RegexType
from .base import BaseLinksResolver as _Blr


class LinkFilter(object):
    project_settings = {
        _attr: getattr(news_settings, _attr)
        for _attr in dir(news_settings)
        if _attr[0].isupper()
        }

    def is_trash(self, link=None):
        """
        return value first is flag, second is site key, third is related trash
        :param link: url, whether filter or not
        """
        flag, domain, trashes = False, None, None
        domain_trash = self.project_settings.get('PAGE_URI_TRASH', {})

        if not link:
            return flag, domain, trashes

        for _domain, _trash in domain_trash.iteritems():
            if _domain in BaseURi.hostname(link):
                # _domain could not as return value
                return True, _domain, _trash
        return flag, domain, trashes

    def page_uri_trash(self, old_multi_uris):
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
                if not new_urls or BaseURi.uniform_hostname(new_urls[-1], _uri):
                    # If have multi news text, make sure that hostname of next url is the same before
                    new_urls.append(_uri)
        return new_urls


class PageLinks(LinkFilter):
    def __init__(self, selector, page_tags):
        self._selector = selector
        self._blr = _Blr(selector)
        self._page_tags = page_tags

    def get_links_from_regex(self, regex):
        urls = []
        html = self._selector.response.body_as_unicode()
        match = regex.search(html)

        if match is not None:
            text = match.groupdict().get('multi_page', '')

            for _link in _Sl(text=text).xpath('//a/@href').extract():
                url = self._blr.join_url(_link)
                if url and url not in urls:
                    urls.append(url)
            html = html[match.end() + 1:]
        return urls

    def get_links_from_xpath(self, css):
        urls = []
        css_selector, index, _ = converter(css)
        links = self._selector.css(css_selector)[index].xpath('.//a/@href').extract()

        for _link in links:
            url = self._blr.join_url(_link)
            if url and url not in urls:
                urls.append(url)
        return urls

    def get_page_links(self):
        urls = []
        first_url = self._selector.response.url

        for _query in self._page_tags:
            if isinstance(_query, RegexType):
                urls.extend(self.get_links_from_regex(_query))
            else:
                urls.extend(self.get_links_from_xpath(_query))

        if first_url in urls:
            urls = urls[urls.index(first_url) + 1:]
        return self.page_uri_trash(urls[:])
