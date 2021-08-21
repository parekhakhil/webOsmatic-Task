from django.db.models import fields
from authapp.models import UserProfile
from django.db import models
from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email", "first_name", "last_name")
        write_only_fields = ("password",)
        read_only_fields = ("id",)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        user.set_password(validated_data["password"])
        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "mobile",
            "description",
            "full_name",
            "social_media",
            "gender",
            "user",
        ]
