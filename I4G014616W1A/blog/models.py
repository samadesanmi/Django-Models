from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    Text=models.TextField()
    Author = models.CharField(max_length=50)
    Created_Date=models.DateTimeField(auto_now_add=True)
    Published_Date=models.DateTimeField(auto_now=True)

    def __str__(self)-> str:
        return self.Title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    