Todo List
---------
* Footer
* Finish Index Page
* Add details about other movies
* Create Events (this can be hard-coded) - Claimed by Leah
* Location added to index page - Duke will do
* Directions added to index page - up for grabs




Movie
-------

* Title
* Time

Rating
-----

* Title
* Descr.
* Thumbnail

Store
-----

* Item Name
* Descr.
* Price

Pages to be done:
--------

Index - Contact Us, About Us - claimed by Nancy

Movies

Showtimes

Events

Store - claimed by Abdul

Our Team - Hiring?- Claimed by Leah 

Trying to setup your Database?
-----------------------------

Here are a few things to get you started...

>Number 1: 

If you aren't using Pycharm then I would suggest now is the time to get it because you can visually see all of the data
being put into the database and manipulate it as well - this is very convenient. So ensure you have it.

>Number 2:

Setup the builtin database by clicking on the word "Database" on the rightmost portion of the screen. This will pull up a menu of things to do. Here is what to click:

1. Click the green plus button
2. Hover over Data Source
3. Hover over SQLite
4. Click Xerial
5. It will prompt you to download a plugin at the bottom of the box that pops up. You should do this.

From here, you will just need to link the filepath to the db.sqlite3 file within your database. Then hit "Apply" and "OK".

>Number 3:

Make sure you are in the second directory, aka "somefilepath/theater_project/theater_project" before the next line.

Type in the following commands:

1. python manage.py makemigrations theater_project
2. python manage.py migrate theater_project

And then you are done...

But wait! The database migration files were updated and my database isn't updating, what do I do?
----------------

>Number 1:

Click on the "Database" tab on the rightmost part of the screen. Then hit CTRL - ALT - Y at the same time to synchronize the database.

>Number2:

Open the table entitled "django_migrations", this is where you will see a few rows of data - we are particularly interested in the rows that pertain to "theater_project". You should highlight each row and DELETE them.

>Number 3:

Highlight the three tables that we generated through the migration files (i.e. theater_project_info, theater_project_movie, theater_project_store) and then delete these.

>Number 4:

Make sure you are in the second directory, aka "somefilepath/theater_project/theater_project" before the next line.

Type in the following commands:

1. python manage.py makemigrations theater_project
2. python manage.py migrate theater_project

And then you are done...
