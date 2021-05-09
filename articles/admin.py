from django.contrib import admin
from django.contrib.admin import ModelAdmin

from articles.models import Document


@admin.register(Document)
class DocumentAdmin(ModelAdmin):
    pass
