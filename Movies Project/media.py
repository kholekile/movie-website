import webbrowser


class Movie():
    '''
    This class provides a way to store a
    movie and its related information
    '''
    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        '''
        This is the constructor method and its used to construct
        or initailise the variable of this Movie class
        '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_tailer(self):
        ''' This is a method method used to show a trailer of a movie '''
        webbrowser.open(self.trailer_youtube_url)
