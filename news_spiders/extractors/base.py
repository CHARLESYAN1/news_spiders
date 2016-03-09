from ..utils import IntType, StringTypes


class BaseMarks(object):
    def __init__(self, config):
        self.__config = config
        self.__default_details = 'details'

    def __getattr__(self, name):
        name = 'marks_' + name
        namespace = [attr for attr in dir(self.__class__) if not attr.startswith('_')]

        if name not in namespace:
            raise AttributeError('<%s> class not existed attribute: <%s>' % (self.__class__.__name__, name))
        return getattr(self, name)

    @property
    def marks_title(self):
        return self.__config[self.__default_details]['pyq_title']

    def __date_auth(self):
        default_date_auth = 'pyq_date_author'
        default_auth_date = 'pyq_author_date'
        default_conf = self.__config[self.__default_details]

        if default_date_auth in default_conf:
            reverse = False
            conf = default_conf[default_date_auth]
        elif default_auth_date in default_conf:
            reverse = True
            conf = default_conf[default_auth_date]
        else:
            raise KeyError("Not existed key about date and auth in <%s> site" % self.__config['site'])
        return conf['date'], conf['auth'], reverse

    marks_date = property(lambda self: self.__date_auth()[0])
    marks_auth = property(lambda self: self.__date_auth()[1])
    marks_reverse = property(lambda self: self.__date_auth()[2])

    @property
    def marks_text(self):
        return self.__config[self.__default_details]['pyq_content']

    @property
    def marks_removal(self):
        return self.__config.get('remove_tags', ())

    @property
    def marks_multipage(self):
        return self.__config.get('multi_page', ())


class ResponseProcessor(object):
    def __init__(self, selector):
        self._selector = selector
        self._context = self._selector.response.body_as_unicode()

    def remove_script_style(self):
        pass


class BaseExtractors(ResponseProcessor):
    def __init__(self, selector):
        super(BaseExtractors, self).__init__(selector)

    def extract_with_regex(self, regex):
        """
        mainly to extract title, content, date, auth by selector, and result is text or html
        :param regex: RegexType, to match content what you want to
        """
        extractors = regex.findall(self._context)

        try:
            if extractors:
                return extractors[0]
        except (IndexError, ValueError, AttributeError):
            pass
        return u''

    def extract_with_selector(self, query, with_tags=False):
        """
        mainly to extract title, content, date, auth by selector, and result is text or html
        :param query: string|tuple, here there situation:
            (1): string, directly extract
            (2): tuple of two items consist tuple, like as ((css, index), ...), extract title
            (3): tuple of three items consist tuple, like as ((css, sub_css, index), (css, None, index), ...)
        :param with_tags: bool, if True, return value include html tags, else return text
        """
        converter = (
            lambda _css, _subcss_or_index=0, _index=0: (_css, _subcss_or_index, _index)
        )

        args_query = query if isinstance(query, (tuple, list)) else (query, )
        main_css, subcss_or_index, index = converter(*args_query)
        main_extractors = self._selector.css(main_css)

        try:
            if isinstance(subcss_or_index, IntType):
                # Only have main_css as parameter to extract, like as (css1, css2, ...)
                if not with_tags:
                    text = main_extractors[0].xpath('.//text()').extract()
                else:
                    text = main_extractors[0].extract()
            elif isinstance(subcss_or_index, StringTypes):
                # `subcss_or_index` is css selector, go on extract by it
                sub_extractors = main_extractors.css(subcss_or_index)
                if not with_tags:
                    text = sub_extractors[index].xpath('.//text()').extract()
                else:
                    text = sub_extractors[index].extract()
            else:
                err_css = subcss_or_index
                raise TypeError('Sub css selector <{}:{}> not expectation type'.format(type(err_css), err_css))

            return u''.join(text)
        except (IndexError, ValueError, AttributeError):
            pass
        return u''
