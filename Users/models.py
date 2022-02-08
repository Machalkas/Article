from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class Manager(UserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Пользователь должен иметь email')
        user=self.model(email=email,)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,  password=None):
        user=self.model(email=email,)
        user.is_staff=True
        user.is_superuser=True
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    sub=models.BooleanField(default=True, blank=False, null=False, verbose_name="Подписчик")
    autor=models.BooleanField(default=False, blank=False, null=False, verbose_name="Автор")
    username = None

    USERNAME_FIELD="email"
    REQUIRED_FIELDS = []
    objects=Manager()
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
