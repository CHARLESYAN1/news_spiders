from importlib import import_module

from ..exceptions import NotExistSiteError
from ..settings import news_settings as _settings


class InitConfigs(object):
    """ This class mainly make configs to *.py file, not static to load configs """
    def __init__(self):
        self._settings = {
            attr: getattr(_settings, attr)
            for attr in dir(_settings) if attr[0].isupper()
            }
        self._config_modules = [key for key in self._settings if 'CONFIGS_MODULE' in key]
        self._specified = [spc.strip() for spc in self._settings['SPECIFIC_CONFIGS'].split(',')]

    def _get_configs(self, name, package=None):
        if not self.is_valid(name):
            raise AttributeError("Don't attribute <%s> in <%s> file" % (name, _settings.__name__))

        module_name = self._settings[name]
        module = import_module(name=module_name, package=package)
        return getattr(module, name[:len(name) - len('_MODULE')], [])

    def is_valid(self, name):
        return name in self._settings

    @property
    def hot_configs(self):
        config_name = 'HOT_CONFIGS_MODULE'
        return self._get_configs(config_name)

    @property
    def amazon_configs(self):
        config_name = 'AMAZON_CONFIGS_MODULE'
        return self._get_configs(config_name)

    @property
    def security_configs(self):
        config_name = 'SECURITY_CONFIGS_MODULE'
        return self._get_configs(config_name)

    @property
    def most_configs(self):
        most_configs = [_name for _name in self._config_modules if _name not in self._specified]
        return [_config for _name in most_configs for _config in self._get_configs(_name)]

    @property
    def total_configs(self):
        return [_config for _name in self._config_modules for _config in self._get_configs(_name)]

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
        return self._settings

news_config = InitConfigs()
