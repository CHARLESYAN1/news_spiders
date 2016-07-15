# -*- coding: utf-8 -*-
from .. import app, logger
from .base import BaseSched
from news_spiders.exceptions import get_exce_info


def dispatch_weixin_jobs():
    bs = BaseSched()

    if bs.is_migrate is None:
        return

    try:
        for _site_name in bs.weixin_sites:
            beat = _site_name.get('beat', {})
            kwargs_func = {'site_name': _site_name['site']}
            app.add_job(bs.schedule, kwargs=kwargs_func, **beat)
    except Exception:
        logger.info(logger.exec_msg.format(msg='Dispatch weixin jobs error', exec_info=get_exce_info()))

dispatch_weixin_jobs()
