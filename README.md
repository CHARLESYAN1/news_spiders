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
（1）：部署环境： 北京亚马逊（54.223.52.50：/opt/scraper），新加坡亚马逊（54.251.56.190：/opt/scraper）

说明：

1：并不直接启动脚本，而是通过supervisor这样的进程管理程序启动；

2：位置：54.251.56.190：/opt/scraper
        

（2）：运行：

    a: 北京亚马逊使用supervisor来启动抓取调度程序， 具体参看：54.223.52.50:/etc/supervisord.conf文件的启动方式
    b: 新加坡亚马逊与上类似
    
特别说明：
-----
1： url解析

说明：首先从网站拿到初步的url, 由于这些urls可能不规范， 所以必须统一已处理已形成”http……..”
Package: news_spiders/news_spiders/urlsresolver

2：时间解析

说明：由于各网站网页时间的写法不一样， 必须将时间转换成14位字符串：“2160914100525”
Package: news_spiders/news_spiders/itemsresolver/dateresolver.py

3：新闻来源解析

说明：新闻来源有时与发布时间在同个标签， 有时在不同标签内， 不同标签处理起来会相对好一点， 如果在同一标签， 属于”时间  新闻来源”， 还是”新闻来源  时间”， 只需要改动pyq_date_author还是pyq_author_date。具体参考代码的解决方案
Package: news_spiders/news_spiders/itemsresolver/authresolver.py

4： 文本解析

说明：新闻文本解析， 每段新闻需要用“#&#”来区分；有时文本中含有一些冗余文本（比如：腾讯财经新闻的很多新闻末尾会来一段”微信扫一扫”, “扫描二维码”, 那么我们只需要保留该字样前面的文本即可），具体的实现逻辑可参照代码。
Package: news_spiders/news_spiders/itemsresolver/textresolver.py

5：过滤

说明：这里包括关键字（可见配置文件）过滤和url过滤(即相同的url在下一次不在抓取)
Package: news_spiders/news_spiders/utils/filter.py(关键字过滤)和 news_spiders/news_spiders/schema/dupefilter.py(包括了redis url 过滤)

6：统一环境文件传送

说明：这里有两种情况：

	A: 北京亚马逊54.223.52.50（新闻抓取服务器）传到 54.223.46.84(文本分析服务器)， 将文件用相同目录从50传到84上

	B: 新加坡亚马逊 54.251.56.190将分析后的文本推入redis队列里， 然后在北京亚马逊这边将文本信息解析出来，生成文件， 最终按照A的方式传到84上
	注意：A是必须保证正确稳定执行，B不是最主要的

Package: 调度在news_spiders/dispatcher/transfer/sender.py下，基本的文件传送在：news_spiders\news_spiders\contrib\transfer\smooth.py

7：部署问题(先scrapyd-deploy部署， 再上传工程启动项目)

说明： 一般有本机和北京亚马逊 54.223.52.50机器分别部署scrapyd服务， 然后在本机上通过
scrapyd-deply server_amazon_bj –p news_spiders –v news_spiders_formal 

将工程打包到 北京亚马逊 50机器(部署了scrapyd服务)， 然后上传工程在指定目录，启动 news_spiders/dispatcher/app/run_jobs.py脚本调度


新增功能：
=========
 基于redis实现的分布式功能, 主从复制， 如果两台机器，可以主从复制， 将主机的过滤数据时刻同步到从机， 以达到同步过滤的要求

改进的地方 ：

1： 配置文件可以放进数据库里， 如mongo， 在配置不是很大的情况下， 可以放在.py文件中

2：默认调度队列是在redis中scheduler_queue:requests下， 这是包括所有站点的requests(即URL请求)都放在了该队列中。

改进的地方：可以采用scheduler_queue:requests:site_A, scheduler_queue:requests:site_B的样式为每个站点提供一个对列
    
3：现在我们对新闻的抓取， 抓取通过先填写配置文件， 修改解析规则(html. ajax, 抓取的数据在script标签里， 等等)URL，
如果元素提取不出来，可能还要进一步修改元素解析规则，包括新闻发布时间， 标题， 正文， 正文的文本抽取在网上都有一些包
（没有100%抽取准确，但也有接近90%以上的准确率），但是时间的抽取可能没有好的方法(至少目前我遇到的)，能不能通过一种机器学习的方法自动的学习提取时间， 标题和文本内容


实时抓取接口：
=======

1:实时抓取接口

方法：GET: 54.222.222.172:7955/api/crawlers/?url=<url>

2:新增实时抓取接口

方法：GET: 54.222.222.172:7955/api/crawlers/v2?url=<url>

说明： 查询字符串是已有配置的财经类新闻网站的某个url

实时接口的说明：
-------------
逻辑：本接口是基于news_spiders 项目， 先进行抓取，然后在规定的时间内判断是否在数据库中有备份了该url抓取的新闻数据，
目前是在54.223.223.172重新部署 news_spiders 项目，然后提供接口。

部署：按照54.223.52.50的方式在54.223.223.172重新部署news_spiders 项目

接口代码：news_spiders/crawlers_api/api.py

执行方式：通过supervisor管理接口， supervisor + flask + gunicorn 来部署
    
