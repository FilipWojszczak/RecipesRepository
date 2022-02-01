from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth import urls


class User(AbstractUser):
    email_confirmed = models.BooleanField(default=False)
