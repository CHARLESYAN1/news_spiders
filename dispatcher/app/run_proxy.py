import sys
import time
from os.path import dirname, abspath

import schedule

sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

from  dispatcher.proxy.proxy import crawl_proxy_ip

schedule.every(5).minutes.do(crawl_proxy_ip)

while True:
    schedule.run_pending()
    time.sleep(1)


