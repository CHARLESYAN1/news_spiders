from datetime import date

from ..utils import JobBase as _JobBase


class StatisticsBase(object):
    def __init__(self):
        self.base = _JobBase

    @property
    def hot_path(self):
        return self.base.hot_news_path

    @property
    def full_path(self):
        return self.base.full_news_path

    @property
    def default_day(self):
        return str(date.today()).replace('-', '')

    def select_day(self):
        pass


class StatisticsBeforeAnalysis(StatisticsBase):
    def __init__(self):
        super(StatisticsBeforeAnalysis, self).__init__()
        pass


class StatisticsAfterAnalysis(StatisticsBase):
    pass


