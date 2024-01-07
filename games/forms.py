from django import forms
from games.models import GamesModel


class GameForm(forms.ModelForm):
    class Meta:
        model = GamesModel
        fields = ['name', 'description', 'link']