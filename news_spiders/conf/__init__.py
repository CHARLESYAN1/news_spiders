import socket
from importlib import import_module
from ConfigParser import NoSectionError

from .genconf import module_path
from ..exceptions import NotExistSiteError
from ..utils.config import BaseConfigParser as _BaseConfig


def make_dev_ip():
    """
    :return: the actual ip of the local machine.
        This code figures out what source address would be used if some traffic
        were to be sent out to some well known address on the Internet. In this
        case, a Google DNS server is used, but the specific address does not
        matter much.  No traffic is actually sent.
    """
    try:
        _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _socket.connect(('8.8.8.8', 80))
        address, port = _socket.getsockname()
        _socket.close()
        return address
    except socket.error:
        return '127.0.0.1'


class InitConfigs(_BaseConfig):
    """ This class mainly make configs to *.py file, not static to load configs """
    module_option = 'module_name'
    specified_section = 'specific'

    def __init__(self):
        _BaseConfig.__init__(self, module_path)

    def _get_configs(self, conf_name, package=None):
        if not self.is_valid(conf_name):
            raise NoSectionError("Don't existed <%s> section in <%s> file" % (conf_name, self.absolute_config_path))

        module_name = self.get_option_value(conf_name, self.module_option)
        module = import_module(name=module_name, package=package)
        return getattr(module, conf_name, [])

    def is_valid(self, section):
        return self.has_section(section=section)

    @property
    def config_sections(self):
        return [_section for _section in self.sections() if _section[0].isupper()]

    @property
    def hot_configs(self):
        conf_name = 'HOT_CONFIGS'
        return self._get_configs(conf_name)

    @property
    def amazon_configs(self):
        conf_name = 'AMAZON_CONFIGS'
        return self._get_configs(conf_name)

    @property
    def most_configs(self):
        specified_options = self.get_option_list(self.specified_section, 'option')
        most_sections = [_section for _section in self.config_sections if _section not in specified_options]
        return [_config for _section in most_sections for _config in self._get_configs(_section)]

    @property
    def total_configs(self):
        return [_config for _section in self.config_sections for _config in self._get_configs(_section)]

    @property
    def names(self):
        return [_cfg.get('site') for _cfg in self.total_configs]

    def specified_config(self, site_name):
        for _config in self.total_configs:
            if _config.get('site', '') == site_name:
                return [_config]
        raise NotExistSiteError("Don't existed this site name: <%s>" % site_name)
