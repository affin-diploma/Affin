import json

from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from articles.models import Document
from articles.serializers import DocumentSerializer, AuthorsListSerializer


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class AuthorsListViewSet(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = AuthorsListSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ['authors']
    search_fields = ['authors']


class AutocompleteAuthors(APIView):
    def get(self, request):
        term = request.GET.get('term')
        authors_list = list()
        if 'term' in request.GET:
            qs = Document.objects.filter(authors__icontains=term)[:20]
            for authors in qs:
                for author in authors.authors:
                    if term in author:
                        if author not in authors_list:
                            authors_list.append(author)

        else:
            qs = Document.objects.all()[:20]
            for authors in qs:
                for author in authors.authors:
                    if author not in authors_list:
                        authors_list.append(author)

        result = {"authors": authors_list[:20]}
        return JsonResponse(result, safe=False)


class AutocompletePublishers(APIView):
    def get(self, request):
        term = request.GET.get('term')
        publishers_list = list()
        if 'term' in request.GET:
            qs = Document.objects.filter(publisher__icontains=term)[:20]
            for publisher in qs:
                if publisher.publisher not in publishers_list:
                    publishers_list.append(publisher.publisher)

        else:
            qs = Document.objects.all()[:20]
            for publisher in qs:
                if publisher.publisher not in publishers_list:
                    publishers_list.append(publisher.publisher)

        result = {"publishers": publishers_list[:20]}
        return JsonResponse(result, safe=False)
