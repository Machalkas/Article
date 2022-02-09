from importlib.resources import Resource
from re import sub
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ArticlesSerializer, ArticleSerializer, EditArticleSerializer
from .models import Article
from Articles import serializers

class ArticlesView(APIView):
    def get(self, request):#список статей
        if request.user.is_authenticated and request.user.sub==True:
            articles=Article.objects.all()
        else:
            articles=Article.objects.filter(onlysub=False)#если пользователь не подписчик, то выводятся только статьи с параметром onlysub=False
        serializer=ArticlesSerializer(articles, many=True)
        return Response(serializer.data)

class ArticleView(APIView):
    def get(self, request,id):#чтение статьи
        try:
            article=Article.objects.get(pk=id)
        except:
            return Response(data={"error":"article %s not found"%id}, status=404)
        if article.onlysub:
            if not request.user.is_authenticated:
                return Response(status=401)
            elif not request.user.sub:
                return Response(status=403)
        serializer=ArticleSerializer(article, many=False)
        return Response(serializer.data)
    def put(self, request, id):#обновление статьи
        try:
            article=Article.objects.get(pk=id)
        except:
            return Response(data={"error":"article %s not found"%id}, status=404)
        if not request.user.is_authenticated or request.user!=article.autor:
            return Response(status=403)
        serializer=EditArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)



    
