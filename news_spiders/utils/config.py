import os.path
from ConfigParser import ConfigParser as _ConfigParser

from ..exceptions import *


class BaseConfigParser(_ConfigParser):
    def __init__(self, absolute_config_path, *args, **kwargs):
        if not os.path.exists(absolute_config_path):
            raise NotExistFileError("Don't exist this file <%s>" % absolute_config_path)
        _ConfigParser.__init__(*args, **kwargs)

        self.absolute_config_path = absolute_config_path
        self.read(self.absolute_config_path)

    def get_sections(self):
        return self.sections()

    def get_options(self, section):
        return self.options(section=section)

    def get_option_value(self, section, option):
        return self.get(section=section, option=option)

