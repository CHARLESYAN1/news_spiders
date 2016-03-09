from scrapy.link import Link as _Link
from scrapy.spiders import Rule as _Rule


class ProcessorLinks(object):
    @staticmethod
    def process_links(links):
        # new_links = []
        #
        # for _link in links or []:
        #     pass
        return links

    @staticmethod
    def process_request(request):
        print request.meta['link_text']
        return request


class NewsRule(_Rule):
    processor_links_class = ProcessorLinks

    def __init__(self, link_extractor, callback, **kwargs):
        super(NewsRule, self).__init__(
            link_extractor=link_extractor,
            callback=callback,
            process_links=self.processor_links_class.process_links,
            process_request=self.processor_links_class.process_request,
            **kwargs
        )

