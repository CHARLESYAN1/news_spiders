import os
from os.path import dirname, abspath

from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor

from news_spiders.utils import Logger

logger = Logger('dispatch_jobs')


def create_jobstrore_sqlite():
    sqlite_path = dirname(abspath(__file__))
    for sql_path in os.listdir(sqlite_path):
        if sql_path.endswith('.db'):
            os.remove(os.path.join(sqlite_path, sql_path))

# create_jobstrore_sqlite()

jobstores = {
    'default': MemoryJobStore(),
    # 'default': SQLAlchemyJobStore(url='sqlite:///jobs.db')
}

# using ThreadPoolExecutor as default other than ProcessPoolExecutor(not work) to executors
executors = {
    'default': ThreadPoolExecutor(35),
    # 'processpool': ProcessPoolExecutor(50)
    # 'default': ProcessPoolExecutor(20)  # not work
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}
app = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

