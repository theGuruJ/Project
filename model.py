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
        return len(MovieTickets.movies)

    @staticmethod
    def get_movie_details():
        return json.dumps(MovieTickets.movies)


    @staticmethod
    def no_of_seats_available(movie_selection):
        return MovieTickets.movies[movie_selection][1]

    @staticmethod
    def get_movie_name(movie_selection):
        return MovieTickets.movies[movie_selection][0]

    @staticmethod
    def book_a_ticket(movie_selection,name_of_booker,phone_number,number_of_seats_booked):
        MovieTickets.tickets[MovieTickets.ticket_id] = [MovieTickets.ticket_id,movie_selection,name_of_booker,phone_number,number_of_seats_booked]
        ticket_details = json.dumps([MovieTickets.ticket_id,MovieTickets.movies[movie_selection][0],name_of_booker,phone_number,number_of_seats_booked])
        MovieTickets.movies[movie_selection][1] -= number_of_seats_booked
        MovieTickets.movies[movie_selection][2] += number_of_seats_booked
        MovieTickets.movies[movie_selection][3].append(MovieTickets.ticket_id)
        MovieTickets.ticket_id += 1
        print("Ticket Booked")
        return ticket_details

