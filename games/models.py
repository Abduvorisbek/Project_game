from django.db import models

class GamesModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Games'
        verbose_name = 'Game'
