import os
from os.path import dirname, abspath

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

from dispatcher.sched.sched_weixin import dispatch_weixin_jobs


def create_sqlite():
    sqlite_path = dirname(abspath(__file__))
    for sql_path in os.listdir(sqlite_path):
        if sql_path.endswith('.db'):
            os.remove(os.path.join(sqlite_path, sql_path))

create_sqlite()

jobstores = {
    # 'mongo': MongoDBJobStore(database='test', collection='job', client=client),
    # 'default': MemoryJobStore()
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.db')
}

executors = {
    'default': ThreadPoolExecutor(2),
    # 'processpool': ProcessPoolExecutor(3)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}

weixin_app = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

dispatch_weixin_jobs(weixin_app)
weixin_app.start()
