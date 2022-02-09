from dataclasses import field
from statistics import mode
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
