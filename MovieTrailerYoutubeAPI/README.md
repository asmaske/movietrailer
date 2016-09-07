# MovieTrailerYoutubeAPI Application

MovieTrailerYoutubeAPI is a Python based application. The application lists the Youtube trailer id and description of a movie.

##### Note

 - The application needs Google API developer key to run successfully
 - The application makes **Youtube API** call to fetch movie trailer data

### Tech

MovieTrailerYoutubeAPI application uses the following software:

* [Python] - Programming language that lets you work quickly
* [Google Client Library for Python] - Google APIs Client Library for Python

### Installation
#### 1. Python
Download and install the latest stable version of Python
Add Python executables location to the PATH environment variable
#### 2. Google APIs Client Library for Python
Install Google APIs Client Library for Python using command:
**pip install --upgrade google-api-python-client**
#### 3. MovieTrailerYoutubeAPI application
Clone/copy the MovieTrailerYoutubeAPI source files to a local directory

### Application Directory Structure
* MovieTrailerYoutubeAPI
    + README.md
    + MovieList.csv
    + movieyoutubeapi.py

### Running the application
1. Change directory to the application source directory
2. **MovieList.csv** is a comma seperated CSV file which has the list of movies
3. Run application using the following command:
    + **python movieyoutubeapi.py**
4. The application outputs information of the movie trailer youtube id and description 
5. Sample output:

> Videos for: The Secret Life of Pets
> -yPuWcCykNk (The Secret Life of Pets Official Trailer #1 (2016) - Kevin Hart, Jenny Slate Animated Comedy HD)
> UZ4WBlveGfw (The Secret Life of Pets Official Trailer #1 (2016) Louis C.K. Animated Movie HD)
> djFUqhbXSwA (THE SECRET LIFE OF PETS - Official Final Trailer (2016)
> Animated Comedy Movie HD)
> i-80SGWfEjM (The Secret Life Of Pets - Official Teaser Trailer (HD) - Illumination)
> GOaS68dEu8w (THE SECRET LIFE OF PETS - Official Trailer #2 (2016) Animated Comedy Movie HD)

   [Python]: <https://python.org>
   [Google Client Library for Python]: <https://developers.google.com/api-client-library/python/start/installation>