from django.urls import path, include
from .views import (
    ArticleDetail,
    ArticleList
)
from .models import Article

app_name = 'articles'

urlpatterns = [
    path('', ArticleList.as_view()),
    path('<slug>/', ArticleDetail.as_view(), name="articles-detail"),
]
