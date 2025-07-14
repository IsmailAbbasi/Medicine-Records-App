import uuid
from django.db.models.signals import pre_save
from django.conf import settings
def random_username(sender, instance, **kwargs):
        if not instance.username:
            instance.username = uuid.uuid4().hex[:30] 