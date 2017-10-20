# coding: utf-8
# celery -A worker worker

from common import app

# 注释这一行, 会导致add失败, sub成功.
# 原因是add没有被加载, sub跟随common被加载
# autodiscover_tasks会搜索foo包(package)下的tasks.py文件里的task, force参数要求eager-load, 默认lazy-load
# http://docs.celeryproject.org/en/latest/reference/celery.html#celery.Celery.autodiscover_tasks
# app.autodiscover_tasks(['foo'], force=True)
app.start()
