from django.db import models
COUNTRY = [
    ('FR', 'France'),
    ('RU', 'Russia'),
    ('US', 'USA'),
    ('UK', 'United Kingdom'),
    ('RO', 'Romania'),
]


class Club(models.Model):
    '''
    Модель футбольного клуба
    '''
    title = models.CharField(max_length=255, verbose_name='Название клуба')
    country = models.CharField(max_length=50, choices=COUNTRY, verbose_name='Страна клуба')

    def __str__(self):
        return self.title


class Player(models.Model):
    '''
    Модель игрока
    '''
    first_name = models.CharField(max_length=128, verbose_name='Имя')
    last_name = models.CharField(max_length=128, verbose_name='Фамилия')
    citizenship = models.CharField(max_length=50, choices=COUNTRY, verbose_name='Гражданство')
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
        verbose_name='Клуб',
        related_name='players'
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
