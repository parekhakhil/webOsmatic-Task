from .views import ContactCreateView, ContactDetailView, ContactListView
from django.urls import path

app_name = "contact_list"

urlpatterns = [
    path("contact/create", ContactCreateView.as_view()),
    path("contact/<int:pk>", ContactDetailView.as_view()),
    path("contact/all", ContactListView.as_view()),
]
