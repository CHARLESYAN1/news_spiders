# -*- coding: utf-8 -*-
import os
import os.path
import logging
from logging.handlers import RotatingFileHandler

from ..conf import news_config


class _LogBase(object):
    def __init__(self):
        self.config = news_config.settings
        self.datefmt = '%Y-%m-%d %H:%M:%S'
        self.log_path = self.config['LOG_PATH']
        self.log_level = self.config.get('LOG_LEVEL', logging.DEBUG)
        self.formatter = '[%(levelname)s]: %(asctime)s %(message)s\n'

        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

    @property
    def exec_msg(self):
        return 'Msg: [{msg}], {exec_info}'

    def logfile(self, name):
        return os.path.join(self.log_path, name + '.log').replace('\\', '/')


class Logger(_LogBase):
    """
    1: The `Logger` Class not for the logging system
    2: 'root' logger for the logging system:
        logging.basicConfig(**kwargs)
        logging.debug() | logging.info() | logging.warning() | logging.error() | logging.critical()
    """
    def __init__(self, filename):
        """ 打印日志文件， 只在这个文件里(logger.py)， 尽管其他模块调用也是在这样 """
        super(Logger, self).__init__()
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.log_level)

        # RotatingFileHandler need parameters
        file_handler = RotatingFileHandler(
            filename=self.logfile(filename),
            backupCount=10,
            maxBytes=5 * 1024 * 1024
        )
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(self.formatter, self.datefmt)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)


