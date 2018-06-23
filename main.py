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


# class Greeting(db.Model):
#     """Models an individual Guestbook entry with an author, content, and date."""
#     author = db.UserProperty()
#     content = db.StringProperty(multiline=True)
#     date = db.DateTimeProperty(auto_now_add=True)

# def guestbook_key(guestbook_name=None):
#     """Constructs a datastore key for a Guestbook entity with guestbook_name."""
#     return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')


class MainPage(webapp2.RequestHandler):
    def get(self):
        details = MovieTickets.movies
        print details

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.headers['content-type'] = 'text/json'
        self.response.out.write(template.render(path, details))

        # guestbook_name=self.request.get('guestbook_name')
        # greetings_query = Greeting.all().ancestor(
        #     guestbook_key(guestbook_name)).order('-date')
        # greetings = greetings_query.fetch(10)

# Start of current version of app

        # if users.get_current_user():
        #     url = users.create_logout_url(self.request.uri)
        #     url_linktext = 'Logout'
        # else:
        #     url = users.create_login_url(self.request.uri)
        #     url_linktext = 'Login'



        # movie_details = MovieTickets.get_movie_details()

        # print movie_details

        # template_values = {
        #     # 'greetings': greetings,
        #     'url': url,
        #     'url_linktext': url_linktext,
        #     'movies': movie_details,
        # }

        # path = os.path.join(os.path.dirname(__file__), 'index.html')
        # self.response.out.write(template.render(path, template_values))

# end of current version of app!

    # Ancestor Queries, as shown here, are strongly consistent with the High
    # Replication datastore. Queries that span entity groups are eventually
    # consistent. If we omitted the ancestor from this query there would be a
    # slight chance that Greeting that had just been written would not show up
    # in a query.



# class Guestbook(webapp2.RequestHandler):
#     def post(self):
    # We set the same parent key on the 'Greeting' to ensure each greeting is in
    # the same entity group. Queries across the single entity group will be
    # consistent. However, the write rate to a single entity group should
    # be limited to ~1/second.
        # guestbook_name = self.request.get('guestbook_name')
        # greeting = Greeting(parent=guestbook_key(guestbook_name))

        
        # if users.get_current_user():
        #     greeting.author = users.get_current_user()

        # greeting.content = self.request.get('content')
        # greeting.put()
        # self.redirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))

# new code again
        # movie_select =  int(self.request.get('movieselect'))
        # movie_name = MovieTickets.get_movie_name(movie_select)
        # no_of_seats = MovieTickets.no_of_seats_available(movie_select)
        # no_of_seats = min(no_of_seats,6)



        # movie_selection = {
        #     "movie_info" : { "mov_select" : movie_select,
        #                      "mov_name" : movie_name,
        #                      "no_of_seats" : no_of_seats, }
        # }


        # print movie_selection

        # path = os.path.join(os.path.dirname(__file__), 'bookticket.html')
        # self.response.out.write(template.render(path, movie_selection))

#new code till above
#activate this as well to revert to current version
# class BookTicket(webapp2.RequestHandler):
#     def post(self):

#         name_of_booker = self.request.get('bname')
#         email = self.request.get('email')
#         phone_number = self.request.get('phonenumber')
#         no_of_seats = self.request.get('no_of_seats')
#activate till above

        # greeting = Greeting(parent=guestbook_key(guestbook_name))

        # if users.get_current_user():
        #     greeting.author = users.get_current_user()

        # greeting.content = self.request.get('content')
        # greeting.put()
        # self.redirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))


application = webapp2.WSGIApplication([
    ('/',MainPage),
    # ('/',Guestbook),
    # ('/bookticket', BookTicket),
], debug=True)

def main():
    application.run()

if __name__ == "__main__":
    main()
