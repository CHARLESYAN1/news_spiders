import os.path

from ... import app, logger


@app.scheduled_job(trigger='interval', seconds=90)
def crawl_proxy_ip():
    try:
        pass
    except Exception as e:
        logger.info('Crawl proxy ip error: type <{}>, msg <{}>, file <{}>'.format(
            e.__class__, e, os.path.abspath(__file__)))
