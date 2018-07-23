from unittest import *
from my_db import MovieTickets
from modifiedVIEW import View
import json
import itertools


class Test(TestCase):

    # def test_no_of_movies(self):
    #     self.assertEqual(MovieTickets.no_of_movies(), movie_str)

    def test_get_movie_details(self):
        self.assertEqual(MovieTickets.get_movie_details(),movie_json_format)

    def test_no_of_seats_available(self):
        for x,y in movies.items():
            self.assertEqual(MovieTickets.no_of_seats_available(x),y)

    def test_get_movie_name(self):
        for x,y in movies2.items():
            self.assertEqual(MovieTickets.get_movie_name(x),y)

    def test_display_movies(self):
        self.assertEqual(View.display_movies(movie_json_format),print_result)

    # def test_get_movie_selection_1(self):
    #     self.assertEqual(View.get_movie_selection('~',movie_str),"Not a valid input, Please try again...")
    #
    # def test_get_movie_selection_2(self):
    #     self.assertEqual(View.get_movie_selection('`',movie_str),"Not a valid input, Please try again...")
    #
    # def test_get_movie_selection_3(self):
    #     self.assertEqual(View.get_movie_selection('A',movie_str),"Not a valid input, Please try again...")
    #
    # def test_get_movie_selection_4(self):
    #     self.assertEqual(View.get_movie_selection('z',movie_str),"Not a valid input, Please try again...")
    #
    # def test_get_movie_selection_5(self):
    #     self.assertEqual(View.get_movie_selection('0',movie_str),"Please make a valid selection!")
    #
    # def test_get_movie_selection_6(self):
    #     self.assertEqual(View.get_movie_selection('9',movie_str),"Please make a valid selection!")
    #
    # def test_get_movie_selection_7(self):
    #     self.assertEqual(View.get_movie_selection('34',movie_str),"Please make a valid selection!")
    #
    # def test_get_movie_selection_8(self):
    #     self.assertEqual(View.get_movie_selection('1',movie_str),1)
    #
    # def test_get_movie_selection_9(self):
    #     self.assertEqual(View.get_movie_selection('5',movie_str),5)
    #
    # def test_get_movie_selection_10(self):
    #     self.assertEqual(View.get_movie_selection('3',movie_str),"No seats available, select another movie!")


# movie_selection_in = ['`','~','E','a','0','9','12','1','2','3','4','5']
#
# movie_selection_out = ["No seats available, select another movie!","Please make a valid selection!","Not a valid input, Please try again...",1,2,3,4,5]

movie_details = {1: ['Avengers: Infinity Wars', 10, 0,[]],
                 2: ['Deadpool 2', 75, 0,[]],
                 3: ['Jurassic World', 0, 0,[]],
                 4: ['Kaala', 100, 0, []],
                 5: ['Veere Di Wedding', 100, 0, []],}

movie_json_format = json.dumps(movie_details)

movies = {'Jurassic World': 100,
          'Kaala': 100,
          'Avengers Infinity Wars': 4,
          'Veere Di Wedding': 10,
          'Deadpool 2': 75}


# movies = {1: 10,
#           2: 75,
#           3: 0,
#           4: 100,
#           5: 100}

movie_str = json.dumps(movies)

movies2 = {1: 'Avengers: Infinity Wars',
           2: 'Deadpool 2',
           3: 'Jurassic World',
           4: 'Kaala',
           5: 'Veere Di Wedding'
           }

print_result = '\nThe available movies are listed below!\nS. No.  Name                          No. Of Seats Available\n1       Avengers: Infinity Wars       10   \n2       Deadpool 2                    75   \n3       Jurassic World                0    \n4       Kaala                         100  \n5       Veere Di Wedding              100  '

suite = TestLoader().loadTestsFromTestCase(Test)
TextTestRunner(verbosity=2).run(suite)

