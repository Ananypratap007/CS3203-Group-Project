from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    pfp = models.ImageField(upload_to ='uploads/')
    username = models.CharField(max_length = 200)
    email = models.EmailField(_("email address"), primary_key = True)
    dob = models.DateTimeField(default=timezone.now)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
