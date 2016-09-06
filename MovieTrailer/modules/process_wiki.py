import wikipedia


def get_wiki_summary_for_movie(param_movie_name):
    """
        Summary for the movie from wikipedia.org

        Args:
            param_movie_name
        Returns:
            One sentence synopsis from the movie page
        """

    local_summary = wikipedia.summary(param_movie_name, sentences=1)
    return local_summary


def get_wiki_box_art_url_for_movie(param_movie_name):
    """
        Box art url

        Args:
            param_movie_name
        Returns:
            url string of the box art for the movie from wikipedia.org
        """

    movie_page = wikipedia.page(param_movie_name)
    url_list = movie_page.images

    # loop thru url_list and save in list only which contans '.jpg'
    url_jpg_list = []
    for url_jpg_str in url_list:
        url_jpg_len = url_jpg_str.find(".jpg")
        if url_jpg_len >= 0:
            url_jpg_list.append(url_jpg_str)

    # return if list has only one jpg entry
    if len(url_jpg_list) == 1:
        return url_jpg_list[0]

    # loop thru url_list and save in list only which contans '.png'
    url_png_list = []
    for url_png_str in url_list:
        url_png_len = url_png_str.find(".png")
        if url_png_len >= 0:
            url_jpg_list.append(url_png_str)

    # return if list has only one png entry
    if len(url_png_list) == 1:
        return url_png_list[0]

    # loop thru url_jpg_list to get only those urls which contain the movie name
    # get one first word from movie title
    movie_title = param_movie_name.split(' ')
    for movie_text_itr in movie_title:
        movie_text = movie_text_itr
        break

    # use the movie work to search thru the movie_jpg list
    for url_jpg_str in url_jpg_list:
        url_jpg_len = url_jpg_str.find(movie_text)
        if url_jpg_len >= 0:
            return url_jpg_str