import webapp2
import cgi
import urllib
import wsgiref.handlers
import os
import datetime
import json


from view import View as View
from my_db import MovieTickets as MovieTickets
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        details = {
            "key" : "value"
        }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.write(template.render(path, details))


class GetMovieDetails(webapp2.RequestHandler):
    def get(self):
        details = MovieTickets.get_movie_details()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(details)

class NoOfSeatsAvail(webapp2.RequestHandler):
    def post(self):

        movie_selection = json.loads(self.request.body)
        print movie_selection
        #no_of_tickets = MovieTickets.no_of_seats_available(movie_selection)
        self.response.headers['Content-Type'] = 'application/json'
        data_to_send = {"movie_selection": movie_selection}
        print data_to_send
        self.response.write(data_to_send)

application = webapp2.WSGIApplication([
    ('/',MainPage),
    ('/display_movie', GetMovieDetails),
    ('/no_of_seats_avail', NoOfSeatsAvail),
    # ('/bookticket', BookTicket),
], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()
