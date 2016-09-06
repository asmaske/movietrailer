import csv

MOVIE_LIST_FILENAME = "MovieList.csv"


def get_list_of_movies():
    """
        List of movies specified in movie list file

        Returns:
            An array list of movie names
            example:
            ['Storks']
        Exception:
            IOError: quits program if movie list file nor found
        """
    list_of_names = []

    try:
        with open(MOVIE_LIST_FILENAME) as movie_list_file:
            file_reader = csv.reader(movie_list_file, delimiter=',')
            for row in file_reader:
                list_of_names.append(row[0])
    except IOError:
        print(MOVIE_LIST_FILENAME + " not found")
        quit()
    return list_of_names


def get_list_of_trailers():
    """
        List of trailers specified in movie list file

        Returns:
            An array list of trailer urls
            example:
            ['vwyZH85NQC4']
        Exception:
            IOError: quits program if movie list file nor found
        """
    list_of_trailers = []

    try:
        with open(MOVIE_LIST_FILENAME) as movie_list_file:
            file_reader = csv.reader(movie_list_file, delimiter=',')
            for row in file_reader:
                list_of_trailers.append(row[1])
    except IOError:
        print(MOVIE_LIST_FILENAME + " not found")
        quit()
    return list_of_trailers
