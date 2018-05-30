import model
import json


class View(object):
    @staticmethod
    def display_movies(movie_details):
        """
        To print to screen the details of movies
        :param movie_details:
        :return n/a:
        """
        movie_details = json.loads(movie_details)
        movie_details = {int(k): v for k, v in movie_details.items()}
        print '\n'
        print("The available movies are listed below!")
        print '%-8s%-30s%-5s' % ('S. No.', 'Name', 'No. Of Seats Available')
        for e in movie_details:
            print '%-8s%-30s%-5i' % (e, movie_details[e][0], movie_details[e][1])

    @staticmethod
    def get_movie_selection(no_of_movies):
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
                # no_of_seats_available = MovieTickets.no_of_seats_available(movie_serial)
                # max_no_bookable = min(no_of_seats_available, 6)
            except ValueError:
                print("Not a valid input, Please try again...")
        return movie_serial

    @staticmethod
    def get_ticket_details(max_no_bookable):
        name = raw_input('Please type in your name:')
        phone_number = raw_input('Please type in your Phone Number:')
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
                print 'Please type in a number between 1 and', max_no_bookable
        return name,phone_number,no_of_seats

    @staticmethod
    def print_a_ticket(ticket_details):
        """
        # ticket_details contains the following
        [MovieTickets.ticket_id,movie_selection,name_of_booker,phone_number,number_of_seats_booked]
        prints details of booked ticket to the screen

        :param ticket_details:
        :return n/a:
        """

        ticket_details = json.loads(ticket_details)
        print '   Ticket No:', ticket_details[0]
        print '        Name:', ticket_details[2]
        print 'Phone Number:', ticket_details[3]
        print ' Movie Name:', ticket_details[1]
        print 'Number of Seats:', ticket_details[4]
