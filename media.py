import webbrowser


# class header
class Movie():
    '''constructor for a movie object, which takes in a movie title,
       the image url, and the trailer url as parameters'''
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
