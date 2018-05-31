import media
import fresh_tomatoes

DEADPOOL2= media.Movie("Deadpool 2",
                      "A story of Stars Would Audition for X-Force",
                      "https://s3.amazonaws.com/ffe-ugc/intlportal2/dev-temp/en-US/__5afdb4c667023.jpg",
                      "https://www.youtube.com/watch?v=D86RtevtfrA")

GUARDIANS= media.Movie("GUARDIANS",
                      "Russia's Superhero Squad to the Rescue",
                      "https://i.ytimg.com/vi/LHoxuW01heg/maxresdefault.jpg",
                      "https://www.youtube.com/watch?v=LHoxuW01heg")

Transformer5= media.Movie("Transformer 5",
                          "Transformers is a series of American science fiction fantasy action films based on the toys",
                          "https://i.ytimg.com/vi/R17_mrSyuBU/maxresdefault.jpg",
                          "https://www.youtube.com/watch?v=cSUx0ZB6HrM")

The_Dark_Tower= media.Movie("The Dark Tower",
                      "One Sworn to Protect It. One Sworn to Destroy It",
                      "https://i.ytimg.com/vi/JlgyYb14O6Q/maxresdefault.jpg",
                      "https://www.youtube.com/watch?v=4C0A2GpMNP8")

KILL_SWITCH= media.Movie("KILL SWITCH",
                      "A story of Stars Would Audition for X-Force",
                      "https://upload.wikimedia.org/wikipedia/en/9/92/Kill_Switch_2017_film.jpg",
                      "https://www.youtube.com/watch?v=SernjeZIsM8")

Infinity_War= media.Movie("Avengers: Infinity War",
                      "A war to save a galaxy",
                      "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                      "https://www.youtube.com/watch?v=6ZfuNTqbHE8")


#incredible2=media.Movie()
#print (deadpool2.storyline)
#deadpool2.show_trailer()
movies =[DEADPOOL2,GUARDIANS,Transformer5,The_Dark_Tower,KILL_SWITCH,Infinity_War]
fresh_tomatoes.open_movies_page(movies)
