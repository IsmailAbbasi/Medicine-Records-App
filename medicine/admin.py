from django.contrib import admin
from .models import Medicine

# Register your models here.
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('medicine', 'stock', 'created_at', 'updated_at', 'user')
    search_fields = ('medicine',)
    list_filter = ('created_at', 'updated_at')

admin.site.register(Medicine, MedicineAdmin)