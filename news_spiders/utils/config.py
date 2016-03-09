import re
import os.path
from ConfigParser import ConfigParser as _ConfigParser

from ..exceptions import NotExistFileError


class Base(object):
    def __init__(self, namespace):
        for attr, value in namespace.iteritems():
            setattr(self, attr.lower(), value)

    def __getattr__(self, attr):
        if attr in self.__dict__:
            return self.__dict__[attr]

    def __setattr__(self, attr, value):
        self.__dict__[attr] = value


class ConfigAttribute(object):
    """ The class suit to every special site configs """
    def __init__(self, site_configs):
        # Must notice to use `copy.deepcopy` that void to modify site_configs variable
        self.__urls = self._copy(site_configs.get('urls', []))
        self.__other = self._copy({k: v for k, v in site_configs.iteritems() if k != 'urls'})

    def _copy(self, obj):
        if isinstance(obj, dict):
            new_obj = {}
            for _key, _value in obj.iteritems():
                new_obj[_key] = self._copy(_value)

        elif isinstance(obj, list):
            new_obj = []
            for _sub in obj:
                new_obj.append(self._copy(_sub))

        elif isinstance(obj, tuple):
            new_obj = ()
            for _tup in obj:
                new_obj += (self._copy(_tup),)
        elif isinstance(obj, (basestring, int, long, float, bool, type(None), type(re.compile(r'')))):
            return obj
        else:
            raise
        return new_obj

    @property
    def length_urls(self):
        return len(self.__urls)

    def master(self, index):
        # Deal with which branch pages configs
        branch_url_cfg = self.__urls[index]
        branch_url_cfg.setdefault('start', 1)
        branch_url_cfg.setdefault('site', self.__other['site'])
        branch_url_cfg['pages'] = branch_url_cfg.get('pages') + 1

        master_namespace = self.__other
        branch_namespace = branch_url_cfg

        # Deal with all urls configs of which branch page as master
        extra_extend = {
            'branch': ['cate', 'page_url'],
            'master': {
                'json': False, 'sleep': False, 'multi_page': None,
                'platform': 'pc', 'remove_tags': None, 'is_script': True
            }
        }

        for which, values in extra_extend.iteritems():
            for key in values:
                if which == 'branch':
                    branch_value = branch_namespace[key]
                    master_namespace[key] = branch_value
                else:
                    master_value = master_namespace.get(key, values[key])
                    master_namespace.setdefault(key, master_value)

        master = Base(master_namespace)
        master.branch = Base(branch_namespace)
        return master


class BaseConfigParser(_ConfigParser):
    def __init__(self, absolute_config_path, *args, **kwargs):
        if not os.path.exists(absolute_config_path):
            raise NotExistFileError("Don't exist this file: <%s>" % absolute_config_path)
        _ConfigParser.__init__(self, *args, **kwargs)

        self.absolute_config_path = absolute_config_path
        self.read(self.absolute_config_path)

    def get_sections(self):
        return self.sections()

    def get_options(self, section):
        return self.options(section=section)

    def get_option_value(self, section, option):
        return self.get(section=section, option=option)

    def get_option_list(self, section, option):
        options = self.get_option_value(section, option)
        return [_option.strip() for _option in options.split(',')]


