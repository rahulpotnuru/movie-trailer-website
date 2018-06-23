import webbrowser


class Movie():
    '''This class stores the information related to a movie.'''
    def __init__(self, name, storyline, poster_image, trailer_link):
        '''Function:
            Initialises the instance attributes
           Args:
            (obj)self - calling object
            (str)movie_name - name of the movie
            (str)movie_storyline - story line of the movie
            (str)movie_poster_image - poster image of the movie
            (str)trailer_youtube_url - link of the movie trailer
          Returns:
            None'''
        self.title = name
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_link

    def show_trailer(self):
        '''Function:
            Plays the trailer of the movie in the webbrowser
           Args:
            (obj)self - calling object
           Returns:
            None'''
        webbrowser.open(self.trailer_youtube_url)
