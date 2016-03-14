from .bucket import Bucket


def test():
    aws = Bucket()
    # path = '/opt/test/fls/20151222165700_tWIyqUEP651738.txt'
    # path = 'D:/temp/csf_news/20151222/20151222165700_tWIyqUEP651738.txt'

    # with open(path, 'rb') as fp:
    #     data = fp.read()

    key = 'data/'
    # aws.put(key, data)
    print len(list(aws.list_keys('data/news/csf_news/20160107/')))
