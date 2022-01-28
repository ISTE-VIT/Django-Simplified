from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=255)
    body  = models.TextField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return(reverse("tasks"))
    
    class Meta:
        ordering = ["complete" , "-created"]

