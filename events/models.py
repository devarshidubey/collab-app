from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

modes=(
    ("Online","Online"),
    ("Offline","Offline"),
    ("Hybrid","Hybrid"),
)

class Events(models.Model):
    name=models.TextField(max_length=50,null=False,blank=False)
    link=models.URLField(max_length=1000,null=False,blank=False)
    location=models.TextField(null=False,blank=False)
    # Poster=models.ImageField()
    date=models.DateTimeField(auto_now_add=True)
    modes = models.CharField(
        max_length = 20,
        choices = modes,
        default = 'Hybrid'
        )
    posted_by=models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('events_detail', args=[str(self.id)])

    
