# MovieTrailer Application

MovieTrailer is a Python based web application. The application displays 2016 animation movie box art images. The movie trailer is played when an image is clicked.

##### Note

 - The application has been developed and tested using Python version 3.2.5
 - The application uses **Wikipedia API** for Python to fetch movie data
 - The application HTML file is created implicitly and opened in the web browser during execution

### Tech

MovieTrailer uses the following softwares:

* [Python] - Programming language that lets you work quickly
* [Bootstrap] - UI boilerplate for modern web apps

### Installation
#### 1. Python
Download and install the latest stable version of Python.
Add Python executables location to the PATH environment variable.
#### 2. MovieTrailer application
Clone/copy the MovieTrailer source files to a local directory

### Application Directory Structure
* MovieTrailer
    + README.md
    + MovieList.csv
    + entertainment_center.py
    + objects
        + media.py
    + modules
        + create_html.py
        + html_contents.py
        + process_data.py
        + process_wiki.py

### Running the application
1. Change directory to the application source directory
2. **MovieList.csv** is a comma seperated CSV file which has the list of movies and corresponding youtube trailer id
3. Run application using the following command:
    + **python entertainment_center.py**
4. Web browser is launched with box art images of the movies listed in the the csv file. To watch the trailer of any movie, click on the movie box art image. 

   [Python]: <https://python.org>
   [Bootstrap]: <http://getbootstrap.com/>
