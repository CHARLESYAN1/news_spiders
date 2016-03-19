# -*- coding: utf-8 -*-
from .. import app
from .base import BaseSched, Intervals


def dispatch_jobs():
    # 该任务一天执行一次， 在每天零点时， 由其他job取消该任务， 并在此重启该任务
    bs = BaseSched()
    overall_sites = bs.overall_sites
    intervals = Intervals().intervals

    for site, interval_type_dict in intervals.iteritems():
        for type_key, interval in interval_type_dict.iteritems():
            kw_values = overall_sites[site]
            bs.dispatch_job(type_key, interval, kw_values)

    rest_sites_keys = set(overall_sites.keys()) - set(intervals.keys())

    for _rest_keys in rest_sites_keys:
        # 将剩下的网站按照三个时间段分开增加任务
        bs.dispatch_job(1, 5, overall_sites[_rest_keys])
        bs.dispatch_job(2, 8, overall_sites[_rest_keys])
        bs.dispatch_job(3, 10, overall_sites[_rest_keys])


@app.scheduled_job(trigger='cron', hour='0', minute='0', second='0')
def restart_jobs():
    app.remove_all_jobs()
    dispatch_jobs()

app.add_job(dispatch_jobs, trigger='date')

