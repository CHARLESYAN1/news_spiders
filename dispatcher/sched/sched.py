# -*- coding: utf-8 -*-
import os.path

from .. import app, logger
from .base import BaseSched, Intervals


# Notice that Just Only run 'dispatch_full_jobs' job one time
# @app.scheduled_job(trigger='date')
def dispatch_full_jobs():
    # 该任务一天执行一次， 在每天零点时， 由其他job取消该任务， 并在此重启该任务
    bs = BaseSched()

    if bs.is_migrate is None:
        return

    most_sites = bs.most_sites
    intervals = Intervals().intervals
    try:
        for site, interval_type_dict in intervals.iteritems():
            for type_key, interval in interval_type_dict.iteritems():
                kw_values = most_sites[site]
                bs.dispatch_job(type_key, interval, kw_values)

        rest_sites_keys = set(most_sites.keys()) - set(intervals.keys())

        for _rest_keys in rest_sites_keys:
            # 将剩下的网站按照三个时间段分开添加任务
            bs.dispatch_job(1, 5, most_sites[_rest_keys])
            bs.dispatch_job(2, 8, most_sites[_rest_keys])
            bs.dispatch_job(3, 10, most_sites[_rest_keys])
    except Exception as e:
        logger.info('Dispatch full jobs error: type <{}>, msg <{}>, file <{}>'.format(
            e.__class__, e, os.path.abspath(__file__)))
    print 'hahaha'


@app.scheduled_job(trigger='interval', minutes=2, seconds=30,)
def dispatch_hot_jobs():
    bs = BaseSched()

    if bs.is_migrate is None:
        return

    try:
        bs.schedule(site_name=bs.hot_sites)
    except Exception as e:
        logger.info('Dispatch hot jobs error: type <{}>, msg <{}>, file <{}>'.format(
            e.__class__, e, os.path.abspath(__file__)))


@app.scheduled_job(trigger='interval', minutes=4)
def dispatch_sgp_jobs():
    bs = BaseSched()

    if bs.is_migrate is not None:
        return

    try:
        bs.schedule(site_name=bs.sgp_sites)
    except Exception as e:
        logger.info('Dispatch Sgp jobs error: type <{}>, msg <{}>, file <{}>'.format(
            e.__class__, e, os.path.abspath(__file__)))


@app.scheduled_job(trigger='cron', hour='0', minute='0', second='0')
def restart_jobs():
    for job in app.get_jobs():
        if job.name != 'schedule':
            app.remove_job(job.id)

    dispatch_full_jobs()

dispatch_full_jobs()
