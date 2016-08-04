# -*- coding: utf-8 -*-
import sys
import simplejson
import time
from os.path import abspath, dirname

from flask import request
from tld import get_tld
from pymongo import MongoClient
from scrapyd_api import ScrapydAPI

sys.path.append(dirname(dirname(abspath(__file__))))

from crawlers_api import app
from news_spiders.utils import populate_md5
from news_spiders.conf import news_config
from news_spiders.settings.news_settings import \
    AMAZON_BJ_MONGO_HOST, AMAZON_BJ_MONGO_DB, AMAZON_BJ_MONGO_CRAWLER


spider_name = 'news'
project = 'news_spiders'
scrapy_host = 'http://localhost:6800'


def get_related_site(url):
    usage_sort = ['full', 'fund', 'sanban']
    # usage_sort = ['full', 'hot', 'hif', 'fund', 'sanban', 'usa', 'hk', 'gp']

    query_site_name = []
    required_names = []
    domain = get_tld(url, as_object=True).domain
    site_names = [conf['site'] for conf in news_config.total_configs]

    for site_name in site_names:
        if domain == site_name.split('_')[1]:
            query_site_name.append(site_name)

    for k in usage_sort:
        required_names.extend([st for st in query_site_name if k == st.split('_')[0]])

    return required_names


def run_scrapy_schedule(url, site_name):
    kwargs = {'site_name': site_name, 'url': url}
    return ScrapydAPI(target=scrapy_host).schedule(project, spider_name, **kwargs)


def detect_status(jobid):
    times = 1

    while times <= 10:
        status = ScrapydAPI(target=scrapy_host).job_status(project, jobid)

        if status == 'finished':
            return True
        times += 1
        time.sleep(0.4)


def get_data(collection, url_md5):
    fields = {'title': 1, 'content': 1}

    news_data = collection.find_one({'uid': url_md5}, fields)

    if news_data:
        news_data.pop('_id')
        data = simplejson.dumps({'t': news_data['title'], 'c': news_data['content']})
        return simplejson.dumps({"status_code": 200, 'message': u"抓取成功", 'data': data, 'uid': url_md5})


@app.route(r'/api/crawlers/', methods=['GET', 'POST'])
def crawlers_api():
    key = 'url'
    client = MongoClient(AMAZON_BJ_MONGO_HOST)
    collection = client[AMAZON_BJ_MONGO_DB][AMAZON_BJ_MONGO_CRAWLER]

    if request.method == 'GET':
        url = request.args.get(key)

        if url is None:
            return simplejson.dumps({"status_code": 404, 'message': u"参数错误", 'data': {}})

    # 先判断mongo里是否存在
    url_md5 = populate_md5(url)
    pre_data = get_data(collection, url_md5)

    if pre_data:
        return pre_data

    # 若mongo未查询到， 再抓取
    site_name_list = get_related_site(url)
    for site_name in site_name_list:
        jobid = run_scrapy_schedule(url, site_name)

        if detect_status(jobid):
            data = get_data(collection, url_md5)

            if data:
                return data

    client.close()
    return simplejson.dumps({"status_code": 404, 'message': u"未抓取到内容", 'data': {}, 'uid': url_md5})


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', 7955)

    # from datetime import datetime
    # _url = 'http://finance.sina.com.cn/china/gncj/2016-08-02/doc-ifxunyxy6277883.shtml'
    # print datetime.now()
    # run_scrapy_schedule(_url, 'full_sina')
    # print datetime.now()
    detect_status('2a07ce0f592711e695e9005056c00008')
