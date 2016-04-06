# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import os.path
import hashlib
from random import sample
from string import letters, digits
from multiprocessing import Lock

from ._types import RegexType, NoneType, IntType
from ._types import LongType, FloatType, BooleanType, StringTypes

lock = Lock()


def populate_md5(value):
    if not isinstance(value, basestring):
        raise ValueError('md5 must string!')
    m = hashlib.md5()
    try:
        m.update(value)
    except UnicodeEncodeError:
        m.update(value.encode('u8'))
    return m.hexdigest()


def get_spider_conf_key(base_url, site_name):
    return populate_md5(base_url + site_name)


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


def converter(query):
    args_query = query if isinstance(query, (tuple, list)) else (query, )
    convert = (lambda _css, _subcss_or_index=0, _index=0: (_css, _subcss_or_index, _index))
    main_css, sub_css, index = convert(*args_query)
    return main_css, sub_css or 0, index or 0


def recognise_chz(string):
    chz_chars = []
    chz_regex = re.compile(r'[\u4e00-\u9fbf]', re.S)
    letters_regex = re.compile(r'[0-9A-Za-z]', re.S)

    for char in string:
        if chz_regex.search(char) or letters_regex.search(char):
            chz_chars.append(char)
    return ''.join(chz_chars)


def is_exist_path(file_or_dir_path):
    if os.path.basename(file_or_dir_path):
        file_path = os.path.dirname(file_or_dir_path)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
    else:
        if not os.path.exists(file_or_dir_path):
            os.makedirs(file_or_dir_path)


def write(dir_path, filename, lines, uri=None, repl=u'\n'):
    is_exist_path(dir_path)
    base_path = [dir_path, filename, '_']

    if uri is not None:
        suffix = [populate_md5(uri)]
    else:
        suffix = sample(letters, 8) + sample(digits, 6)
    abs_filename = ''.join(base_path + suffix + ['.txt'])

    with lock:
        with open(abs_filename, 'w') as fp:
            try:
                if isinstance(lines, (tuple, list)):
                    lines_seq = repl.join(lines).encode('u8')
                else:
                    lines_seq = lines
                fp.writelines(lines_seq)
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass

