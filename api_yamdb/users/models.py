from smtplib import SMTPException

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models

from .exceptions import SendMailProblem


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Никнейм пользователя (обязательно):'
    )
    password = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Пароль'
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name='Адрес электронной почты (обязательно):'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Информация о пользователе'
    )
    role = models.CharField(
        max_length=150,
        blank=True,
        choices=(
            (USER, 'Пользователь'),
            (MODERATOR, 'Модератор'),
            (ADMIN, 'Администратор'),
        ),
        default='user',
        verbose_name='Право управления'
    )
    mail_confirmation_code = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Код подтверждеиня адреса электронной почты'
    )

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=('username', 'email'), name='unique_following')]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_staff or self.is_superuser or self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    def send_mail(self):
        try:
            send_mail('Confirm your email address',
                      f'Ваш код подтверждения: {self.mail_confirmation_code}',
                      'no-reply@yamdb.project',
                      (self.email, ))
        except SMTPException:
            raise SendMailProblem('Ошибка отправки письма с подтверждением')
