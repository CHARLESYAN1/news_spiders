# coding=utf-8
# author: shuqing.zhou

# User-Agent
UA = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# 采集超时时间
FETCH_TIMEOUT = 20

# 测试URL
TEST_URL = "http://www.baidu.com"
MARK = "www\.baidu\.com"

# 采集的站点
PROXY_SITES = [
    {
        "site": "http://proxy.ipcn.org/proxylist.html",
        "page": 1,
        "type": "re",
        "re": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}"
    },
    {
        "site": "http://www.kxdaili.com/dailiip/1/%s.html#ip",
        "page": 10,
        "type": "bs4",
        "select": {
            "base": "tbody > tr",
            "last": "td",
            "ip": 0,
            "port": 1
        }
    },
    {
        "site": "http://proxy.goubanjia.com/free/gngn/index.shtml",
        "page": 1,
        "type": "bs4",
        "select": {
            "base": "tbody > tr",
            "last": "td",
            "ip": 0,
            "port": 1
        }
    },
    {
        "site": "http://www.cz88.net/proxy/",
        "page": 1,
        "type": "bs4",
        "select": {
            "base": "#boxright .box694 ul li",
            "last": "div",
            "ip": 0,
            "port": 1
        }
    },
    {
        "site": "http://www.ip3366.net/?page=%s",
        "page": 10,
        "type": "bs4",
        "select": {
            "base": "tbody > tr",
            "last": "td",
            "ip": 0,
            "port": 1
        }
    },
    {
        "site": "http://www.xicidaili.com/nn/%s",
        "page": 20,
        "type": "bs4",
        "select": {
            "base": "tbody > tr",
            "last": "td",
            "ip": 0,
            "port": 1
        }
    },
    {
        "site": "http://www.swei360.com/free/?stype=1&page=%s",
        "page": 7,
        "type": "bs4",
        "select": {
            "base": "tbody > tr",
            "last": "td",
            "ip": 0,
            "port": 1
        }
    },
    {
        "site": "http://www.xsdaili.com/index.php?s=/index/mfdl/p/%s.html",
        "page": 100,
        "type": "bs4",
        "select": {
            "base": "tbody > tr",
            "last": "td",
            "ip": 0,
            "port": 1
        }
    },
    {
        "site": "http://www.89ip.cn/tiqu.php?sxb=&tqsl=200&ports=&ktip=&xl=on&submit=%CC%E1++%C8%A1",
        "page": 1,
        "type": "re",
        "re": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}"
    },
    {
        "site": "http://m.66ip.cn/nmtq.php?getnum=&isp=0&anonymoustype=0&start=&"
                "ports=&export=&ipaddress=&area=1&proxytype=2&api=66ip",
        "page": 1,
        "type": "re",
        "re": r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}"
    },
]
