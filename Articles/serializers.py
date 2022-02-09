from dataclasses import fields
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
    
    def autorName(self, obj):
        return obj.autor.first_name+" "+obj.autor.last_name

class EditArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields=["title","text"]
