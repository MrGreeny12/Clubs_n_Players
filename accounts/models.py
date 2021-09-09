from django.contrib.auth.models import User
from django.db import models
ROLE = [
    ('PR', 'President'),
    ('MN', 'Manager'),
]


class Profile(models.Model):
    '''
    Модель профиля пользователя
    '''
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    role = models.CharField(max_length=50, choices=ROLE, verbose_name='Роль пользователя')

    def __str__(self):
        return self.role