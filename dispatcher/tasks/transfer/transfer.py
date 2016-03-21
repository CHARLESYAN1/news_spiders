import os
import os.path

from .. import app
from .base import Base


def transport(self, dir_path, filename):
    local_path = dir_path + filename

    if self.filter_files(dir_path + filename):
        self.goosy.put(local_path, dir_path)

        s3_key = self.s3_key(dir_path, filename)
        self.bucket.put(s3_key, local_path)

        if self.is_migrate is None:
            # transfer news file to redis
            pass


@app.scheduled_job(trigger='interval', seconds='5')
def transfer():
    """ this function transfer crawled news file to analytic server and aws s3 bucket """
    self = Base()
    if not os.path.exists(self.hot_news_path):
        os.makedirs(self.hot_news_path)

    if not os.path.exists(self.full_news_path):
        os.makedirs(self.full_news_path)

    for filename in os.listdir(self.hot_news_path):
        transport(self, self.hot_news_path, filename)

    for filename in os.listdir(self.full_news_path):
        transport(self, self.full_news_path, filename)









