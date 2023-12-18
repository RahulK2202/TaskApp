# serializers.py
from rest_framework import serializers
from .models import AppUsers

class AppUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            
        }

    def create(self, validated_data):
        
        password = validated_data.pop('password', None)
        user = AppUsers.objects.create(**validated_data)
        if password:
            user.set_password(password)
        user.is_active = False
        user.save()
        return user

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
       