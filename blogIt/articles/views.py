from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
class ArticleList(APIView):
    """
    List all articles or create a new article
    """
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer_context = {
            'request': request
        }
        serializer = ArticleSerializer(articles, many=True, context=serializer_context)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer_context = {
            'request': request
        }
        serializer = ArticleSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    """
    Retrieve, Update and Delete an article instance
    """
    def get_object(self, slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
    
    def get(self, request, slug, format=None):
        article = self.get_object(slug)
        serializer_context = {
            'request': request
        }
        serializer = ArticleSerializer(article, context=serializer_context)
        return Response(serializer.data)
    
    def put(self, request, slug, format=None):
        article = self.get_object(slug)
        serializer_context = {
            'request': request
        }
        serializer = ArticleSerializer(article, data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, slug, format=None):
        article = self.get_object(slug)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
