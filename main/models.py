from django.db import models
from datetime import datetime

# Create your models here.
class Data(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField('date published')


    def __str__(self):
        return self.title