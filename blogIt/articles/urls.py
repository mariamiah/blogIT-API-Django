from django.urls import path, include
from .views import (
    ArticleDetail,
    ArticleList
)
from .models import Article


urlpatterns = [
    path('', ArticleList.as_view()),
    path('<int:pk>/', ArticleDetail.as_view()),
]
