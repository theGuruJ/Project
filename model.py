import json


class MovieTickets(object):
    '''
    provides for a way to store and retrieve details of tickets issued
    uses a dictionary structure.
    {   ticket ID: [Movie Serial Number(int),
                    Customer name (Str),
                    The number of Seats(int, max of 6, no more per booking.
                    The phone number (10 digit numeric number}

    '''

    movies = {1: ['Avengers: Infinity Wars', 10, 0,[]],
              2: ['Beyond The Clouds', 75, 0,[]],
              3: ['Nanu Ki Jaanu', 100, 0,[]]}
    tickets = {}

    ticket_id = 1

    @staticmethod
    def no_of_movies():
        """
        :return number of movies available in the booking list:
        """
        list_of_movies = []
        for i in MovieTickets.movies:
            if MovieTickets.movies[i][1] != 0:
                list_of_movies.append(i)

        return list_of_movies


    @staticmethod
    def get_movie_details():
        """
        :return returns a json of the details of the movies:
        """
        movie_list = {}
        for i in MovieTickets.movies:
            if MovieTickets.movies[i][1] != 0:
                movie_list[i]=MovieTickets.movies[i]
        return json.dumps(movie_list)

    @staticmethod
    def no_of_seats_available(movie_selection):
        """
        input: the movie selection

        :param movie_selection:
        :return returns the number of seats still available to book for a specific movie:
        """
        return MovieTickets.movies[movie_selection][1]


    @staticmethod
    def get_movie_name(movie_selection):
        """
        input: takes the selection of the user for booking seats for a movie.
        :param movie_selection:
        :return the name of the movie:
        """
        return MovieTickets.movies[movie_selection][0]


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
        MovieTickets.tickets[MovieTickets.ticket_id] = [MovieTickets.ticket_id,movie_selection,name_of_booker,phone_number,number_of_seats_booked]
        ticket_details = json.dumps([MovieTickets.ticket_id,MovieTickets.movies[movie_selection][0],name_of_booker,phone_number,number_of_seats_booked])
        MovieTickets.movies[movie_selection][1] -= number_of_seats_booked
        MovieTickets.movies[movie_selection][2] += number_of_seats_booked
        MovieTickets.movies[movie_selection][3].append(MovieTickets.ticket_id)
        MovieTickets.ticket_id += 1
        print("Ticket Booked")
        return ticket_details

