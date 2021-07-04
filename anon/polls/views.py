from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def index(request):
    return redirect('/polls')

@login_required
def polls(request):
    pass