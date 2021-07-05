from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required
def index(request):
    return redirect('/polls')

@login_required
def polls(request):
    return HttpResponse("Hello, world. You're at the polls")

@login_required
def questions(request, event_id):
    return HttpResponse(f'Hello, this is page of {event_id} event')