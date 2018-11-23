from __future__ import absolute_import
from RedScarf import celery_app
import time


@celery_app.task()
def add(x, y):
    time.sleep(3)
    return x + y


@celery_app.task()
def mul(x, y):
    time.sleep(3)
    return x * y


@celery_app.task()
def xsum(numbers):
    time.sleep(3)
    return sum(numbers)
