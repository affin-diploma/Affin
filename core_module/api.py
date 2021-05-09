import requests
from rest_framework.views import APIView
from rest_framework.response import Response


class CoreListView(APIView):

    def post(self, request):

        req = requests.post(
            'https://kka8kksmqf.execute-api.eu-central-1.amazonaws.com/Prod/GetArticlesCore',
            json=request.data
        )
        articles = req.json()

        return Response(data=articles)