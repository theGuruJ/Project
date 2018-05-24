import model
import json


class view(object):
    @staticmethod
    def display_movies(movie_details):
        movie_details = json.loads(movie_details)
        movie_details = {int(k): v for k, v in movie_details.items()}
        print '\n'
        print("The available movies are listed below!")
        print '%-8s%-30s%-5s' % ('S. No.', 'Name', 'No. Of Seats Available')
        for e in movie_details:
            print '%-8s%-30s%-5i' % (e, movie_details[e][0], movie_details[e][1])

    @staticmethod
    def print_a_ticket(ticket_details):
        # [MovieTickets.ticket_id,movie_selection,name_of_booker,phone_number,number_of_seats_booked]
        ticket_details = json.loads(ticket_details)
        print '   Ticket No:', ticket_details[0]
        print '        Name:', ticket_details[2]
        print 'Phone Number:', ticket_details[3]
        print ' Movie Name:', ticket_details[1]
        print 'Number of Seats:', ticket_details[4]
