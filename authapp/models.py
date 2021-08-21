from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class GenderChoice(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    OTHER = "other", _("Other")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, unique=True)
    full_name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    social_media = models.URLField(null=True, blank=True)
    gender = models.CharField(choices=GenderChoice.choices, max_length=15)

    def __str__(self):
        return f"{self.user.username}'s profile"
