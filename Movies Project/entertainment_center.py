import media
import fresh_tomatoes

# despicable me three: movie title, storyline, poater image and trailer
despicable_me_three = media.Movie(
    "Despicable Me 3",
    "Dru has a twin brother and saves the world",
    "https://upload.wikimedia.org/wikipedia/en/9/91/"
    "Despicable_Me_3_%282017%29_Teaser_Poster.jpg",
    "https://www.youtube.com/watch?v=6DBi41reeF0"
    )

# despicable me two: movie title, storyline, poater image and trailer
despicable_me_two = media.Movie(
    "Despicable Me 2",
    "Dru joins the AVL and saves the world",
    "https://upload.wikimedia.org/wikipedia/en/2/29/"
    "Despicable_Me_2_poster.jpg",
    "https://www.youtube.com/watch?v=yM9sKpQOuEw"
    )

# the planet of the apes: movie title, storyline, poater image and trailer
the_planet_of_the_apes = media.Movie(
    "The Planet Of The Apes",
    "It's about monkeys that talk and "
    "protect the land",
    "https://upload.wikimedia.org/wikipedia/en/d/d7/"
    "War_for_the_Planet_of_the_Apes_poster.jpg",
    "https://www.youtube.com/watch?v=UEP1Mk6Un98"
    )

# spider man homecoming: movie title, storyline, poater image and trailer
spider_man_homecoming = media.Movie(
    "Spider-Man homecoming",
    "It's about a man that becomes a spider and "
    "saves people and goes home",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/"
    "Spider-Man_Homecoming_poster.jpg",
    "https://www.youtube.com/watch?v=n9DwoQ7HWvI"
    )

# transformers: movie title, storyline, poater image and trailer
transformers = media.Movie(
    "Transformers",
    "It's about robots fighting other robots"
    "to protect planet earth",
    "http://tfwiki.net/mediawiki/images2/5/50/"
    "Transformersanimatedfilmposter.jpg",
    "https://www.youtube.com/watch?v=6Vtf0MszgP8"
    )

# the legend of bruce lee: movie title, storyline, poater image and trailer
the_legend_of_bruce_lee = media.Movie(
    "The Legend of Bruce Lee",
    "It's a true life story of Bruce Lee",
    "https://upload.wikimedia.org/wikipedia/en/1/1d/"
    "The_Legend_of_Bruce_Lee_poster.jpg",
    "https://www.youtube.com/watch?v=va3DwaVafN8"
    )

# Adding objects into a array
movies = [
    despicable_me_three,
    despicable_me_two,
    the_planet_of_the_apes,
    spider_man_homecoming,
    transformers,
    the_legend_of_bruce_lee
    ]

# calling open_movies_page() passing in the array
fresh_tomatoes.open_movies_page(movies)
