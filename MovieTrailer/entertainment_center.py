from modules import process_data
from modules import process_wiki
from modules import create_html
from objects import media
import sys

# read data file and get list of movies
print()
print ('Opening movie data file and processing data...')
print()
list_of_movies = process_data.get_list_of_movies()
if len(list_of_movies) <= 0:
    print("No movies found in file")
    quit()

# read data file and get list of youtube trailer id
list_of_trailers = process_data.get_list_of_trailers()
if len(list_of_trailers) <= 0:
    print("No trailers found in file")
    quit()

# for each movie, get summary, box art url and youtube trailer id
print ('Making API call to get all movies storyline and box art url...')
movie_obj_list = []
for index, movie_name in enumerate(list_of_movies):
    if movie_name == "Storks":
        local_movie_name = "Storks (film)"
    elif movie_name == "Moana":
        local_movie_name = "Moana (2016 film)"
    else:
        local_movie_name = movie_name

    storyline = process_wiki.get_wiki_summary_for_movie(local_movie_name)
    box_art_url = process_wiki.get_wiki_box_art_url_for_movie(local_movie_name)

    # use loop counter to get corresponding youtube trailer id
    trailer_url = 'https://www.youtube.com/watch?v='+list_of_trailers[index]
    movie_obj = media.Movie(movie_name, storyline, box_art_url, trailer_url)
    movie_obj_list.append(movie_obj)

create_html.open_movies_page(movie_obj_list)
