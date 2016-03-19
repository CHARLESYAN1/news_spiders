from dispatcher.sched.sched import Intervals
from collections import defaultdict
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from datetime import datetime

jobstores = {
    'default': MemoryJobStore()
}

executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}
app = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)


def sub_job():
    print datetime.now(), 'count:', len(app.get_jobs())
    print app.get_jobs(), '\n\n'


def dispatch_jobs():
    print 'dis:', datetime.now(), app.get_jobs()
    app.add_job(sub_job, 'interval', seconds=10)


# @app.scheduled_job(trigger='cron', hour='18', minute='27', second='0')
def restart_jobs():
    func_name = 'restart_jobs'
    for _job in app.get_jobs():
        if _job.name != func_name:
            app.remove_job(_job.id)
    dispatch_jobs()

app.add_job(restart_jobs, trigger='cron', hour='18', minute='45', second='0')
app.add_job(dispatch_jobs, trigger='date')

app.start()

