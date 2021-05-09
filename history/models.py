from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from articles.models import SearchQuery


class SearchHistory(models.Model):
    class Meta:
        unique_together = (('user_id', 'query_id'),)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    query_id = models.ForeignKey(SearchQuery, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)
