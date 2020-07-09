from django.db import models
from datetime import datetime

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length = 200)
    question_text = models.TextField()
    date = models.DateTimeField('date published',default=datetime.now)
  
    def __str__(self):
        return self.title
   

class Choice(models.Model):
    #title = models.CharField(max_length =200)
    #choices_text = models.TextField()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    #date = models.DateTimeField('date published')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text