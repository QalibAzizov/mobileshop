
from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mobile_shop.settings")
app = Celery("mobile_shop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind = True)
def debug_task(self):
    print ('Request: {Oir}'.format(self.request))