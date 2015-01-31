from __future__ import unicode_literals
import datetime
from django.db import models, migrations

def add_data(apps, schema_editor):
    Movie = apps.get_model("theater_project", "Movie")

    #Pre-config'd Times for the movies
    Time1 = ['8:00 AM', '10:00 AM', '12:00 PM', '2:00 PM', '4:00 PM', '6:00 PM']
    Time2 = ['9:30 AM', '12:00 PM', '2:30 PM', '5:00 PM', '7:30 PM', '9:00 PM']
    Time3 = ['11:20 AM', '1:30 PM', '4:00 PM', '6:30 PM', '8:50 PM', '11:00 PM']
    Time4 = ['9:15 AM', '12:45 PM', '4:15 PM', '7:45 PM', '10:45 PM']
    Time5 = ['9:30 AM', '10:15 PM']
    #Some Pre-config'd Titles
    Titles = ["Duke's Heroes", "Movie2", "Movie3", "Movie4", "Movie5"]

    #Seeds all of our data
    for i in Time1:
        data = Movie(title = Titles[0], time = i)
        data.save()

    for i in Time2:
        data = Movie(title = Titles[1], time = i)
        data.save()

    for i in Time3:
        data = Movie(title = Titles[2], time = i)
        data.save()

    for i in Time4:
        data = Movie(title = Titles[3], time = i)
        data.save()

    for i in Time5:
        data = Movie(title = Titles[4], time = i)
        data.save()



class Migration(migrations.Migration):

    dependencies = [
        ('theater_project', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]