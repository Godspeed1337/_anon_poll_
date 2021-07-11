from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Event, Question, Choise, Turnout, Profile
from django.contrib import auth
# Create your views here.

@login_required
def index(request):
    return redirect('/polls')

@login_required
def polls(request):
    try:
        group = request.user.groups.get().name
    except:
        group = 'None'
    context = {'events': Event.objects.all(),
               'group': group,
               }
    return render(request, 'polls/polls.html', context)

@login_required
def questions(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == "POST":
        questionslist = Question.objects.filter(event_id= event_id)
        choises = Choise.objects.filter(question_id__event_id=event_id)
        for i in questionslist:
            value = request.POST.get(f'{i.pk}')
            choise = choises.get(question_id=i.pk)
            if value == 'za':
                choise.za += 1
            elif value == 'protiv':
                choise.protiv += 1
            else:
                choise.abstained += 1
            choise.save()
        p = Turnout(event_id=Event.objects.get(pk=event_id), profile_id=Profile.objects.get(user_id=request.user.pk))
        p.save()
        return redirect("/")
    else:
        questionslist = Question.objects.filter(event_id= event_id)
        if Choise.objects.filter(question_id__event_id=event_id).exists():
            context = {'choises' : Choise.objects.filter(question_id__event_id=event_id),
                       'questionslist' : questionslist,
                        'event' : event,
                       }
        else:
            for i in range(len(questionslist)):
                p = Choise(question_id=questionslist[i])
                p.save()
            context = {'choises': Choise.objects.filter(question_id__event_id=event_id),
                       'questionslist': questionslist,
                       'event': event,
                       }
        return render(request, 'polls/questions.html', context)

@login_required
def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return redirect("/")

@login_required
def results(reqeust):


