from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Document(models.Model):
    objects = models.Manager()
    downloadUrl = models.CharField(max_length=2048)
    doi = models.CharField(max_length=2048, null=True)
    title = models.CharField(max_length=256, null=True)
    description = models.CharField(max_length=4096, null=True)
    lang = models.CharField(max_length=28, null=True)
    topics = ArrayField(models.CharField(max_length=128), null=True)
    authors = ArrayField(models.CharField(max_length=128), null=True)
    publisher = models.CharField(max_length=256, null=True)
    year = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    relations = ArrayField(models.CharField(max_length=2048, default=None), null=True)


class Bookmark(models.Model):
    class Meta:
        unique_together = (('user_id', 'document_id'),)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SearchQuery(models.Model):
    searchQuery = models.CharField(max_length=512)
    title = models.CharField(max_length=256, default=None)
    doi = models.CharField(max_length=2048, null=True)
    description = models.CharField(max_length=4096, default=None)
    lang = models.CharField(max_length=28, default=None)
    topics = ArrayField(models.CharField(max_length=128, default=None))
    authors = ArrayField(models.CharField(max_length=128, default=None))
    publisher = models.CharField(max_length=256, default=None)
    published_before = models.IntegerField()
    published_after = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QueriesDocument(models.Model):
    class Meta:
        unique_together = (('query_id', 'document_id'),)

    query_id = models.ForeignKey(SearchQuery, on_delete=models.CASCADE)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


