from django.contrib.auth import password_validation
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not (email and password):
            raise ValueError("The user needs an email and password")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        try:
            password_validation.validate_password(password)
        except ValidationError:
            raise ValueError("Password does not pass validations")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(max_length=200)
    full_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return self.email
