from django.contrib import admin

# Register your models here.
from .models import Event, Question

admin.site.register(Question, Event)