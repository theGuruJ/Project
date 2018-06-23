from model import MovieTickets
from modifiedVIEW import View
import json

movie_details = MovieTickets.get_movie_details()
print View.display_movies(movie_details)


movies = {1: 10,
          2: 75,
          3: 0,
          4: 100,
          5: 100}

movie_str = json.dumps(movies)


def get_movie_selection(select_test, no_of_movies):
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


print get_movie_selection(3,movie_str)