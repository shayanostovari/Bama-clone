from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.hashers import make_password
from lib.base_model import BaseModel


class User(AbstractUser, BaseModel):
    """
    Abstract user contains these fields:
    1- username: The username of the user
    2- password: The password of the user
    3- email: The email address of the user
    4- first_name: The first name of the user
    5- last_name: The last name of the user
    """
    phone_number = models.CharField(verbose_name=_('phone number'), max_length=12, blank=True)

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

    objects = UserManager()
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
