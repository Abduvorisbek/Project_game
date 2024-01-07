from django.contrib import admin
from games.models import GamesModel

@admin.register(GamesModel)
class GameModelAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')