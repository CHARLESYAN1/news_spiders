import simplejson
from os.path import abspath as _abs

from . import logger
from .base import Base


class PubSubMigration(Base):
    def __init__(self, *args, **kwargs):
        super(PubSubMigration, self).__init__(*args, **kwargs)

    def subscribe(self, channel_typ):
        messages = []
        channel = self.select_channel(channel_typ)

        pub = self.redis.pubsub()
        pub.subscribe(channel)

        for _message in pub.listen():
            # listen is block, if have not message, which will block here
            try:
                data = _message['data']

                if isinstance(_message, basestring):
                    msg = simplejson.loads(data['data'])

                    if 'exit' in msg:
                        break
                    messages.append(msg)
            except (simplejson.JSONDecodeError, KeyError) as e:
                logger.info('Subscribe message error: redis channel <{}>, type <{}>, msg <{}>, file <{}>'.format(
                    channel, e.__class__, e, _abs(__file__)))
        return messages

    def publish(self, message, channel_typ):
        channel = self.select_channel(channel_typ)
        self.redis.publish(channel, message)

    def select_channel(self, typ):
        """
        Select which Redis channel
        :param typ: int, select which channel
        """
        assert isinstance(typ, int)

        channels = {
            1: self.sgp_hot_channel,
            2: self.sgp_news_channel,
        }

        return channels[typ]
