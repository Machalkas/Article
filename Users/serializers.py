from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['pk','email','password','first_name','last_name','sub','autor']
        
    def validate(self, data):
        password_validation.validate_password(password=data["password"], user=User)
        return data

    def create(self, data):
        user=User.objects.create(email=data['email'], password=make_password(data["password"]), first_name=data.get('first_name',''), last_name=data.get('last_name',''))
        return user

class UserPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["sub", "autor", "is_superuser"]