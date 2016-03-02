import socket
from importlib import import_module

from .genconf import aws_path, sched_path


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


class InitializationConfigs(object):
    """ This class mainly make configs to *.py file, not static to load configs """

    @staticmethod
    def _get_configs(conf_name, module_name, package=None):
        module = import_module(name=module_name, package=package)
        return getattr(module, conf_name, [])

    def get_hot_configs(self):
        conf_name = 'HOT_CONFIGS'
        module_name = 'conf.pyconf.chot'
        return self._get_configs(conf_name, module_name)

    def get_full_configs(self):
        conf_name = 'FULL_CONFIGS'
        module_name = 'conf.pyconf.cfull'
        return self._get_configs(conf_name, module_name)

    def get_fund_configs(self):
        conf_name = 'FUND_CONFIGS'
        module_name = 'conf.pyconf.cfund'
        return self._get_configs(conf_name, module_name)

    def get_hk_configs(self):
        conf_name = 'HK_CONFIGS'
        module_name = 'conf.pyconf.chk'
        return self._get_configs(conf_name, module_name)

    def get_hif_configs(self):
        conf_name = 'HIF_CONFIGS'
        module_name = 'conf.pyconf.chif'
        return self._get_configs(conf_name, module_name)

    def get_sanban_configs(self):
        conf_name = 'SANBAN_CONFIGS'
        module_name = 'conf.pyconf.csanban'
        return self._get_configs(conf_name, module_name)

    def get_usa_configs(self):
        conf_name = 'USA_CONFIGS'
        module_name = 'conf.pyconf.cusa'
        return self._get_configs(conf_name, module_name)

    def get_amazon_configs(self):
        conf_name = 'AMAZON_CONFIGS'
        module_name = 'conf.pyconf.camazon'
        return self._get_configs(conf_name, module_name)
