import webbrowser


class Movie:
    def __init__(self, title, storyline, box_art, trailer):
        self.title = title
        self.storyline = storyline
        self.box_art_url = box_art
        self.trailer_url = trailer

    def play_trailer(self):
        webbrowser.open(self.trailer_url)
"""

    def __init__(self, title, story_line, box_art_url, trailer_url):
        self.title = title
        self.story_line = story_line
        self.box_art_url = box_art_url
        self.trailer_url = trailer_url

    def play_trailer(self):
        webbrowser.open(self.trailer_url)
"""