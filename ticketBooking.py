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

while True:

    # Getting movie details
    movie_details = MovieTickets.get_movie_details()

    # sending movie details to display methos
    View.display_movies(movie_details)

    # getting details of available movies, only serial numbers
    no_of_movies = MovieTickets.no_of_movies()

    # passing serial numbers to method to get movie selection from user
    movie_serial = View.get_movie_selection(no_of_movies)

    # getting number of seats available for selected movie
    no_of_seats_available = MovieTickets.no_of_seats_available(movie_serial)

    # defining max no of seats bookable, least between remaining seats or 6 seats.
    max_no_bookable = min(no_of_seats_available, 6)

    # getting user details from booker. method returns a json with
    user_details = View.get_ticket_details(max_no_bookable)

    # booking a ticket. the method returns a json with the ticket details
    booked_ticket_details = MovieTickets.book_a_ticket(movie_serial, user_details[0], user_details[1], user_details[2])

    # print ticket_details
    View.print_a_ticket(booked_ticket_details)

if __name__ == '__main__':
    main()
