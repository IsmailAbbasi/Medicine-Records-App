from django.apps import AppConfig
from django.core.signals import request_finished
from . import signals

class MedicineConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'medicine'

    def ready(self):
        request_finished.connect(signals.random_username)
