from django.contrib import admin
from .models import Agv

class AgvAdmin(admin.ModelAdmin):
    list_display = ('verhicle_id', 'verhicle_model', 'guidance','is_connected','is_active')

# Register your models here.

admin.site.register(Agv, AgvAdmin)