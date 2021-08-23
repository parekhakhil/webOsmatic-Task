from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10, unique=True)
    url = models.URLField(null=True, blank=True)
    country_code = models.CharField(max_length=5)
    email = models.EmailField(max_length=128, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='contacts')

    def __str__(self):
        return f"{self.name} -- {self.mobile}"
