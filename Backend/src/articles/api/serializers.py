from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # this field attributes should be same as the model attribute
        fields = ('id', 'title', 'content')
