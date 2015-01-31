from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from theater_project.models import Info
# Create your views here.
def home(request):
    return render(request, 'index.html', {'all_movies': Info.objects.all()})

def events(request):
    return render(request,'events.html')

def movies(request):
    return render(request,'movies.html')

def showtimes(request):
    return render(request,'showtimes.html')

def store(request):
    return render(request,'store.html')

def team(request):
    return render(request,'team.html')