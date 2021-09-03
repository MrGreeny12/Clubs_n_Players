from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from club.filters import ClubFilter, PlayerFilter
from club.models import Club, Player
from club.permissions import IsManagerOrAdminOrReadOnly, IsPresidentOrAdminOrReadOnly
from club.serializers import ClubsListSerializer, PlayersDetailSerializer, PlayersListSerializer, ClubDetailSerializer


class PlayerCreateView(generics.CreateAPIView):
    '''
    Создаёт игрока. Доступ только у администратора и менеджера
    '''
    serializer_class = PlayersDetailSerializer
    queryset = User.objects.none()
    permission_classes = (IsManagerOrAdminOrReadOnly,)


class PlayerDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Редактирует и удаляет данные игрока. Доступ только у администратора и менеджера
    '''
    serializer_class = PlayersDetailSerializer
    queryset = Player.objects.all()
    permission_classes = (IsManagerOrAdminOrReadOnly,)


class PlayerListView(generics.ListAPIView):
    '''
    Передаёт список игроков в формате:
    {
        "id"
        "first_name"
        "last_name"
        "citizenship"
        "club"
    }
    '''
    serializer_class = PlayersListSerializer
    queryset = Player.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PlayerFilter


class ClubCreateView(generics.CreateAPIView):
    '''
    Создаёт клуб. Доступ только у администратора и президента
    '''
    serializer_class = ClubDetailSerializer
    permission_classes = (IsPresidentOrAdminOrReadOnly, )


class ClubDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Редактирует и удаляет данные клуба. Доступ только у администратора и президента
    '''
    serializer_class = ClubDetailSerializer
    queryset = Club.objects.all()
    permission_classes = (IsPresidentOrAdminOrReadOnly, )


class ClubListView(generics.ListAPIView):
    '''
    Передаёт список клубов в формате:
    {
        "id"
        "title"
        "country"
    }
    '''
    serializer_class = ClubsListSerializer
    queryset = Club.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ClubFilter