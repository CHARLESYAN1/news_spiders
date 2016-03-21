import os
import simplejson

from .mq import MessageQueue


class ConvertBase(MessageQueue):
    keys = ['url', 'dt', 'auth', 'cat', 't', 'con', 'rat', 'crt', 'fn']

    def to_queue(self, filename, typs):
        """
        Read file data to yield serializable data
        :param filename: absolute path to the file
        :param typs: Only 1 or 2, if typs = 1, it is hot news, else typs = 2, it is full news
        """
        data = []
        fn = os.path.basename(filename)

        try:
            with open(filename) as fp:
                data.extend([_line.strip() for _line in fp])

            data.append(fn)

            dumps = simplejson.dumps(dict(zip(self.keys, data)))
        except (IOError, simplejson.JSONDecodeError) as e:
            pass
            # logger_error.info('Yield Serialization Data from file Error: [{}], file path: [{}]'.format(e, filename))
        else:
            if len(self.keys) == len(data):
                self.push(dumps, typs)
            else:
                pass
                # logger_error.info('Keys count not equal to line count, keys:[{}], file lines:[{}]\n\t-->[{}]'.format(
                #         self.keys, len(data), filename
                # ))

    def to_file(self, message, news_path):
        """
        Make serializable data to yield file
        :param message: json data format, serializable data from redis queue
        :param news_path: absolute directory path, message will store file
        """
        try:
            data = simplejson.loads(message)
            filename = data.pop('fn')
            lines = [data[_key] for _key in self.keys[:-1]]

            with open(news_path + filename, 'w') as fp:
                lines_seq = '\n'.join(lines).encode('u8')
                fp.writelines(lines_seq)

            # logger_error.info('Yield File Success: [%s]' % (news_path + filename))
        except (KeyError, IOError, simplejson.JSONDecodeError) as e:
            pass
            # logger_error.info('Serialization Data write to file Error: [{}], Message: [{}]'.format(e, message))


class PickleToQueue(ConvertBase):
    """
    The class aim at the Singapore amazon fetching foreign Chinese website,
    Every time crawled news put serialized data into the queue from news path, make part two:
    One: hot news to put queue from hot news path
    Two: full news to put queue from full news path
    """

    def __init__(self):
        super(PickleToQueue, self).__init__()

    def send_message(self, filename, mq_typ):
        """
        :param filename: every time crawled news and absolute file path
        :param mq_typ: Only 1 or 2, if typ = 1, it is hot news, else typ = 2, it is full news
        """
        self.to_queue(filename, mq_typ)


class UnpickleToFile(ConvertBase):
    def __init__(self):
        super(UnpickleToFile, self).__init__()

    def convert_message(self, store_path, mq_typ):
        """
        :param store_path: absolute directory path
        :param mq_typ: Only 1 or 2, if typ = 1, it is hot news, else typ = 2, it is full news
        """
        while True:
            message = self.get_message(mq_typ)

            if not message:
                break

            self.to_file(message, store_path)
