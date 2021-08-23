from .serializers import AllContactSerializer,ContactSerializer
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
from django.contrib.auth.models import User
# Create your views here.


class ContactCreateView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    authentication_classes = [SessionAuthentication]

    def post(self, request):
        if not request.POST._mutable:
            request.POST._mutable
        data = request.data
        data['user'] = request._user
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
    serializer_class = AllContactSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_queryset(self):
        qs = User.objects.filter(id=self.request.user.id)
        return qs
