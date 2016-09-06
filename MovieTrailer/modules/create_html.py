import webbrowser
import os
import re

from modules import html_contents


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += html_contents.movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            box_art_url=movie.box_art_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('animation_movies_2016.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = html_contents.main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(html_contents.main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
