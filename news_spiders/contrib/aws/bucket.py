import os
import ssl
import boto
from boto.s3 import connection

from ...conf import news_config


class Base(object):
    def __init__(self):
        self.config = news_config.settings

    @property
    def access_key(self):
        return self.config['AWS_ACCESS_KEY_ID']

    @property
    def secret_key(self):
        return self.config['AWS_SECRET_ACCESS_KEY']

    @property
    def host(self):
        return self.config['AWS_HOST']

    @property
    def bucket_name(self):
        return self.config['BUCKET_NAME']


class Bucket(Base):
    def __init__(self):
        super(Bucket, self).__init__()

        self.conn = boto.connect_s3(
                aws_access_key_id=self.config.access_key,
                aws_secret_access_key=self.config.secret_key,
                host=self.config.host,
                calling_format=boto.s3.connection.OrdinaryCallingFormat(),
        )

    def all_buckets_name(self):
        return [bucket.name for bucket in self.conn.get_all_buckets()]

    def lookup(self):
        return self.conn.lookup(self.bucket_name)

    def get_buck(self):
        return self.conn.get_bucket(self.bucket_name)

    def create_bucket(self):
        """ Temporary don't have to implement """
        pass

    def delete_bucket(self):
        """ Temporary don't have to implement """
        pass

    def put(self, key_name, filename):
        """
        :param key_name: key name of Amazon S3
        :param filename: Store local directory filename path
        """
        try:
            bucket = self.get_buck()
            key = bucket.new_key(key_name)
            key.set_contents_from_filename(filename)
        except Exception as e:
            pass

    def get(self, key_name, filename=None):
        """
        :param key_name: key name of Amazon S3
        :param filename: Store local directory filename path
        :return `boto.s3.key.Key` class instance
        """
        try:
            bucket = self.get_buck()
            key = bucket.get_key(key_name)

            if key and filename is not None:
                key.get_contents_to_filename(filename)

            return key
        except ssl.SSLError:
            pass

    def list_keys(self, prefix=''):
        """
        List key from S3 bucket
        :param prefix: key part
        """
        try:
            bucket = self.get_buck()
            lister = bucket.list(prefix)

            for key in lister:
                yield key.name
        except ssl.SSLError:
            yield

    def delete_key(self):
        pass

    def close(self):
        return self.conn.close()

if __name__ == '__main__':
    s3 = Bucket()
    # print s3.all_buckets_name()
    # s3.put(
    #         'csf_news/20151222/20151222165800_EXZbSmio079184.txt',
    #         r'D:\temp\csf_news\20151222\20151222165800_EXZbSmio079184.txt'
    # )
    for k, _key in enumerate(s3.list_keys('data/news/'), 1):
        print _key,
    # kkey = s3.get('csf_news/20151222/20151222165700_tWIyqUEP65178.txt', r'D:\temp\data\ssss3.txt')
    # print kkey, type(kkey)
