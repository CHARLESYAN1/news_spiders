News_Spiders
============

概述
----
该项目主要为京东和智投App等抓取财经类新闻源资讯， 利用Scrapy框架来定制该新闻项目， scrapyd来部署项目， 利用scrapyd-api来间隔调度

主要说明
--------
抓取新闻的字段解析，关键词过滤，新闻文本冗余干扰， url过滤， redis消息推送与接收上传S3等操作， 在docs目录有文档详细解释

模块说明
--------
	docs目录下有详细的模块说明， 请翻阅。

部署及运行
-------------
（1）：部署环境：新加坡亚马逊（54.251.56.190：/opt/scraper）， 北京亚马逊（54.223.52.50：/opt/scraper）

（2）：运行：

    a: 进入虚拟环境： source {virtual_env_path}/bin/activate

    b: 北京亚马逊： python dispatcher/app/run)jobs.py
    
    c：新加坡亚马逊： python dispatcher/app/run)jobs.py

新增功能：
-------
 基于redis实现的分布式功能, 主从复制， 如果两台机器，可以主从复制， 将主机的过滤数据时刻同步到从机， 以达到同步过滤的要求

1:实时抓取接口

方法：GET: 54.222.222.172:7955/api/crawlers/?url=<url>

说明： 查询字符串是已有配置的财经类新闻网站的某个url


改进的地方 ：
1： 配置文件可以放进数据库里， 如mongo， 在配置不是很大的情况下， 可以放在.py文件中

2：默认调度队列是在redis中scheduler_queue:requests下， 这是包括所有站点的requests(即URL请求)都放在了该队列中。

    改进的地方：可以采用scheduler_queue:requests:site_A, scheduler_queue:requests:site_B的样式为每个站点提供一个对列
    
3：现在我们对新闻的抓取， 抓取通过先填写配置文件， 修改解析规则(html. ajax, 抓取的数据在script标签里， 等等)URL，
如果元素提取不出来，可能还要进一步修改元素解析规则，包括新闻发布时间， 标题， 正文， 正文的文本抽取在网上都有一些包
（没有100%抽取准确，但也有接近90%以上的准确率），但是时间的抽取可能没有好的方法(至少目前我遇到的)，能不能通过一种机器学习的方法自动的学习提取时间， 标题和文本内容

    
