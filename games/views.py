from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from games.forms import GameForm
from games.models import GamesModel


class GameListView(ListView):
    model = GamesModel
    template_name = 'games.html'
    context_object_name = 'games'


class GameDetailView(DetailView):
    model = GamesModel
    template_name = 'games_detail.html'
    context_object_name = 'game'


class GameCreateView(CreateView):
    model = GamesModel
    form_class = GameForm
    template_name = 'game_create.html'
    success_url = reverse_lazy('games:list')


class GameUpdateView(UpdateView):
    model = GamesModel
    form_class = GameForm
    template_name = 'game_update.html'
    success_url = reverse_lazy('games:list')
    context_object_name = 'game'


class GameDeleteView(DeleteView):
    model = GamesModel
    template_name = 'game_delete_confirm.html'
    success_url = reverse_lazy('games:list')
    context_object_name = 'game'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(GamesModel, pk=pk)