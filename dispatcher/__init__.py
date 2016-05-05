from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor

from news_spiders.utils import Logger

logger = Logger('dispatch_jobs')

jobstores = {
    'default': MemoryJobStore()
}

# using ThreadPoolExecutor as default other than ProcessPoolExecutor(not work) to executors
executors = {
    'default': ThreadPoolExecutor(20),
    # 'processpool': ProcessPoolExecutor(50)
    # 'default': ProcessPoolExecutor(20)  # not work
}

job_defaults = {
    'coalesce': False,
    'max_instances': 1
}
app = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults)

