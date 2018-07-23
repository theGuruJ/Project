import webapp2
import cgi
import urllib
import wsgiref.handlers
import os
import datetime
import json


from view import View as View
from my_db import MovieTickets as MovieTickets # old db model based on dict
from my_db import Customers as Customers
from my_db import Session as Session
from my_db import Tickets as Tickets
from my_db import MovieDetails as MovieDetails
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.ext import ndb


class MainPage(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(template.render(path, {}))


class GetMovieDetails(webapp2.RequestHandler):
    def get(self):
        movie = MovieDetails.query().fetch()
        print movie
        details = {}
        for n in movie:
            details.update({
                n.key.id(): {"name": n.movie_name,
                             "avail_seats": n.available_seats}
            })
            print n.key.id()
            print n.movie_name
            print n.available_seats
        print details

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(details))


class NoOfSeatsAvail(webapp2.RequestHandler):
    def post(self):
        input_data = json.loads(self.request.body)
        # print input_data
        selected_movie_id = int(input_data.get('movie_name'))
        print MovieDetails.get_movie_name(selected_movie_id)

        # selected_movie_id_s = str(input_data.get('movie_name'))
        # print selected_movie_id
        movie_key = ndb.Key("MovieDetails", selected_movie_id)
        # print movie_key
        # print type(movie_key)
        no_of_seats_avail = movie_key.get()
        # print no_of_seats_avail.available_seats
        # no_of_tickets = MovieTickets.no_of_seats_available(movie_selection)
        self.response.headers['Content-Type'] = 'application/json'
        data_to_send = {"no_of_seats": no_of_seats_avail.available_seats}
        # print data_to_send
        self.response.write(json.dumps(data_to_send))


class BookTicket(webapp2.RequestHandler):
    def post(self):
        input_data = json.loads(self.request.body)
        print input_data
        # {u'movie_name': u'4785074604081152', u'email': u'email@email.com', u'name': u'afdsg', u'noOfSeats': u'5',
        #  u'phoneNumber': u'3456'}
        #
        # class Customers(ndb.Model):
        #     customer_name = ndb.StringProperty()
        #     email_address = ndb.StringProperty()
        #     phone_number = ndb.IntegerProperty()

        email_address = str(input_data.get('email'))
        if not ndb.Key("Customers", email_address).get():

            customer = Customers()
            customer.customer_name = str(input_data.get('name'))
            customer.phone_number = int(input_data.get('phoneNumber'))
            customer.username = str(input_data.get('email'))
            customer.password = 'temp'
            customer_key = customer.put()
        else:
            customer_key = ndb.Key("Customers", email_address)

        selected_movie_id = int(input_data.get('movie_name'))
        movie_key = ndb.Key("MovieDetails", selected_movie_id)
        movie_entity = movie_key.get()

        ticket = Tickets()
        ticket.movie_selection = movie_key
        ticket.customer_id = customer_key
        ticket.no_of_seats_booked = int(input_data.get('noOfSeats'))
        ticket_key = ticket.put()

        ticket_id = ticket_key.id()
        movie_entity.available_seats -= int(input_data.get('noOfSeats'))
        movie_entity.booked_seats += int(input_data.get('noOfSeats'))
        movie_entity.put()
        ticket_output = {"output": ticket_id}
        self.response.write(json.dumps(ticket_output))


class AddMovie(webapp2.RequestHandler):
    def get(self):
        movie = MovieDetails()
        # list_of_movies = movie.get()
        details = {
            'Movies': "list_of_movies"
        }
        path = os.path.join(os.path.dirname(__file__), 'addMovie.html')
        print path
        self.response.write(template.render(path, details))

    def post(self):
        movie_name = self.request.POST['movie_name']
        print movie_name
        capacity = int(self.request.POST['capacity'])
        print capacity
        available_seats = int(self.request.POST['available_seats'])
        print available_seats
        booked_seats = int(self.request.POST['booked_seats'])
        print booked_seats
        movie = MovieDetails()
        movie.movie_name = movie_name
        movie.capacity = capacity
        movie.available_seats = available_seats
        movie.booked_seats = booked_seats
        key_from_put = movie.put()
        print type(key_from_put)
        key_from_put = str(key_from_put)
        print key_from_put
        what_happened = {'Key_ID': key_from_put}
        self.response.write(json.dumps(what_happened))


class Register(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'signup.html')
        self.response.write(template.render(path, {}))

    def post(self):
        input_data = json.loads(self.request.body)
        email_address = input_data['email_address']
        # print Customers.query(Customers.identifier == email_address).fetch()

        print ndb.Key("Customers", email_address).get()
        password = input_data['password']
        customer_name = input_data['customer_name']
        phone_number = int(input_data['phone_number'])
        customer_key = Customers.create_customer(email_address, password, customer_name, phone_number)
        session_id = str((Session.set_session({'name': customer_name, 'email': email_address})).id())
        print session_id
        if customer_key:
            self.response.set_cookie('session_id', session_id)
            self.response.write(json.dumps({'status': 'succeeded'}))
        else:
            self.response.write(json.dumps({'status': 'failed'}))


class SignIn(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'signup.html')
        self.response.write(template.render(path, {}))
    
    def post(self):
        pass


class EditMovie(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'edit_movie.html')
        self.response.write(template.render(path, {}))

    def post(self):
        movie = MovieDetails.query().fetch()
        print movie
        details = {}

        for n in movie:
            details.update({
                n.key.id(): {"name": n.movie_name,
                             "avail_seats": n.available_seats}
            })
        #     print n.key.id()
        #     print n.movie_name
        #     print n.available_seats
        # print details

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(details))


application = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/display_movie', GetMovieDetails),
    ('/no_of_seats_avail', NoOfSeatsAvail),
    ('/book_ticket', BookTicket),
    ('/add_movie', AddMovie),
    ('/register', Register),
    ('/signin', SignIn),
    ('/edit_movie', EditMovie),

], debug=True, )

def main():
    application.run()

if __name__ == "__main__":
    main()