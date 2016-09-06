from googleapiclient.discovery import build
import csv

# set constants
DEVELOPER_KEY = "developer key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
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


def youtube_search(param_list_of_movies):
  """
      Get Youtube movie trailer id

      Returns:
          Display information for trailers
 """
  # build youtube object
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method for every movie and return only first 5
  for movie_name in list_of_movies:
    search_response = youtube.search().list(
      q=movie_name + 'Official Trailer',
      part="id,snippet",
      maxResults=5
    ).execute()

    videos = []

    # Add each result to the and then display the lists of matching videos
    for search_result in search_response.get("items", []):
      if search_result["id"]["kind"] == "youtube#video":
        videos.append("%s (%s)" % (search_result["id"]["videoId"],  search_result["snippet"]["title"]))
    print ("Videos for: " + movie_name)
    print("--------------------------")
    print ("\n".join(videos), "\n")


# main program

# get movie list from csv file
list_of_movies = get_list_of_movies()

#display movie trailer name and youtube id
youtube_search(list_of_movies)
