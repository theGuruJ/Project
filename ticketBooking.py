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


# import datetime


def booking():
    movie_details = MovieTickets.get_movie_details()
    #    print (movie_details)
    View.display_movies(movie_details)
    no_of_movies = MovieTickets.no_of_movies()
    while True:  # So that we can repeatedly ask for input until we get the correct input
        try:
            selection = raw_input('\n'
                                  'Please type in the serial number of the movie you want to book!')
            movie_serial = int(selection)
            if (movie_serial < 1) or (
                    movie_serial > no_of_movies):  # Checking if the selection corresponds to the no of movies in the list.
                raise ValueError
            else:
                break  # to break out of while loop and continue with the program if the input is correct
            no_of_seats_available = MovieTickets.no_of_seats_available(movie_serial)
            max_no_bookable = min(no_of_seats_available, 6)
        except ValueError:
            print("Not a valid input, Please try again...")
    no_of_seats_available = MovieTickets.no_of_seats_available(movie_serial)
    max_no_bookable = min(no_of_seats_available, 6)
    while True:  # So that we can repeatedly ask for input until we get the correct input
        try:
            if max_no_bookable == 0:
                raise KeyError
            else:
                break  # to break out of while loop and continue with the program if the input is correct
        except KeyError:
            print("Movie selection does not have any seats available! Please make a different selection...")
            booking()
    name = raw_input('Please type in your name:')
    phone_number = raw_input('Please type in your Phone Number:')
    no_of_seats_available = MovieTickets.no_of_seats_available(movie_serial)
    max_no_bookable = min(no_of_seats_available, 6)
    while True:
        try:
            string = "How many seats would you like to book?(Max " + str(max_no_bookable) + " seats allowed)"
            no_of_seats = raw_input(string)
            no_of_seats = int(no_of_seats)
            if (no_of_seats < 1) or (no_of_seats > max_no_bookable):
                raise ValueError
            else:
                break
        except ValueError:
            print 'Please type in a number between 1 and', max_no_bookable, '...'
    #            date_of_show = raw_input('\n'
    #                'Please type in the serial number of the movie you want to book!')
    #            time_of_show= raw_input('\n'
    #                'Please type in the serial number of the movie you want to book!')

    #    tickets.book_a_ticket(x,name,phone_number,no_of_seats)
    name_of_movie = MovieTickets.get_movie_name(movie_serial)
    ticket_details = MovieTickets.book_a_ticket(movie_serial, name, phone_number, no_of_seats)
    # print ticket_details
    View.print_a_ticket(ticket_details)
    if __name__ == '__main__':
        booking()


if __name__ == '__main__':
    booking()
