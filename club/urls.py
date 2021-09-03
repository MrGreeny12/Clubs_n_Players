from django.urls import path
from club.views import ClubListView, PlayerCreateView, PlayerDetailView, PlayerListView, ClubDetailView, ClubCreateView

app_name = 'club'
urlpatterns = [
    path('club/list/', ClubListView.as_view(), name='club_list_api_url'),
    path('club/create/', ClubCreateView.as_view(), name='club_create_api_url'),
    path('club/detail/<int:pk>', ClubDetailView.as_view(), name='club_detail_api_url'),
    path('player/create/', PlayerCreateView.as_view(), name='player_create_api_url'),
    path('player/detail/<int:pk>/', PlayerDetailView.as_view(), name='player_detail_api_url'),
    path('player/list/', PlayerListView.as_view(), name='player_list_api_url'),
]