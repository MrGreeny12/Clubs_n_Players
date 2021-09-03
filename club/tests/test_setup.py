from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from club.models import Club, Player


class TestSetup(APITestCase):

    def setUp(self):
        self.club_list_api_url = reverse('club_list_api_url')
        user = User.objects.create_user(
            username='username',
            password='password',
            is_staff=True,
            is_superuser=True,
        )
        user.save()
        self.club = Club.objects.create(
            title='Тестовый клуб',
            country='RU'
        )
        self.club.save()
        player = Player.objects.create(
            first_name='Петя',
            last_name='Иванов',
            citizenship='RU',
            club=club,
        )
        player.save()

        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()