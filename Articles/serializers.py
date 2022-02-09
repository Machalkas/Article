from dataclasses import fields
from traceback import print_tb
from rest_framework import serializers
from .models import Article

class ArticlesSerializer(serializers.ModelSerializer):
    autor_name=serializers.SerializerMethodField(method_name="autorName")
    short_text=serializers.SerializerMethodField(method_name="textCutter")
    class Meta:
        model=Article
        exclude=["text"]
    
    def autorName(self, obj):
        return obj.autor.first_name+" "+obj.autor.last_name
    def textCutter(self, obj):
        return obj.text[:300]

class ArticleSerializer(serializers.ModelSerializer):
    autor_name=serializers.SerializerMethodField(method_name="autorName")
    class Meta:
        model=Article
        fields="__all__"
    
    # def create(self, valid_data):
    #     return Article.objects.create(**valid_data)
    
    # def update(self, instance, valid_data):
    #     print("update")
    #     instance.title=valid_data.get('title', instance.title)
    #     instance.text=valid_data.get('text', instance.text)
    #     instance.save()
    #     return instance

    def autorName(self, obj):
        return obj.autor.first_name+" "+obj.autor.last_name

class EditArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=["title","text", "onlysub"]
