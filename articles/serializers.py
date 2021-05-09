from rest_framework.serializers import ModelSerializer

from articles.models import Document


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class AuthorsListSerializer(ModelSerializer):
    class Meta:
        model = Document
        fields = ('authors',)
