from __future__ import unicode_literals
import datetime
from django.db import models, migrations

def add_data(apps, schema_editor):
    Movie = apps.get_model("theater_project", "Movie")
    Info = apps.get_model("theater_project", "Info")
    Store = apps.get_model("theater_project", "Store")

    #Pre-config'd Times for the movies
    Time1 = ['8:00 AM', '10:00 AM', '12:00 PM', '2:00 PM', '4:00 PM', '6:00 PM']
    Time2 = ['9:30 AM', '12:00 PM', '2:30 PM', '5:00 PM', '7:30 PM', '9:00 PM']
    Time3 = ['11:20 AM', '1:30 PM', '4:00 PM', '6:30 PM', '8:50 PM', '11:00 PM']
    Time4 = ['9:15 AM', '12:45 PM', '4:15 PM', '7:45 PM', '10:45 PM']
    Time5 = ['9:30 AM', '10:15 PM']
    #Some Pre-config'd Titles
    Titles = ["Duke's Heroes", "Movie2", "Movie3", "Movie4", "Movie5"]
    #Pre-config'd Descriptions according to each movie.
    Descr = ["A great movie about how Duke aspires to become something like his greatest heroes of all time. This may seem like another sad, unfortunate story of how Duke never actually gets his aspirations but it all gets better with the Mountain Dew and Doritos.", "Null", "Null", "Null", "Null"]
    #paths of each picture once we get them
    ThumbLocation = ["movie-pictures/dukehero.png", "movie-pictures/camorta.png", "movie-pictures/outlast.png", "movie-pictures/thegarden.png", "movie-pictures/velvetexile.png"]
    #list of durations for the movies
    Durations = ["121", "null", "null", "null", "null"]
    #rating of each movie
    Ratings = ["PG - 13", "null", "null", "null", "null"]
    Items = ["Movie Ticket", "Souvenir Cup", "Large Popcorn", "Theater T-Shirt", "Medium Popcorn", "Candy"]
    Prices = ["$6.00", "$5.00", "$3.00", "$20.00", "$3.00", "$4.00"]
    ItemDescr = ["A general movie ticket for any movie you would like to see.", "A refillable cup that allows for 50 cent refills!", "Popcorn, but large!", "An awesome gift idea for any of your friends! Nevermind that it is literally made out of stale popcorn and the dreams of failed actors/actresses!", "Popcorn, but in a medium container!", "Did... Did someone just say... Candy? Oh.. I'm in."]
    ThumbLocationStore = ["store_items/ticket.jpg", "store_items/cup.JPG", "store_items/largepop.jpg", "store_items/tshirt.jpg", "store_items/medpop.jpg", "store_items/candy.jpg"]

    #Seeds all of our data for the Movie Table
    for i in Time1:
        data = Movie(title = Titles[0],  time = i)
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

#Seeds all of our data for the Info table
    for i in range(0, 5):
        data = Info(title = Titles[i], description = Descr[i], thumbnail = ThumbLocation[i], rating = Ratings[i], duration = Durations[i])
        data.save()

    for i in range(0, 6):
        data = Store(item = Items[i], description = ItemDescr[i], price = Prices[i], thumbnail = ThumbLocationStore[i])
        data.save()

class Migration(migrations.Migration):

    dependencies = [
        ('theater_project', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data)
    ]