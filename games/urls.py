from django.urls import path
from games.views import GameListView, GameDetailView, GameCreateView, GameUpdateView, GameDeleteView

app_name = 'games'


urlpatterns = [
    path('', GameListView.as_view(), name='list'),
    path('<int:pk>/', GameDetailView.as_view(), name='detail'),
    path('create/', GameCreateView.as_view(), name='create'),
    path('<int:pk>/update/', GameUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', GameDeleteView.as_view(), name='delete')
]