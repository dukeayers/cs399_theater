from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from theater_project.models import Info
# Create your views here.
def home(request):
    return render(request, 'index.html', {'all_movies': Info.objects.all()})

def events(request):
    return render(request,'events.html', {'all_movies': Info.objects.all()})

def movies(request):
    return render(request,'movies.html', {'all_movies': Info.objects.all()})

def showtimes(request):
    return render(request,'showtimes.html', {'all_movies': Info.objects.all()})

def store(request):
    return render(request,'store.html', {'all_movies': Info.objects.all()})

def team(request):
    return render(request,'team.html', {'all_movies': Info.objects.all()})