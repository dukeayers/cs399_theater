from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from theater_project.models import Info, Movie , Store
# Create your views here.
def home(request):
    return render(request, 'index.html', {'all_movies': Info.objects.all()})

def events(request):
    return render(request,'events.html', {'all_movies': Info.objects.all()})

def movies(request):
    return render(request,'movies.html', {'all_movies': Info.objects.all()})

def showtimes(request):
    return render(request,'showtimes.html', {'all_movies': Info.objects.all(), 'all_times': Movie.objects.all()})
#, 'movie_info': Movie.objects.filter(title="Duke's Heroes"), 'movie_info2': Movie.objects.filter(title="Movie3"), 'movie_info3': Movie.objects.filter(title="Movie3"), 'movie_info4': Movie.objects.filter(title="Movie4"), 'movie_info5': Movie.objects.filter(title="Movie5")

def store(request):
    return render(request,'store.html', {'store_item': Store.objects.all()})

def team(request):
    return render(request,'team.html', {'all_movies': Info.objects.all()})