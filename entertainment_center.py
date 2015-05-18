#importing fresh_tomatoes to get access to open_movies_page function
import fresh_tomatoes
#importing media to get access to Movie() class
import media

#listing of movie objects/instances for Movie() class 
spiderman = media.Movie("Spider-Man",
                        "A high school student who turns to crimefighting after developing spider-like super powers.",
                        "http://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg",
                        "https://www.youtube.com/watch?v=O7zvehDxttM",
                        "http://www.rottentomatoes.com/m/spiderman/")

spiderman2 = media.Movie("Spider-Man 2",
                        "Set two years after the events of Spider-Man, the film focuses on Peter Parker struggling to manage both his personal life and his duties as Spider-Man, while Dr. Otto Octavius (Doctor Octopus) becomes diabolical following a failed experiment and his wife's death.",
                        "http://upload.wikimedia.org/wikipedia/en/0/02/Spider-Man_2_Poster.jpg",
                        "https://www.youtube.com/watch?v=nbp3Ra3Yp74",
                        "http://www.rottentomatoes.com/m/spiderman_2/")


spiderman3 = media.Movie("Spider-Man 3",
                        "Set months after the events of Spider-Man 2, Peter Parker has become a cultural phenomenon as Spider-Man, while Mary Jane Watson continues her Broadway career.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Spider-Man_3%2C_International_Poster.jpg/220px-Spider-Man_3%2C_International_Poster.jpg",
                        "https://www.youtube.com/watch?v=wPosLpgMtTY",
                        "http://www.rottentomatoes.com/m/spiderman_3/")


iron_man = media.Movie("Iron Man",
                        "Tony Stark, an industrialist and master engineer, builds a powered exoskeleton and becomes the technologically advanced superhero Iron Man.",
                        "http://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://youtu.be/7H0yo-lDuk0",
                        "http://www.rottentomatoes.com/m/iron_man/")


iron_man2 = media.Movie("Iron Man 2",
                        "Six months after the events of Iron Man, Tony Stark is resisting calls by the United States government to hand over the Iron Man technology while also combating his declining health from the arc reactor in his chest.",
                        "http://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
                        "https://www.youtube.com/watch?v=FNQowwwwYa0",
                        "http://www.rottentomatoes.com/m/iron_man_2/")


iron_man3 = media.Movie("Iron Man 3",
                        "Tony Stark tries to recover from posttraumatic stress disorder caused by the events of The Avengers, while investigating a terrorist organization led by the mysterious Mandarin.",
                        "http://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
                        "https://youtu.be/RsxsAN_bsvQ",
                        "http://www.rottentomatoes.com/m/iron_man_3/")

#creating an array of movies
movies = [spiderman, spiderman2, spiderman3, iron_man, iron_man2, iron_man3]
#passing movies array as arguement to open_movies_page function
fresh_tomatoes.open_movies_page(movies)
