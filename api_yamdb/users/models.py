from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель создания пользователя."""

    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    USER_ROLES = [
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin'),
    ]
    email = models.EmailField(
        max_length=254,
        unique=True,
    )
    bio = models.TextField(
        verbose_name='Биография',
        blank=True,
    )
    role = models.CharField(
        verbose_name='Роль пользователя',
        max_length=10,
        choices=USER_ROLES,
        default='user',
    )
    confirmation_code = models.CharField(
        verbose_name='Токен пользователя',
        max_length=100,
        blank=True,
        null=True,
    )

    @property
    def is_admin(self):
        """Проверка пользователя на наличие прав администратора."""
        return self.role == self.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        """Проверка пользователя на наличие прав модератора."""
        return self.role == self.MODERATOR

    @property
    def is_user(self):
        """Проверка пользователя на наличие стандартных прав."""
        return self.role == self.USER

    class Meta:
        ordering = ('username',)

        def __str__(self):
            return self.username
