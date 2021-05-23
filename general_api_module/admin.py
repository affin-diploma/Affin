from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from general_api_module.models import DataSource


@admin.register(DataSource)
class DocumentAdmin(ModelAdmin):
    pass
