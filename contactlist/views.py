from zipapp import create_archive
from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status as httpStatus

# Create your views here.


class ContactCreateView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        if not request.POST._mutable:
            request.POST._mutable
        data = request.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": True,
                    "message": "Contact successfully saved",
                    "data": serializer.data,
                },
                status=httpStatus.HTTP_201_CREATED,
            )
        else:
            return Response({"status": False, "details": serializer.errors})


class ContactDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        qs = Contact.objects.filter(user=self.request._user)
        return qs


class ContactListView(ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        qs = Contact.objects.filter(user__id=self.request.user.id)
        return qs
