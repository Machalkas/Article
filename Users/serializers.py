from rest_framework import serializers
from .models import User
from django.contrib.auth import password_validation

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['pk','email','password','sub','autor']
        
    def validate(self, data):
        password_validation.validate_password(password=data["password"], user=User)
        return data

    def create(self, data):
        user=User.objects.create_user(email=data['email'], password=data["password"])
        return user