import os
import simplejson

from .mq import MessageQueue


class ConvertBase(MessageQueue):
    keys = ['url', 'dt', 'auth', 'cat', 't', 'con', 'rat', 'crt', 'fn']

    def from_file(self, filename, typs):
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


class SerializationToQueue(ConvertBase):
    """
    The class aim at the Singapore amazon fetching foreign Chinese website,
    Every time crawled news put serialized data into the queue from news path, make part two:
    One: hot news to put queue from hot news path
    Two: full news to put queue from full news path
    """

    def __init__(self, filename, typ):
        """
        :param filename: every time crawled news and absolute file path
        :param typ: Only 1 or 2, if typ = 1, it is hot news, else typ = 2, it is full news
        """
        self.typ = typ
        self.filename = filename

        super(SerializationToQueue, self).__init__()

    def send_message(self):
        self.from_file(self.filename, self.typ)


class ConvertToFile(ConvertBase):
    def __init__(self, news_path, typ):
        """
        :param news_path: absolute directory path
        :param typ: Only 1 or 2, if typ = 1, it is hot news, else typ = 2, it is full news
        """
        self.typ = typ
        self.news_path = news_path

        super(ConvertToFile, self).__init__()

    def messages_to_file(self):
        while True:
            message = self.get_message(self.typ)

            if not message:
                break

            self.to_file(message, self.news_path)
