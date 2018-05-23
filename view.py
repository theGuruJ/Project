import model
import json

class view(object):
    @staticmethod
    def display_movies(movie_details):
        movie_details = json.loads(movie_details)
        print '\n'
        print("The available movies are listed below!")
        print '%-8s%-30s%-5s' % ('S. No.', 'Name', 'No. Of Seats Available')
        for e in movie_details:
            print '%-8s%-30s%-5i' % (e,movie_details[e][0],movie_details[e][1])

    @staticmethod
    def print_a_ticket(ticket_id,movie_name):
        print '   Ticket No:',ticket_id
        print '        Name:',model.MovieTickets.tickets[ticket_id][1]
        print 'Phone Number:',MovieTickets.tickets[ticket_id][2]
        print ' Movie Name:',movie_name
        print 'Number of Seats:',MovieTickets.tickets[ticket_id][3]

