from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#    Turnout_id = models.ForeignKey('Turnout', on_delete=models.CASCADE)

class Turnout(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Event(models.Model):
    date = models.DateTimeField('Дата и время проведения заседания')
    open_bool = models.BooleanField('Заседание открыто?')
 #   turnout_id = models.ForeignKey(Turnout, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}'

class Question(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    text = models.CharField(max_length=110)

class Choise(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    za = models.IntegerField(default=0)
    protiv = models.IntegerField(default=0)
    abstained = models.IntegerField(default=0)