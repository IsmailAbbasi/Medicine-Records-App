from django.db import models

class Medicine(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='medicines')
    medicine = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine} (Stock {str(self.stock)})"
