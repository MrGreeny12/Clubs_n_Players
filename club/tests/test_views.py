from django.urls import reverse
from club.models import Club, Player
from club.tests.test_setup import TestSetup


class TestViews(TestSetup):

    def test_view_club_list_with_no_auth(self):
        res = self.client.get(reverse('club_list_api_url'))
        self.assertEqual(res.status_code, 200)

    def test_club_create_with_no_auth(self):
        res = self.client.post(reverse('club_create_api_url'))
        self.assertEqual(res.status_code, 403)

    def test_club_create_with_auth(self):
        data = {
            'title': 'Тест_2',
            'country': 'FR'
        }
        self.client.login(username='username', password='password')
        res = self.client.post(reverse('club_create_api_url'), data=data)
        club_2 = Club.objects.get(pk=2)
        self.assertEqual(res.status_code, 301)
        self.assertEqual(data['title'], club_2.title)
        self.assertEqual(data['country'], club_2.country)

    def test_club_update_with_no_auth(self):
        res = self.client.put(reverse('club_detail_api_url'))
        self.assertEqual(res.status_code, 403)

    def test_club_update_with_auth(self):
        data = {
            'id': 1,
            'title': 'Тест',
            'country': 'RU'
        }
        self.client.login(username='username', password='password')
        res = self.client.put(reverse('club_detail_api_url'), data=data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['title'], res.POST.club.title)
        self.assertEqual(data['country'], res.POST.club.title)

    def test_club_delete_with_no_auth(self):
        res = self.client.delete(reverse('club_detail_api_url'))
        self.assertEqual(res.status_code, 403)

    def test_club_delete_with_auth(self):
        self.client.login(username='username', password='password')
        res = self.client.delete(reverse('club_detail_api_url'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Club.objects.all().count(), 0)

    def test_view_player_list_with_no_auth(self):
        res = self.client.get(reverse('player_list_api_url'))
        self.assertEqual(res.status_code, 200)

    def test_player_create_with_no_auth(self):
        res = self.client.post(reverse('player_create_api_url'))
        self.assertEqual(res.status_code, 403)

    def test_player_create_with_auth(self):
        data = {
            'first_name': 'Имя_2',
            'last_name': 'Фамилия_2',
            'citizenship': 'FR',
            'club': self.club,
        }
        self.client.login(username='username', password='password')
        res = self.client.post(reverse('player_create_api_url'), data=data)
        player_2 = Player.objects.get(pk=2)
        self.assertEqual(res.status_code, 301)
        self.assertEqual(data['first_name'], player_2.first_name)
        self.assertEqual(data['last_name'], player_2.last_name)
        self.assertEqual(data['citizenship'], player_2.citizenship)
        self.assertEqual(data['club'], player_2.club)

    def test_player_update_with_no_auth(self):
        res = self.client.put(reverse('player_detail_api_url'))
        self.assertEqual(res.status_code, 403)

    def test_player_update_with_auth(self):
        data = {
            'first_name': 'Имя_2',
            'last_name': 'Фамилия_2',
            'citizenship': 'FR',
            'club': self.club,
        }
        self.client.login(username='username', password='password')
        res = self.client.put(reverse('player_detail_api_url'), data=data)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['first_name'], res.POST.club.first_name)
        self.assertEqual(data['last_name'], res.POST.club.last_name)
        self.assertEqual(data['citizenship'], res.POST.club.citizenship)
        self.assertEqual(data['club'], res.POST.club.club)

    def test_player_delete_with_no_auth(self):
        res = self.client.delete(reverse('player_detail_api_url'))
        self.assertEqual(res.status_code, 403)

    def test_player_delete_with_auth(self):
        self.client.login(username='username', password='password')
        res = self.client.delete(reverse('player_detail_api_url'))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Player.objects.all().count(), 0)
