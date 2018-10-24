

# movies model
#
# key
# name - string
# capacity - integer
# available seats - integer
# booked seats - integer
#
#
# tickets
# 	key -
# 	movie selection - key of the movie?
# 	user ID - Key of the user entry?
# 	number_of_seats_booked - integer
#
# user db:
# 	key -
# 	name - string
# 	email address - string
# 	phone number - integer
#

import json
from google.appengine.ext import ndb
from datetime import datetime


class Session(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @staticmethod
    def set_session(user_data):
        existing_sessions = Session.query(Session.email == user_data.get('email_address')).get()
        if existing_sessions is not None:
            existing_sessions.date = datetime.now()
            existing_sessions.put()
            return existing_sessions.key
        else:
            return Session(name=user_data.get('customer_name'), email=user_data.get('email_address')).put()


class MovieDetails(ndb.Model):
    movie_name = ndb.StringProperty()
    capacity = ndb.IntegerProperty()
    available_seats = ndb.IntegerProperty()
    booked_seats = ndb.IntegerProperty()
    movie_status = ndb.StringProperty()
    screening_end_date = ndb.StringProperty()

    @staticmethod
    def get_movie_name(movie_name):
        return MovieDetails.query(MovieDetails.movie_name == movie_name).get().movie_name

    @staticmethod
    def get_movie_listings():
        movie = MovieDetails.query().fetch()
        details = {}
        for each in movie:
            details.update({
                each.key.id(): {"name": each.movie_name,
                             "avail_seats": each.available_seats}
            })
        return json.dumps(details)

    @staticmethod
    def add_movie(details):
        movie = MovieDetails(
            movie_name=details.get('movie_name'),
            capacity=int(details.get('capacity')),
            available_seats=int(details.get('available_seats')),
            booked_seats=int(details.get('booked_seats')),
            movie_status=details.get('movie_status'),
            screening_end_date=details.get('screening_end_date')
            )
        return movie.put().urlsafe()


class Customers(ndb.Model):
    username = ndb.StringProperty()
    password = ndb.StringProperty()
    customer_name = ndb.StringProperty()
    email_address = ndb.StringProperty()
    phone_number = ndb.StringProperty()

    @staticmethod
    def create_customer(email_address, password, customer_name, phone_number):
        customer_query = Customers.query(Customers.email_address == email_address).get()
        if customer_query is not None:
            c_key = customer_query.key
            output = {"status": "customer already exists",
                      "key": c_key.urlsafe()}
            return json.dumps(output)
        else:
            customer = Customers(
            username=email_address,
            password=password,
            customer_name=customer_name,
            email_address=email_address,
            phone_number=phone_number
            )
            c_key = customer.put()
            output = {"status": "customer created",
                      "key": c_key.urlsafe()}

            return json.dumps(output)

    @staticmethod
    def get_customer(customer_key):
        c_key = ndb.Key(urlsafe=customer_key)
        customer = c_key.get()
        output = {}
        if customer is not None:
            output['status'] = "Customer Exists"
            output['key'] = customer.key.urlsafe()
            return json.dumps(customer)
        else:
            return "not a customer"

    @staticmethod
    def is_customer(email_address, password):
        customer = Customers.query(Customers.username == email_address).get()
        print password
        print customer

        if customer is not None:
            if password == customer.password:
                return {
                        "status": "Valid Customer",
                        "customer": customer.to_dict()
                        }
            else:
                return {
                        "status": "Invalid Password"
                        }
        else:
            return {
                        "status": "Invalid Username"
                        }


class MovieScreeningDates(ndb.Model):
    movie_identifier = ndb.KeyProperty(kind=MovieDetails)
    screening_date = ndb.StringProperty()

    @staticmethod
    def create_movie_screening(movie_identifier, screening_date):
        print movie_identifier
        print screening_date
        m_key = ndb.Key(urlsafe=movie_identifier)
        movie_screening = MovieScreeningDates(
            movie_identifier=m_key,
            screening_date=screening_date,
        )
        return movie_screening.put().urlsafe()

    @staticmethod
    def get_screening_dates(mov_id):
        movie_key = ndb.Key(MovieDetails, int(mov_id))
        query_result = MovieScreeningDates.query(MovieScreeningDates.movie_identifier == movie_key).fetch(projection=[MovieScreeningDates.screening_date])
        if query_result is not None:
            output = {}
            for each in query_result:
                output.update({each.key.urlsafe(): each.to_dict()})
            # for each in output:
            #     output[each]['movie_identifier'] = output[each]['movie_identifier'].urlsafe()
            print output
            return json.dumps(output)
        else:
            return "invalid movie selection"

class MovieScreeningTimes(ndb.Model):
    movie_identifier = ndb.KeyProperty(kind=MovieDetails)
    screening_date = ndb.StringProperty()
    screening_time = ndb.StringProperty()

    @staticmethod
    def add_movie_screening_times(movie_identifier, screening_date, screening_time):
        print movie_identifier
        print screening_date
        print screening_time
        m_key = ndb.Key(urlsafe=movie_identifier)
        movie_screening = MovieScreeningTimes(
            movie_identifier=m_key,
            screening_date=screening_date,
            screening_time=screening_time
        )
        return movie_screening.put().urlsafe()



    @staticmethod
    def get_screening_times(mov_id):
        movie_key = ndb.Key(MovieDetails, int(mov_id))
        query_result = MovieScreeningTimes.query(MovieScreeningTimes.movie_identifier == movie_key).fetch()
        if query_result is not None:
            output = {}
            for each in query_result:
                output.update({each.key.urlsafe(): each.to_dict()})
            for each in output:
                output[each]['movie_identifier'] = output[each]['movie_identifier'].urlsafe()
            print output
            return json.dumps(output)
        else:
            return "invalid movie selection"


class Tickets(ndb.Model):
    movie_selection = ndb.KeyProperty(kind=MovieDetails)
    screening = ndb.KeyProperty(kind=MovieScreeningTimes)
    customer_id = ndb.KeyProperty(kind=Customers)
    no_of_seats_booked = ndb.IntegerProperty()

    @staticmethod
    def create_ticker(movie_key, screening_key, customer_key, no_of_seats):
        ticket = Tickets(
            movie_selection=movie_key,
            screening=screening_key,
            customer_id=customer_key,
            no_of_seats_booked=no_of_seats
        )
        ticket_key = ticket.put()
        return ticket_key


