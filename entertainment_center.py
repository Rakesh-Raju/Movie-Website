import media
import fresh_tomatoes

'''a block that creates a few instance of movie objects,
which pass in the proper parameters defined in media.py'''

avatar = media.Movie("Avatar",
                     "http://s3.foxmovies.com/foxmovies/production/films/18/images/posters/251-asset-page.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

toy_story = media.Movie("Toy Story",
                        "http://thegeekchurch.com/wp-content/uploads/2014/05/Toy-Story-DVD95.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

pirates_carribean = media.Movie("Pirates of the Carribean:\nThe Curse of the Black Pearl",  # NOQA
                                "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-nie8b7_49ceb417.jpeg?region=0%2C0%2C300%2C450",  # NOQA
                                "https://www.youtube.com/watch?v=naQr0uTrH_s")


# creates a list of movies that were previously defined
movielist = [avatar, toy_story, pirates_carribean]


'''uses the open_movies_page function of the provided fresh_tomatoes.py module,
using the movielist previously initialized as a paramater'''
fresh_tomatoes.open_movies_page(movielist)
