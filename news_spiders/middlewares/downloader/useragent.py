import random

from .base import USER_AGENT as _user_agent


class NewsUserAgentMiddleware(object):
    def __init__(self):
        self.user_agent = _user_agent

    def process_request(self, request, spider):
        user_agent = random.choice(self.user_agent)

        if user_agent:
            request.headers.setdefault('User-Agent', user_agent)
