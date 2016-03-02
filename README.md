News_Spiders
============

概述
----

此系统的任务是抓取 hot_news 与 full_news 新闻任务：
    
    1: 程序 'news_crawler/hot_tun.py'
    hot_news 包括主要知名的和本公司指定的财经类网站:
    (1): 每天基本上是10分钟跟新一次
    (2): 增加了早高峰， 晚高峰功能
    (3): 鉴于频率的考虑， 在休息日和国家法定节假日中降低抓取频率
    
    2：程序 'news_crawler/full_tun.py' 
    full_news 包括热点新闻， 公司新闻，行业新闻，宏观新闻，新三板新闻，港股新闻， 美股新闻（基于国内中文的美股新闻文章）
    （1）：每天20分钟抓取一次
     (2): 增加了早高峰， 晚高峰功能
     (3): 鉴于频率的考虑， 在休息日和国家法定节假日中降低抓取频率

主要说明
--------

目前基于协程并发的思想来抓取网站新闻，当然这个方案目前还在测试，原则上对抓取过的新闻都有基本的过滤，包括链接，关键词，剔除新闻的某些干扰文本等，

模块说明
--------

	(1): pyq_news_crawler/configs:    
	    对所有网站新闻的配置， 包括新闻文本的存储路径，数据库备份路径， 抓取配置等其他的配置
	    a: cbase.py: 基本的配置文件， 如过滤关键词， 存储路径等其他配置
	    b: cfull.py: 全量新闻各个网站抓取元素的配置
	    c: cfund.py: 基金新闻各个网站抓取元素的配置
	    d: chk.py:   港股新闻各个网站抓取元素的配置
	    e: chot.py:  热点新闻(cat 为`hot` 和 `hjd`)各个网站抓取元素的配置， 为智投产品和京东提供的新闻
	    f: chot_in_full.py:     全量新闻中热点新闻(cat 为`热点新闻`)的各个网站抓取元素的配置
	    g: csanban.py:          新三板新闻的各个网站抓取元素的配置
	    h: cusa.py:             美股新闻的各个网站抓取元素的配置
	    i: cyamaxun.py:         在亚马逊服务器上抓取的各个网站抓取元素的配置
	    k: dispatch.cfg:        暂时没用
	    l: sched.cfg:           全量和热点新闻的抓取时间限制和调度配置

	(2): pyq_news_crawler/decorators:   
	    一些预处理和装饰函数

	(3): pyq_news_crawler/dispatch:

	    allocator.py:   主要的任务分派工作， 对各个网站的参数分配和抓取调度
	    
	    handlers.py:    具体的数据抓取，处理过程
	    
	    scheduler.py:   对抓取任务以时间调度的工作
	    
	    storage.py:     抓取的新闻的存储和备份
	   
	(4): pyq_news_crawler/eggs:    
	    常用的工具集合
	     database:  包括基本的mongo DB， file BSD接口， 
	     utils:     包括配置工具， 下载， 日志， 过滤等
	     
    (5）：pyq_news_crawler/frequency:   
        关于抓取调度类的接口

	(6): pyq_news_crawler/test_case:    
	    基本的测试， 可按照具体的网站测试和具体的URI测试

	(7): pyq_news_crawler/wheel:        
	    解析新闻数据的所需的各种轮子， 目前这些轮子包括了现有的这些网站的的所有解析情况，
	    包括url, title， pub_date, author, content
	    
	(8): pyq_news_crawler/contrib:  
	   迁移至 Amazon上传文件的接口

部署及远程仓储
-------------
（1）：远程仓储：git@gitlab.chinascope.net:scraper/news_crawler.git

（2）：部署：

    a: 目前部署上海环境在192.168.250.207:/opt/news_analyse/
    
    b：后期迁移至北京 Amazon（54.223.52.50：/opt/scraper/）和新加坡 Amazon（54.251.106.214:/opt/scraper/）上

运行脚本：
--------
(1): full_run.py: 在192.168.250.207服务器上运行的全量新闻抓取

(2): hot_run.py: 在192.168.250.207服务器上运行的全量新闻抓取

新增功能：
-------
（1）一部分国外网站的新闻在新加坡亚马逊服务器运行, 这部分的新闻网站在北京亚马逊无法访问， 并将抓取的新闻上传至S3

（2）由于等到年后才全部迁移至北京亚马逊上， 目前对于这些国外网站抓取的新闻在上海环境需要从S3上下载下来， 后提供给arvin分析

（3）在北京亚马逊抓取服务器上， 已经写了部分接口将国外网站抓取的新闻从S3上下载下来， 并提供给北京亚马逊分析服务器的程序分析

    a: 该功能起初是通过从S3上直接将文件拉倒 Office 207 环境， 鉴于需求的增加，将会改进此方法
    b： 通过redis发布订阅， 将新闻传递到Office 207环境， 或以后上线的 北京亚马逊环境。
    
 （4）：过滤之前是通过 db 文件途径， 目前正改进使用redis




