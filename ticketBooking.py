"""
Movie Ticket booking project - To do

fix the bugs in the input -
database structure change - use dictionary / key value pairs.
segregating the project into separate modules.
	MVC Structure.

show purchase summary

- program capability

Display the list of Movies!
Book a Ticker
 - allow selection of a movie from the displayed list
 - take input from the user.
    name
    number of tickets
 - print a summary of the booking. AKA the ticket

Display the list of Movies again should show a decremented value for available tickets.

Model = Data
    -* The movies List
        - Hard Coded
            - S. No.
            - Movie Name
            - Number of Tickets available
            - Show Date (V2)
            - Show Time (V2)
    -* The List of tickets - Calling this function with the requisite details should create a /
    record in the dictionary/list used to store the data
        - tickets Booked via the app
            - The date of the Booking (V2)
            - The S. No. Of the Movie
            - The name of the person making the booking
            - The number of Seats.
            - The phone number

View = Output on the screen
    - The movies list - Calling this module should produce the requisite output in console.
    - the Ticket - Calling this module with the details should produce the requisite output
        - Ticket ID / Phone number

Controller = The code that controls it.
    - Initialise the object
    - Ask for input
    - Book a ticket and print -
    - Print a already booked ticket - Reuse the Print Ticket Module
        - lookup using the already booked ticket.

"""
import json
from model import MovieTickets
from view import View
from mock import patch


# import datetime

while True:

    #Calling function to display movies on console
    movie_details = MovieTickets.get_movie_details()

    View.display_movies(movie_details)
    no_of_movies = MovieTickets.no_of_movies()
    movie_serial = View.get_movie_selection(no_of_movies)
    no_of_seats_available = MovieTickets.no_of_seats_available(movie_serial)
    max_no_bookable = min(no_of_seats_available, 6)
    ticket = View.get_ticket_details(max_no_bookable)
    name_of_movie = MovieTickets.get_movie_name(movie_serial)
    ticket_details = MovieTickets.book_a_ticket(movie_serial, ticket[0], ticket[1], ticket[2])
    # print ticket_details

    View.print_a_ticket(ticket_details)
