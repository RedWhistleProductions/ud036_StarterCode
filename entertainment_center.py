import fresh_tomatoes #fresh_tomatoes was created by Adarsh Nair at Udacity.com
from media import Movie

'''
    This file instatiates 6 instances of the movie class and puts them in a 
    list and calls the openMovies page from fresh_tomatoes.py which generates
    and loads the web page freshtomatoes.html
'''

toy_story = Movie("Toy Story",
                    "A story of a boy and his toys that come to life",
                    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
                    "https://youtu.be/KYz2wyBy3kc")

last_samurai = Movie("The Last Samurai", 
                    '''An American military advisor embraces the Samurai culture 
                    he was hired to destroy after he is captured in battle''', 
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMzkyNzQ1Mzc0NV5BMl5BanBnXkFtZTcwODg3MzUzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                    "https://youtu.be/T50_qHEOahQ")

aladdin = Movie("Aladdin",
                    '''When a street urchin vies for the love of a beautiful
                    princess, he uses a genie's magic power to make himself off
                    as a prince in order to marry her.''',"https://t2.gstatic.com/images?q=tbn:ANd9GcSsSEOwh6rx0SSBgd5IHoAZMaU3jLtyxMfFbtfJFTjc-SYHsFQL","https://youtu.be/gWLa6y7Z2TE")

guardians = Movie("Guardians of The Galaxy",
                    '''A group of intergalactic criminals are forced to work
                    together to stop a fanatical warrior from taking control of
                    the universe.''',
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                    "https://youtu.be/d96cjJhvlMA")

lion_king = Movie("The Lion King",
                    '''Lion cub and future king Simba searches for his identity.
                    His eagerness to please others and penchant for testing his
                    boundaries sometimes gets him into trouble. ''',
                    "http://cdn1.gomoviesgo.com/movies/1230110357-poster-The-Lion-King.jpg",
                    "https://youtu.be/4sj1MT05lAA")

the_matrix = Movie("The Matrix",
                    "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                    "https://images-na.ssl-images-amazon.com/images/I/51EG732BV3L.jpg",
                    "https://youtu.be/Q8g9zL-JL8E")

fresh_tomatoes.open_movies_page([aladdin, guardians, last_samurai, lion_king, the_matrix, toy_story])