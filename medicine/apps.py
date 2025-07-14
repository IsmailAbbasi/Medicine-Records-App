from django.apps import AppConfig
from django.core.signals import request_finished
from . import signals
from django.db.models.signals import pre_save
from django.conf import settings

class MedicineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medicine'

    def ready(self):
        # request_finished.connect(signals.random_username)
        pre_save.connect(signals.random_username, sender=settings.AUTH_USER_MODEL)
