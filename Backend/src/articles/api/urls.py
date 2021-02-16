from django.urls import path
# from .views import ArticleDetailView, ArticleListView, ArticleCreateView, ArticleDeleteView, ArticleUpdateView

from articles.api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='article')
urlpatterns = router.urls

# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('<pk>', ArticleDetailView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
#     path('update/<pk>/', ArticleUpdateView.as_view()),
#     path('delete/<pk>/', ArticleDeleteView.as_view()),
# ]
