import webapp2
import cgi
import urllib
import wsgiref.handlers
import os
import datetime
import json


from my_db import Session as Session
from my_db import Customers as Customers
from my_db import Tickets as Tickets
from my_db import MovieDetails as MovieDetails
from my_db import MovieScreeningDates as MovieScreeningDates
from my_db import MovieScreeningTimes as MovieScreeningTimes


from google.appengine.ext.webapp import template
from google.appengine.ext import ndb


class MainPage(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(template.render(path, {}))


class AddMovie((webapp2.RequestHandler)):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'addmovie.html')
        self.response.write(template.render(path, {}))

    def post(self):
        input_date = self.request.POST
        print input_date
        key_from_put = MovieDetails.add_movie(input_date)
        print key_from_put
        what_happened = {'Key_ID': key_from_put}
        self.response.write(json.dumps(what_happened))


class Movies(webapp2.RequestHandler):
    def get(self):
        print self.request
        output_data = MovieDetails.get_movie_listings()

        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(output_data)

    def post(self):
        input_date = json.loads(self.request.body)
        print input_date
        key_from_put = MovieDetails.add_movie(input_date)
        print key_from_put
        what_happened = {'Key_ID': key_from_put}
        self.response.write(json.dumps(what_happened))

    def put(self):
        pass



class NoOfSeatsAvail(webapp2.RequestHandler):
    def post(self):
        input_data = json.loads(self.request.body)
        print input_data
        # selected_movie_id = int(input_data.get('movie_name'))
        # print MovieDetails.get_movie_name(selected_movie_id)

        movie_key = ndb.Key("MovieDetails", selected_movie_id)
        no_of_seats_avail = movie_key.get()
        self.response.headers['Content-Type'] = 'application/json'
        output_data = {"no_of_seats": no_of_seats_avail.available_seats}
        self.response.write(json.dumps(output_data))


class Tickets(webapp2.RequestHandler):
    def get(self):
        '''
        return tickets based on criteria tbd
        :return:
        '''


    def post(self):
        input_data = json.loads(self.request.body)
        print input_data

        customer_key = input_data.get('customer_key')

        email_address = str(input_data.get('email'))

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



class Customers_handler(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'register.html')
        self.response.write(template.render(path, {}))

    def post(self):
        input_data = json.loads(self.request.body)
        email_address = input_data['email_address']
        # print Customers.query(Customers.identifier == email_address).fetch()

        password = input_data['password']
        customer_name = input_data['customer_name']
        phone_number = str(input_data['phone_number'])
        customer_key = Customers.create_customer(email_address, password, customer_name, phone_number)
        print customer_key
        session_id = str((Session.set_session({'customer_name': customer_name, 'email_address': email_address})).id())
        print session_id
        if customer_key:
            self.response.set_cookie('session_id', session_id, max_age=1800)
            self.response.write(json.dumps({'status': 'succeeded'}))
        else:
            self.response.write(json.dumps({'status': 'failed'}))


class Login(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'login.html')
        self.response.write(template.render(path, {}))
    
    def post(self):
        input_data = json.loads(self.request.body)
        print "Main.py - line 174"
        print input_data
        customer = Customers.is_customer(**input_data)
        print "Main.py - line 177"
        print customer
        if customer.get('status') == "Valid Customer":
            customer_info = {
                'customer_name': customer.get('customer').get('customer_name'),
                'email_address': customer.get('customer').get('email_address')
            }
            session_key = Session.set_session(customer_info)
            print "Main.py - line 181"
            print session_key
            session_id = str(session_key.id())
            print "Main.py - line 184"
            print session_id
            self.response.set_cookie('session_id', session_id, max_age=1800)
            self.response.write(json.dumps({'status': 'login successful'}))
        else:
            self.response.write(json.dumps({'status': customer.get('status')}))

class Register(webapp2.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'register.html')
        self.response.write(template.render(path, {}))

    def post(self):
        input_data = json.loads(self.request.body)
        email_address = input_data.get('email_address')
        customer_name = input_data.get('customer_name')
        print input_data
        customer = json.loads(Customers.create_customer(**input_data))
        if customer.get("status") == "customer created":
            customer_info = {
                'customer_name': customer_name,
                'email_address': email_address
            }
            session_key = Session.set_session(customer_info)
            print session_key
            session_id = str(session_key.id())
            print "Main.py - line 184"
            print session_id
            self.response.set_cookie('session_id', session_id, max_age=1800)
            self.response.write(json.dumps({'status': 'registration successful, logged in'}))
        else:
            self.response.write(json.dumps({'status': 'Email already registered, please login'}))



class Screenings(webapp2.RequestHandler):
    def get(self, mov_id=None):
        print mov_id
        self.request.headers.get('Content_Type')

        if self.request.headers.get('Content_Type') == "application/json":
            screenings = MovieScreeningTimes.get_screening_times(mov_id)
            self.response.write(screenings)
        else:
            path = os.path.join(os.path.dirname(__file__), 'screenings.html')
            self.response.write(template.render(path, {}))

    def post(self):
        input_data = {key: value for (key, value) in self.request.POST.items()}
        print input_data
        a, b, c = input_data
        print input_data[a]
        print input_data[b]
        print input_data[c]
        screening = MovieScreeningTimes.add_movie_screening_times(**input_data)
        self.response.write(screening)


application = webapp2.WSGIApplication([
    webapp2.Route('/',MainPage),
    webapp2.Route('/movies', Movies),
    webapp2.Route('/query/no_of_seats_avail', NoOfSeatsAvail),
    webapp2.Route('/tickets', Tickets),
    webapp2.Route('/customers', Customers_handler),
    webapp2.Route('/register', Register),
    webapp2.Route('/login', Login),
    webapp2.Route('/add_movie', AddMovie),
    webapp2.Route('/screenings/<:\S+>', Screenings),
    webapp2.Route('/screenings', Screenings),

], debug=True, )

# def main():
#     application.run()
#
# if __name__ == "__main__":
#     main()
