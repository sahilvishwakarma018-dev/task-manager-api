from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id","title","description","completed","created_at","updated_at",]
        read_only_fields = ["id", "created_at", "updated_at"]