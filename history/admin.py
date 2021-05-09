from django.contrib import admin
from django.contrib.admin import ModelAdmin

from history.models import SearchHistory


@admin.register(SearchHistory)
class SearchHistoryAdmin(ModelAdmin):
    pass