from importlib import import_module
from ConfigParser import NoSectionError

from .genconf import module_path
from ..exceptions import NotExistSiteError
from ..utils.config import BaseConfigParser as _BaseConfig


class InitConfigs(_BaseConfig):
    """ This class mainly make configs to *.py file, not static to load configs """
    module_option = 'module_name'
    specified_section = 'specific'

    def __init__(self):
        _BaseConfig.__init__(self, module_path)

    def _get_module(self, section, package=None):
        if not self.is_valid(section):
            raise NoSectionError("Don't existed <%s> section in <%s> file" % (section, self.absolute_config_path))

        module_name = self.get_option_value(section, self.module_option)
        module = import_module(name=module_name, package=package)
        return module

    def _get_configs(self, conf_name, package=None):
        module = self._get_module(section=conf_name, package=package)
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

    @property
    def settings(self):
        module = self._get_module('news_settings')
        return {attr: getattr(module, attr) for attr in dir(module) if attr[0].isupper()}
