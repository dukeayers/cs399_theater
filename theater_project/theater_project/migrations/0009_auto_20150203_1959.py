# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models, migrations

def add_data(apps, schema_editor):
    Movie = apps.get_model("theater_project", "Movie")
    Info = apps.get_model("theater_project", "Info")
    Store = apps.get_model("theater_project", "Store")
    Event = apps.get_model("theater_project", "Event")

    #Pre-config'd Times for the movies
    Time1 = ['8:00 AM', '10:00 AM', '12:00 PM', '2:00 PM', '4:00 PM', '6:00 PM']
    Time2 = ['9:30 AM', '12:00 PM', '2:30 PM', '5:00 PM', '7:30 PM', '9:00 PM']
    Time3 = ['11:20 AM', '1:30 PM', '4:00 PM', '6:30 PM', '8:50 PM', '11:00 PM']
    Time4 = ['9:15 AM', '12:45 PM', '4:15 PM', '7:45 PM', '10:45 PM']
    Time5 = ['9:30 AM', '10:15 PM']
    #Some Pre-config'd Titles
    Titles = ["Duke's Heroes", "Camorta", "Outlast", "The Garden", "Velvet Exile"]
    #Pre-config'd Descriptions according to each movie.
    Descr = ["A great movie about how Duke aspires to become something like his greatest heroes of all time. This may seem like another sad, unfortunate story of how Duke never actually gets his aspirations but it all gets better with the Mountain Dew and Doritos.", 
	"Lincoln Six-Echo is a resident of a seemingly Utopian but contained facility in the year 2019. Like all of the inhabitants of this carefully controlled environment, Lincoln hopes to be chosen to go to the Camorta - reportedly the last uncontaminated spot on the planet. But Lincoln soon discovers that everything about his existence is a lie. He and all of the other inhabitants of the facility are actually human clones. Lincoln makes a daring escape with a beautiful fellow resident named Jordan Two-Delta. Relentlessly pursued by the forces of the sinister institute that once housed them, Lincoln and Jordan engage in a race for their lives to literally meet their makers.", 
	"The misadventures of Mickey and Mallory: outcasts, lovers, and serial killers. They travel across Route 666 conducting psychadelic mass-slaughters not for money, not for revenge, just for kicks. Glorified by the media, the pair become legendary folk heroes; their story told by the single person they leave alive at the scene of each of their slaughters.", 
	"The impressionistic story of a Texas family in the 1950s. The film follows the life journey of the eldest son, Jack, through the innocence of childhood to his disillusioned adult years as he tries to reconcile a complicated relationship with his father (Brad Pitt). Jack (played as an adult by Sean Penn) finds himself a lost soul in the modern world, seeking answers to the origins and meaning of life while questioning the existence of faith.", 
	"During the psychedelic 60s and 70s Larry 'Doc' Sportello is surprised by his former girlfriend and her plot for her billionaire boyfriend, his wife, and her boyfriend. A plan for kidnapping gets shaken up by the oddball characters entangled in this groovy kidnapping romp based upon the novel by Thomas Pynchon."]
    #paths of each picture once we get them
    ThumbLocation = ["movie-pictures/dukehero.png", "movie-pictures/camorta.png", "movie-pictures/outlast.png", "movie-pictures/thegarden.png", "movie-pictures/velvetexile.png"]
    #list of durations for the movies
    Durations = ["121", "136", "118", "139", "148"]
    #rating of each movie
    Ratings = ["PG", "PG - 13", "G", "PG - 13", "R"]

	#Seeded data for the store page
    Items = ["Movie Ticket", "Souvenir Cup", "Large Popcorn", "Theater T-Shirt", "Medium Popcorn", "Candy"]
    Prices = ["$6.00", "$5.00", "$3.00", "$20.00", "$3.00", "$4.00"]
    ItemDescr = ["A general movie ticket for any movie you would like to see.", "A refillable cup that allows for 50 cent refills!", "Popcorn, but large!", "An awesome gift idea for any of your friends! Nevermind that it is literally made out of stale popcorn and the dreams of failed actors/actresses!", "Popcorn, but in a medium container!", "Did... Did someone just say... Candy? Oh.. I'm in."]
    ThumbLocationStore = ["store_items/ticket.jpg", "store_items/cup.JPG", "store_items/largepop.jpg", "store_items/tshirt.jpg", "store_items/medpop.jpg", "store_items/candy.jpg"]

    #Seeded data for the events page
    eTitle = ["Children's Film Marathon", "3D Animation Film Festival"]
    eDate = ["Date: June 5th, 2015 12pm-5pm", "Date: August 16th, 2015 6pm-10pm"]
    eImage = ["event-icons/children.png", "event-icons/festival.png"]
    eDescr = ["Are you a film enthusiast?  Do you have a passion for 3D animation?  If you answered yes to either question then we have some good news for you!  This coming August Sharkins Theaters is holding its first annual 3D Animation Film Festival!  Local film makers will present their finest work for your viewing pleasure all for our current ticket price.  Order your ticket today!", "This summer our theater is holding a special marathon of family movies for your entertainment.  This marathon includes movies you all know and love including: How to Train Your Dragon, Despicable Me and The Lego Movie!  Children's tickets are $3.00 and adults are $5.00.  Don't miss out on this evening of fun!"]

    #Add in all of the Event data
    for i in range(0,2):
        data = Event(title = eTitle[i], date = eDate[i], image = eImage[i], descr = eDescr[i])
        data.save()

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
