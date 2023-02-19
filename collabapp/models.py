from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class CollabRequestPost(models.Model):
    title = models.CharField(max_length = 255)
    team_size = models.SmallIntegerField()
    description = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        null = True,
    )
    #tags to be added later

    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('request list')

