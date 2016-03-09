# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from ._types import RegexType, NoneType, IntType
from ._types import LongType, FloatType, BooleanType, StringTypes


def populate_md5(value):
    if not isinstance(value, basestring):
        raise ValueError('md5 must string!')
    m = hashlib.md5()
    try:
        m.update(value)
    except UnicodeEncodeError:
        m.update(value.encode('u8'))
    return m.hexdigest()


def deepcopy(obj):
    if isinstance(obj, dict):
        new_obj = {}
        for _key, _value in obj.iteritems():
            new_obj[_key] = deepcopy(_value)

    elif isinstance(obj, list):
        new_obj = []
        for _sub in obj:
            new_obj.append(deepcopy(_sub))

    elif isinstance(obj, tuple):
        new_obj = ()
        for _tup in obj:
            new_obj += (deepcopy(_tup),)
    elif isinstance(obj, (StringTypes, IntType, LongType, FloatType, BooleanType, NoneType, RegexType)):
        return obj
    else:
        raise
    return new_obj


