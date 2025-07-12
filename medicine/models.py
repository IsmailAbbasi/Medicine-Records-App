from django.db import models

class Medicine(models.Model):
    medicine = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=1)
