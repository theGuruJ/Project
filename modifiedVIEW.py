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
        output = ''
        output += "\nThe available movies are listed below!"
        output += '\n%-8s%-30s%-5s' % ('S. No.', 'Name', 'No. Of Seats Available')
        for e in movie_details:
            output += '\n%-8s%-30s%-5i' % (e, movie_details[e][0], movie_details[e][1])
        return output

    @staticmethod
    def get_movie_selection(select_test,no_of_movies):
        no_of_movies = json.loads(no_of_movies)
        no_of_movies = {int(m): s for m, s in no_of_movies.items()}
        while True:  # So that we can repeatedly ask for input until we get the correct input
            try:
                selection = select_test
                movie_serial = int(selection)
                if movie_serial in no_of_movies:  # Checking if the selection corresponds to the no of movies in the list.
                    if no_of_movies[movie_serial] == 0:
                        return "No seats available, select another movie!"
                    else:
                        return movie_serial
                else:
                    return "Please make a valid selection!"
                    # to repeat loop if the selection is not in list of movies.
                    # no_of_seats_available = MovieTickets.no_of_seats_available(movie_serial)
                    # max_no_bookable = min(no_of_seats_available, 6)
            except ValueError:
                return "Not a valid input, Please try again..."

    @staticmethod
    def get_ticket_details(name_s,phone_no,num_seats,max_no_bookable):
        name = name_s
        phone_number = phone_no
        while True:
            try:
                # no_seats_in = "How many seats would you like to book?(Max " + str(max_no_bookable) + " seats allowed)"
                # no_of_seats = raw_input(no_seats_in)
                no_of_seats = int(num_seats)
                if (no_of_seats < 1) or (no_of_seats > max_no_bookable):
                    raise ValueError
                else:
                    break
            except ValueError:
                return 'invalid seat numbers'
        return name, phone_number, no_of_seats

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
