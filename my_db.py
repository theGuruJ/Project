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

    movies = {
        "Avengers Infinity Wars": {"avail_seats": 10, "booked_seats": 0},
        "Deadpool 2": {"avail_seats": 75, "booked_seats": 0},
        "Jurassic World":{"avail_seats": 0, "booked_seats": 0},
        "Kaala":{"avail_seats": 100, "booked_seats": 0},
        "Veere Di Wedding":{"avail_seats": 100, "booked_seats": 0}
    }

    # movies = {"1": {"name": 'Avengers: Infinity Wars', "avail_seats": 10, "booked_seats": 0,},
    #           "2": {"name": 'Deadpool 2', "avail_seats": 75, "booked_seats": 0,},
    #           "3": {"name": 'Jurassic World', "avail_seats": 0, "booked_seats": 0,},
    #           "4": {"name": 'Kaala', "avail_seats": 100, "booked_seats": 0,},
    #           "5": {"name": 'Veere Di Wedding', "avail_seats": 100, "booked_seats": 0,},
    #           }




    tickets = {}

    ticket_id = 1

    @staticmethod
    def no_of_movies():
        """
        :return number of movies available in the booking list:
        """
        list_of_movies = {}
        for i in MovieTickets.movies:
                list_of_movies[i] = MovieTickets.movies[i][1]
        return json.dumps(list_of_movies)


    @staticmethod
    def get_movie_details():
        """
        :return returns a json of the details of the movies:
        """
        print json.dumps(MovieTickets.movies)
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
        MovieTickets.tickets[MovieTickets.ticket_id] = [MovieTickets.ticket_id,movie_selection,name_of_booker,phone_number,number_of_seats_booked]
        ticket_details = json.dumps([MovieTickets.ticket_id,MovieTickets.movies[movie_selection][0],name_of_booker,phone_number,number_of_seats_booked])
        MovieTickets.movies[movie_selection][1] -= number_of_seats_booked
        MovieTickets.movies[movie_selection][2] += number_of_seats_booked
        MovieTickets.movies[movie_selection][3].append(MovieTickets.ticket_id)
        MovieTickets.ticket_id += 1
        print("Ticket Booked")
        return ticket_details


if __name__ == '__main__':
    main()
