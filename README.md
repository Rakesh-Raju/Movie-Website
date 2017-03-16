MOVIE WEBPAGE PROJECT
---------------------

This is a simple project coded in python, that essentially allows a user to create a webpage that displays a set of movies.
This includes their titles, their poster/box art, and the official trailer of that movie.

CLASSES:

media.py - A class that defines what a movie object consists of. A movie has a parameter of title, poster url (or box art url), and the trailer url.

fresh_tomatoes.py - A class that actually generates the webpage with proper formatting, and takes in a list of movies and manipulates it accordingly.

entertainment_center.py - A class that initializes a set of movie objects, puts them into a list, and runs the functions of fresh_tomatoes.py

Usage:

Simply run entertainment_center.py, making sure that media.py and fresh_tomatoes.py are in the same directory.

To modify how many movies there are, simply create more movie objects in entertainment.py (following the required parameters in media.py for a movie object)
and update movielist.

Author:
Rakesh Raju
3/14/17

(fresh_tomatoes.py provided by the team at Udacity)
