from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .managers import UserManager

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия пользователя')
    phone = PhoneNumberField(verbose_name='телефон для связи', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='электронная почта пользователя ')
    image = models.ImageField(upload_to='users/avatars', verbose_name='аватарка пользователя', **NULLABLE)
    role = models.CharField(max_length=50, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
