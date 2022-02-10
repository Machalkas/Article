from dataclasses import fields
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['pk','email','password','sub','autor']
    def create(self, data):
        user=User.objects.create_user(email=data['email'], password=data["password"])
        return user