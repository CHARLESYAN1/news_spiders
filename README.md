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
 基于redis实现的分布式功能


