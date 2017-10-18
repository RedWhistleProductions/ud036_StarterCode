import webbrowser

class Movie():
    '''For use with the fresh_tomatoes library created by Kunal at Udacity.com
    This is a storage container for movie data to be which is used on the fresh tomatoes web page.
    Additionaly the show_trailer method can be called to open the trailer's webpage.

    movie_title (str) name of the movie as it will appear on the page
    movie_storyline (str) IMDB.com description of the Movie
    poster_image_url (str) poster image link
    trailer_youtube_url (str) link to the video on youtube
    '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)