from importlib.resources import Resource
from re import sub
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import ArticlesSerializer, ArticleSerializer
from .models import Article
from Articles import serializers

class ArticlesViewSet(APIView):
    def get(self, request):
        if request.user.is_authenticated and request.user.sub==True:
            articles=Article.objects.all()
        else:
            articles=Article.objects.filter(onlysub=False)
        serializer=ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleViewSet(APIView):
    def get(self, request,id):
        try:
            article=Article.objects.get(pk=id)
        except:
            return Response(data={"error":"article %s not found"%id}, status=404)
        if request.user.is_authenticated and request.user.sub==True or article.onlysub==False:
            pass
        else:
            return Response(data={"error":"not enough permissions"}, status=403)
        serializer=ArticleSerializer(article, many=False)
        return Response(serializer.data)


    
