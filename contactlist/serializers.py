from .models import Contact
from rest_framework import serializers
from django.contrib.auth.models import User
from authapp.serializers import UserSerializer


class ContactSerializer(serializers.ModelSerializer):
    # user_id = serializers.PrimaryKeyRelatedField(
    #     write_only=True, source="user", queryset=User.objects.all()
    # )
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = [
            "id",
            "mobile",
            "name",
            "email",
            "country_code",
            # "user_id",
            "user",
            "url",
        ]

class AllContactSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['id','email','username','contacts']
