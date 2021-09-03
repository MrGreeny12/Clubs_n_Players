import django_filters
from .models import Club, Player


class ClubFilter(django_filters.FilterSet):
    '''
    Фильтрует по стране клуба.
    '''

    class Meta:
        model = Club
        fields = {
            'country': ['exact'],
        }


class PlayerFilter(django_filters.FilterSet):
    '''
    Фильтрует по клубу и по гражданству игрока.
    '''

    class Meta:
        model = Player
        fields = {
            'citizenship': ['exact'],
            'club': ['exact'],
        }