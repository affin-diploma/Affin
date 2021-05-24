import pickle

import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from articles.models import Document
from general_api_module.models import DataSource


class PullArticlesListView(APIView):

    def post(self, request):
        data_sources = DataSource.objects.all()
        articles = dict()
        articles["status"] = "ERROR"
        articles["total"] = 0
        articles["data"] = []
        for ds in data_sources:
            req = requests.post(
                url=ds.api,
                json=request.data
            )

            result = req.json()
            if articles["status"] == "ERROR":
                if result["status"] == "OK":
                    articles["status"] = result["status"]

            if result['data']:
                articles["data"] += result["data"]
                articles["total"] += result["total"]

                qs = Document.objects.values_list('downloadUrl')
                local_articles = Document.objects.all()
                local_articles.query = pickle.loads(pickle.dumps(qs.query))
                local_articles = [loc_article['downloadUrl'] for loc_article in local_articles]

                for article in articles.get('data'):
                    if article['downloadUrl'] in local_articles:
                        pass
                    else:
                        Document.objects.create(downloadUrl=article['downloadUrl'],
                                                doi=article['doi'],
                                                title=article['title'],
                                                description=article['description'],
                                                lang=article['lang'],
                                                topics=article['topics'],
                                                authors=article['authors'],
                                                publisher=article['publisher'],
                                                year=article['year'],
                                                relations=article['relations']
                                                )


        return Response(data=articles)
