# importing webbrowser module to use for playing youtube video
import webbrowser


class Movie():
    # creating/initializing space in memory for movie details data
    """ This class provides a way store movie related information """

    def __init__(
        self, movie_title, movie_storyline, poster_image, trailer_youtube,
            rotten_page):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rotten = rotten_page

    # calling webbrowser.open and creating/initializing space in memory to
    # link to youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
