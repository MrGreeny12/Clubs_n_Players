from rest_framework import serializers
from club.models import Club, Player, COUNTRY


class PlayersDetailSerializer(serializers.ModelSerializer):
    """
    Сериалайзер игрока.
    """
    citizenship = serializers.ChoiceField(
        choices=COUNTRY,
    )

    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ('id',)


class PlayersListSerializer(serializers.ModelSerializer):
    """
    Сериалайзер списка игроков.
    """
    class Meta:
        model = Player
        fields = '__all__'


class ClubDetailSerializer(serializers.ModelSerializer):
    """
    Сериалайзер клуба.
    """
    country = serializers.ChoiceField(
        choices=COUNTRY,
    )

    class Meta:
        model = Club
        fields = '__all__'
        read_only_fields = ('id',)


class ClubsListSerializer(serializers.ModelSerializer):
    """
    Сериалайзер списка клубов.
    """
    class Meta:
        model = Club
        fields = ('id', 'title', 'country')
