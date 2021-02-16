# from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from articles.models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# class ArticleListView(ListAPIView):
#     """
#     Used for read-only endpoints to represent a collection of model instances.
#     Provides a get method handler.
#     Extends: GenericAPIView, ListModelMixin
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDetailView(RetrieveAPIView):
#     """
#     Used for read-only endpoints to represent a single model instance.
#     Provides a get method handler.
#     Extends: GenericAPIView, RetrieveModelMixin
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleCreateView(CreateAPIView):
#     """
#     Used for read-only endpoints to represent a single model instance.
#     Provides a get method handler.
#     Extends: GenericAPIView, RetrieveModelMixin
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleUpdateView(UpdateAPIView):
#     """
#     Used for read-only endpoints to represent a single model instance.
#     Provides a get method handler.
#     Extends: GenericAPIView, RetrieveModelMixin
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleDeleteView(DestroyAPIView):
#     """
#     Used for read-only endpoints to represent a single model instance.
#     Provides a get method handler.
#     Extends: GenericAPIView, RetrieveModelMixin
#     """
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
