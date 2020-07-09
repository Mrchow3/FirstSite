from django.contrib import admin
from django.db import models
from .models import Question, Choice

# Register your models here.

#class QuestionAdmin(admin.ModelAdmin)
#class ChoicesAdmin(admin.ModelAdmin)

admin.site.register(Question)
#admin.site.register(Choice)
