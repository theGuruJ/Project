
class MovieTickets(object):

    movies = {1: ['Avengers: Infinity Wars', 10, 0,[]],
              2: ['Beyond The Clouds', 75, 0,[]],
              3: ['Nanu Ki Jaanu', 100, 0,[]]}
    tickets = {}

    ticket_id = 11
    def no_of_movies(self):
        return len(self.movies)

    def no_of_seats_available(self, movie_selection):
        return self.movies[movie_selection][1]

    def display_movies(self):
        print '\n'
        print("The available movies are listed below!")
        print '%-8s%-30s%-5s' % ('S. No.', 'Name', 'No. Of Seats Available')
        for e in range(1,len(self.movies)+1):
            print '%-8s%-30s%-5i' % (e,self.movies[e][0],self.movies[e][1])
        #The serial numbers on the list of movies correspond to S. No. - 1 on the index value in the list of movies list.
        #Hence the selection subtracts one from the serial number that is input by the user.

    def get_movie_name(self, movie_selection):
        return self.movies[movie_selection][0]
    '''
    provides for a way to store and retrieve details of tickets issued
    uses a dictionary structure.
    {   ticket ID: [Movie Serial Number(int),
                    Customer name (Str),
                    The number of Seats(int, max of 6, no more per booking.
                    The phone number (10 digit numeric number}

    '''

    def print_a_ticket(self,ticket_id,movie_name):
        print '   Ticket No:',ticket_id
        print '        Name:',self.tickets[ticket_id][1]
        print 'Phone Number:',self.tickets[ticket_id][2]
        print ' Movie Name:',movie_name
        print 'Number of Seats:',self.tickets[ticket_id][3]

    def book_a_ticket(self,movie_selection,name_of_booker,phone_number,number_of_seats_booked):
        self.tickets[self.ticket_id] = [movie_selection,name_of_booker,phone_number,number_of_seats_booked]
        self.movies[movie_selection][1] -= number_of_seats_booked
        self.movies[movie_selection][2] += number_of_seats_booked
        self.movies[movie_selection][3].append(self.ticket_id)
        self.ticket_id += 1
        print("Ticket Booked")
        return self.ticket_id - 1
