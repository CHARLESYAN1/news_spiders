from lxml import etree
from scrapy import Selector as _Slr

from ..utils import IntType, converter


class SlrExtension(_Slr):
    def __init__(self, selector):
        self.__slr = selector
        super(SlrExtension, self).__init__(response=selector.response)

    def clean_node(self, css_query):
        css, subcss_or_index, index = converter(css_query)
        index = subcss_or_index if isinstance(subcss_or_index, IntType) else index

        try:
            xpathev = self._root.xpath
        except AttributeError:
            return self.__slr

        try:
            elements = xpathev(
                _path=self._css2xpath(css),
                namespaces=self.namespaces,
                smart_strings=self._lxml_smart_strings
            )

            if not elements:
                return self.__slr

            if isinstance(subcss_or_index, IntType):
                cleaned_element = elements[subcss_or_index]
            else:
                cleaned_element = elements[0].xpath(
                    _path=self._css2xpath(subcss_or_index),
                    namespaces=self.namespaces,
                    smart_strings=self._lxml_smart_strings
                )[index]

            cleaned_element.clear()
        except (etree.XPathError, IndexError, AttributeError) as e:
            raise ValueError('Css: <{}>, Error: <{}>: <{}>'.format(css, e.__class__, e))

        return _Slr(
            text=etree.tounicode(self._root),
            namespaces=self.namespaces,
            type=self.type
        )

    def test(self, query):
        return self.clean_node(query)
