from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticlesSerializer, ArticleSerializer, EditArticleSerializer
from .models import Article

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
        if not request.user.is_authenticated or request.user!=article.autor or request.user.autor==False:
            return Response(status=403)
        serializer=EditArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)

    def delete(self, request, id):#удаление статьи
        try:
            article=Article.objects.get(pk=id)
        except:
            return Response(data={"error":"article %s not found"%id}, status=404)
        if not request.user.is_authenticated or request.user!=article.autor or request.user.autor==False:
            return Response(status=403)
        article.delete()
        return Response(status=200)


class CreateArticleView(APIView):
    def post(self, request):#создание статьи
        if not request.user.is_authenticated or request.user.autor==False:
            return Response(status=403)
        serializer=EditArticleSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(autor=request.user)
            except:
                return Response(data={"error":"You already have article with the same title"}, status=400)
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=400)

