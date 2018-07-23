

# movies model
#
# key
# name - string
# capacity - integer
# available seats - integer
# booked seats - integer
#
#
# tickets
# 	key -
# 	movie selection - key of the movie?
# 	user ID - Key of the user entry?
# 	number_of_seats_booked - integer
#
# user db:
# 	key -
# 	name - string
# 	email address - string
# 	phone number - integer
#

import json
from google.appengine.ext import ndb


class Session(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def set_session(cls, user_data):
        return cls(name=user_data.get('name'), email=user_data.get('email')).put()


class MovieDetails(ndb.Model):
    movie_name = ndb.StringProperty()
    capacity = ndb.IntegerProperty()
    available_seats = ndb.IntegerProperty()
    booked_seats = ndb.IntegerProperty()
    status = ndb.StringProperty()

    @staticmethod
    def get_movie_name(movie_name):
        return (ndb.Key("MovieDetails", movie_name).get()).movie_name

    def get_movie_details(self):
        #to be implemented
        pass

class Customers(ndb.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    customer_name = ndb.StringProperty()
    email_address = ndb.StringProperty()
    phone_number = ndb.IntegerProperty()

    @staticmethod
    def create_customer(email_address, password, customer_name, phone_number):
        if not ndb.Key("Customers", email_address).get():
            customer = Customers(
            id=email_address, username=email_address, password=password, customer_name=customer_name,
            email_address=email_address, phone_number=int(phone_number)
            )
        else:
            return False

        return customer.put()


class Tickets(ndb.Model):
    movie_selection = ndb.KeyProperty(kind=MovieDetails)
    customer_id = ndb.KeyProperty(kind=Customers)
    no_of_seats_booked = ndb.IntegerProperty()


class MovieTickets(object):
    '''
    provides for a way to store and retrieve details of tickets issued
    uses a dictionary structure.
    {   ticket ID: [Movie Serial Number(int),
                    Customer name (Str),
                    The number of Seats(int, max of 6, no more per booking.
                    The phone number (10 digit numeric number}

    '''

    movies = {
        "Avengers Infinity Wars": {"avail_seats": 4, "booked_seats": 0, "tickets_list": []},
        "Deadpool 2": {"avail_seats": 75, "booked_seats": 0, "tickets_list": []},
        "Jurassic World":{"avail_seats": 100, "booked_seats": 0, "tickets_list": []},
        "Kaala":{"avail_seats": 100, "booked_seats": 0, "tickets_list": []},
        "Veere Di Wedding":{"avail_seats": 10, "booked_seats": 0, "tickets_list": []}
    }

    # movies = {"1": {"name": 'Avengers: Infinity Wars', "avail_seats": 10, "booked_seats": 0,},
    #           "2": {"name": 'Deadpool 2', "avail_seats": 75, "booked_seats": 0,},
    #           "3": {"name": 'Jurassic World', "avail_seats": 0, "booked_seats": 0,},
    #           "4": {"name": 'Kaala', "avail_seats": 100, "booked_seats": 0,},
    #           "5": {"name": 'Veere Di Wedding', "avail_seats": 100, "booked_seats": 0,},
    #           }

    tickets = {}

    ticket_id = 1

    # @staticmethod
    # def no_of_movies():
    #     """
    #     :return number of movies available in the booking list, with no of available seats:
    #     """
    #     list_of_movies = {}
    #     for i in MovieTickets.movies:
    #         list_of_movies.update({i:MovieTickets.movies[i]["avail_seats"]})
    #     return json.dumps(list_of_movies)


    @staticmethod
    def get_movie_details():
        """
        :return returns a json of the details of the movies:
        """
        return json.dumps(MovieTickets.movies)

    @staticmethod
    def no_of_seats_available(movie_selection):
        """
        input: the movie selection

        :param movie_selection:
        :return returns the number of seats still available to book for a specific movie:
        """
        return MovieTickets.movies[movie_selection]["avail_seats"]


    @staticmethod
    def get_movie_name(movie_selection):
        """
        input: takes the selection of the user for booking seats for a movie.
        :param movie_selection:
        :return the name of the movie:
        """
        return MovieTickets.movies[movie_selection]["name"]


    @staticmethod
    def book_a_ticket(movie_selection,name_of_booker,phone_number,number_of_seats_booked):
        """
        enables to book a ticket

        :param movie_selection:
        :param name_of_booker:
        :param phone_number:
        :param number_of_seats_booked:
        :return ticket details in a json format, to be used to print to screen to confirm to user:
        """
        MovieTickets.tickets.update({MovieTickets.ticket_id : {'movieSelection' : movie_selection, "name_of_user" : name_of_booker, "phone_number" : phone_number, "no_of_seats" : number_of_seats_booked}})
        #ticket_details = json.dumps([MovieTickets.ticket_id,MovieTickets.movies[movie_selection][0],name_of_booker,phone_number,number_of_seats_booked])
        ticket_details = MovieTickets.tickets.get(MovieTickets.ticket_id)
        number_of_seats_booked = int(number_of_seats_booked)
        MovieTickets.movies[movie_selection]["avail_seats"] -= number_of_seats_booked
        MovieTickets.movies[movie_selection]["booked_seats"] += number_of_seats_booked
        MovieTickets.movies[movie_selection]["tickets_list"].append(MovieTickets.ticket_id)
        MovieTickets.ticket_id += 1
        print("Ticket Booked")
        return ticket_details


if __name__ == '__main__':
    main()
