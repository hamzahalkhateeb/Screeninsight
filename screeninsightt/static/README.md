ScreenInsight Project Description:

ScreenInsight is an interactive website engineered to deliver extensive movie and TV show information directly to users' browsers. Leveraging multiple APIs, ScreenInsight retrieves JSON files encompassing trending movies, genre-specific shows, and additional content. Users enjoy a seamless experience as they log in, explore, rate, add to watchlist, and review both movies and TV shows. Moreover, the platform empowers users with the ability to customize their interactions, including managing their preferences and lists. Additionally, ScreenInsight boasts a recommendation feature powered by an algorithm that tailors movie suggestions based on users' liked movies lists, ensuring personalized content discovery.

Views.py: the backend side of my project contains the main functions which are as follows:
    - def index(request):
        On the main page of my app, we integrate the powerful TMDB API to provide users with a diverse range of movie options. Leveraging this API, the app dynamically fetches trending movies, movies belonging to various genres, and even the top 10 movies of all time, ensuring a constantly updated and engaging selection for users.
        
        Moreover, our app personalizes the user experience by incorporating their liked movies. By utilizing the user's liked movies object, we tailor API fetch requests to recommend movies that align with their preferences, fostering a more tailored and enjoyable browsing experience.
        
        Users have the ability to click on movie titles and be taken to a page where it displays said movie's details.
        
        The function then renders all said information on the index.html page.

    - def tv(request):
        This function renders a page works the same way the index page does; however, this one displays TV shows rather than movies. It then renders the information on tv.html page.

    - def login_view(request):
        Allows users to log in.

    - def logout_view(request):
        Allows users to log out.

    - def register(request):
        Allows users to register.

    - def movieDetails(request, movieid):
        This function utilizes the unique movie ID to send an API request, retrieving comprehensive details about the selected movie. These details encompass various elements including the movie's synopsis, overall rating, cast members, similar movies, and a collection of reviews. By leveraging the movie ID, users gain access to a wealth of information that is then rendered on the movie_details.html page.

    - def exists(request):
        This function checks if a movie is in the user's liked movies object field list or a watchlist object field list, it then sends a message to movieDetails.js to tell it what color should the heart and eye symbols be when the page is loaded. If the heart is red, it means the movie already exists in the user's liked movie list; otherwise, it is grey. The same applies to the eye symbol if it is green.

    - def tvexists(request):
        This function works the same way as the above function, except it is for TV shows rather than movies. It works with the tvdetails.html page.

    - def tvdetails(request, movieid):
        This function works the same way as the above, however, it is for TV shows rather than movies. It displays a TV show's details on tvdetails.html.

    - def genrePage(request, genreid):
        By clicking on a genre name, it allows this function to request 40 movies associated with said genre and send them to genrePage.html.

    - def genrePagetv(request, genreid):
        This function works the same way as the above function, however, it is dedicated to genres associated with TV show genres only and displays the resulting data on genrePagetv.html.

    - def filter(request):
        This function takes multiple variables from a form on that is rendered on genrePage and performs a filtered search function that retrieves data based on parameters such as rating, genre, and country. The returned search results are then rendered on the genrePage.html.

    - def filtertv(request):
        This function works the same way as the above function, however, it displays the results on genrePagetv.html.

    - def basicsearch(request):
        This function takes the name of a movie from a search form on index.html and sends an API request that fetches movies with similar names. It then displays the data on genrePage.html.

    - def basicsearchtv(request):
        This function works the same way as the above function, however, it takes the search parameter from tv.html and displays the results on genrePagetv.html.

    - def addobjectL(request):
        This function is called when the heart symbol on movie_details.html is clicked. It retrieves or makes the LikedMovies model and either adds or deletes the movie from the object field. The function then returns a response to movieDetails.js to tell it what color the heart should be. If the movie is in the user's LikedMovies, it is red; if not, it is grey.

    - def tvaddobjectsL(request):
        This function works the same way as the above section except it works with TV shows rather than movies.

    - def addobjectW(request):
        This function works the same way as the above function, however, it handles movies that are added to a watchlist instead.

    - def tvaddobjectsW(request):
        This function works the same way as the above section except it works with TV shows rather than movies.

    - def review(request):
        This function is called when the "add a review" form is submitted on movie_details.html. It takes a group of variables and saves them as a Comment object, then adds it to the movie's Comments object field list. The page is then reloaded to display the recently added review in the review's section of movie_details.html page.

    - def tvreview(request):
        This function works the same as the above function except it is for TV shows rather than movies. It works with tv_details.html.

    - def edit(request):
        This function is called when the user clicks the pen symbol on movie_details.html page. It edits the review they added earlier, allowing them to add different inputs, which will replace the older inputs.

    - def tvedit(request):
        This function works the same as the above function.

    - def delete(request):
        This function is called when the user clicks the trash bin symbol on either the movie_details.html page or the tvdetails.html page. It then retrieves the review which the user has submitted for the relevant movie or show and deletes it.

    - def profile(request):
        This function renders a profile page which displays the user's list of liked movies, reviews, and watchlisted movies. The user is then able to toggle between movies and TV shows, as well as deleting movies from their respective lists.

The front end of my project doesn't have any standout features; the HTML and CSS pages are relatively standard. The JavaScript primarily consists of event listeners that send API requests to the Python backend to perform functions like adding reviews. The only notable feature is its ability to convert float rating values of a movie into star ratings instead of just displaying a number.


Requirements: The projects doesn't need any special installation package, it needs the standard installation packages to run django, js, html, css and python, the file can then 