from django.contrib import admin

# Register your models here.
from .models import Event, Question, Choise, Profile, Turnout

admin.site.register(Question)
admin.site.register(Event)
admin.site.register(Choise)
admin.site.register(Profile)
admin.site.register(Turnout)