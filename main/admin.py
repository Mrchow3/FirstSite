from django.contrib import admin
from .models import Data

from django.db import models


class DataAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title/date", {'fields': ["title", "published"]}),

        ("Content", {"fields": ["content"]})
    ] 


admin.site.register(Data, DataAdmin)