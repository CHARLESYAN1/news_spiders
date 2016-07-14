# -*- coding: utf-8 -*-
import logging
import time

from scrapy.http import HtmlResponse

from selenium.webdriver import PhantomJS
from selenium.webdriver.support.ui import WebDriverWait

from news_spiders.conf import news_config


class WeixinMiddleware(object):
    def process_request(self, request, spider):
        weixin_start = 'weixin_start'
        try:
            key = request.meta[spider.conf_key]
            weixin_config = spider.config[key]
        except (KeyError, AttributeError):
            spider.log("Don't have Weixin", level=logging.INFO)
        else:
            belong = weixin_config.get('belong')

            # 所有的链接都会走该中间件， 必须过滤一下
            if belong and belong == 'weixin' and request.meta.get(weixin_start) is True:
                return WeixinCrawler(request, weixin_config, spider).response()


class WeixinCrawler(object):
    """ 微信抓取通过 Phantomjs 来抓取，尽管通过这种方法的抓取效率不高， 但对少数抓取还可以 """
    def __init__(self, request, config, spider):
        self.request = request
        self.config = config
        self.spider = spider
        self.settings = news_config.settings
        self.driver = PhantomJS(self.settings['PHANTOMJS_PATH'])
        self.open()

    def open(self):
        try:
            self.driver.get(self.request.url)
            self.driver.set_page_load_timeout(4)

            self.until()
        except Exception as e:
            self.spider.log('Open Weixin with PhantomJS or Firefox err: typ <{}>, msg <{}>'.format(
                e.__class__, e), level=logging.INFO)

    @property
    def tag_func(self):
        blocks = self.config.get('location_tags')

        if blocks is None:
            self.spider.log('incorrect element name', level=logging.INFO)

        for css, selector in blocks:
            if css == 'id':
                return lambda driver: driver.find_element_by_id(selector)
            elif css == 'class':
                return lambda driver: driver.find_element_by_class_name(selector)
            else:
                pass
        raise

    def until(self):
        try:
            # Have `click` function to specified element
            tag = WebDriverWait(self.driver, 20).until(self.tag_func)
        except Exception as e:
            self.spider.log("PhantomJS or Firefox don't find element: type <> err <>".format(
                e.__class__, e), level=logging.INFO)
        else:
            tag.click()
            time.sleep(3)

    def response(self):
        # 点击元素后可能不在同一个页面，当生成新的窗口时，必须赚到新窗口才能获取该窗口的元素
        # 目前微信公众号点击后会生成一个窗口
        current_window = self.driver.current_window_handle
        window_handles = self.driver.window_handles
        window_handles.remove(current_window)

        self.driver.switch_to.window(window_handles[0])
        time.sleep(3)
        # html = self.driver.find_elements_by_class_name('weui_media_title')
        html = self.driver.page_source
        self.driver.quit()
        return HtmlResponse(url=self.request.url, body=html.encode('utf-8'), request=self.request)


