
from ...utils import Logger
from ...conf import news_config


logger = Logger('transfer')


class Base(object):
    def __init__(self):
        self.config = news_config.settings

    @property
    def inner_host(self):
        return self.config['ANALYSIS_SERVER_INNER_IP']

    @property
    def inner_pwd(self):
        return self.config['ANALYSIS_SERVER_PASSWORD']

    @property
    def inner_user(self):
        return self.config.get('ANALYSIS_SERVER_USER') or 'root'

    @property
    def inner_port(self):
        return self.config.get('ANALYSIS_SERVER_PORT') or 22


