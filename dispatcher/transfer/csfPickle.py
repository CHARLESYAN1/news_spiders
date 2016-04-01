try:
    import cPickle as pickle
except ImportError:
    import pickle as pickle

import os
from datetime import date
from os.path import dirname, abspath, join


class CsfPickle(object):
    default_path = join(dirname(dirname(dirname(abspath(__file__)))), 'pickle/').replace('\\', '/')

    def __init__(self):
        if not os.path.exists(self.default_path):
            os.makedirs(self.default_path)

        self._fpath = self.default_path + '%s_cached.pk' % str(date.today()).replace('-', '')

    def dump(self, obj):
        with open(self._fpath, 'wb') as fp:
            pickle.dump(obj, fp)

    def load(self):
        try:
            with open(self._fpath, 'rb') as fp:
                obj = pickle.load(fp)
            return obj
        except IOError:
            return set()

