**ScreenInsight Project Description:**
  ScreenInsight is an interactive website engineered to deliver extensive movie and TV show information directly to users' browsers. Leveraging multiple APIs, ScreenInsight retrieves JSON files encompassing trending movies, genre-specific shows, and additional content. Users enjoy a seamless experience as they log in, explore, rate, add to watchlist, and review both movies and TV shows. Moreover, the platform empowers users with the ability to customize their interactions, including managing their preferences and lists. Additionally, ScreenInsight boasts a recommendation feature powered by an algorithm that tailors movie suggestions based on users' liked movies lists, ensuring personalized content discovery.

**Distinctiveness and Complexity:**
*  **Advanced Tools:** Utilizing a diverse array of sophisticated tools, including JavaScript and Python, our website offers a personalized experience for users. By employing these technologies, we customize a recommended movie list based on the user's preferences, enhancing user engagement and satisfaction.
* **Functionality Enhancements:**
  + Advanced Search Functions: In addition to basic search capabilities, our website incorporates advanced search functions, enabling users to find movies more efficiently and effectively.
  + External API Integration: Setting us apart from other projects, our website seamlessly integrates with external APIs to retrieve comprehensive movie information. Leveraging multiple API requests on each page, our platform dynamically updates its extensive movie database with every page refresh, ensuring users have access to the latest information.
  + In house API that allows communication between frontend and backend to save user data such as preferences, liked movies, watchlist etc...
  + Interactive Animations: Leveraging the power of JavaScript and CSS, we've infused our application with captivating animations and interactivity. These dynamic elements breathe life into the app, making it not only functional but also enjoyable and engaging for users.

  
**-------------------------------------------------------------------------------------------------------------------------------------------------------------**
**File By File explanation**

* Views.py: the backend side of my project contains the main functions which are as follows:
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

**-------------------------------**

* layout.html:
  - The foundation of my frontend, it has the navigation bar which allows the user to switch between tv shows, movies, genres and if authenticated, log out, or visit the profile page.
  - It also has a search field which allows the user to search a movie by its name
  - it is complimentd by a javascript filw which is further explained in the next point

* layout.js:
  - When the page DOM content is loaded, the opacity of the navigation bar will smoothly increase to give a nice awelcoming gesture
  - The page has mutlpile event listenres that wait for a genre name to be clicked which then smoothly scrolls taht genre of movies into view, note that the movie genre sections are in index.html which will discusses later.

* layout.css:
  - Provides the stylistic choices for the design of the page

* index.html:
  - The most complex html page in my website, the main components of this page is various movie containers which container trending movies, different gernes of movies as well as different the rbread and butter of app, which is the recommended movies. All these container import data from the backend and use a forloop to display it all. each container is accompanied by various buttons

* index.js:
  - It waits for the DOM content to be fully loaded before executing the JavaScript code.
  - It selects all elements with the class .movie-info within the .indexdiv and sets a timeout to gradually reveal them by adjusting opacity and padding.
  - It initializes variables and selects buttons for scrolling through movie elements (nextbtn, nextbtn2, nextbtn3, etc.).
  - It sets up event listeners for each button to scroll horizontally through the movie elements using smooth scrolling behavior.
  - It also sets up an interval function to automatically scroll through the movie elements at regular intervals.
  - Similar functionality is repeated for multiple sets of movie elements (indexed as trdmDisplayed, trdmDisplayed2, trdmDisplayed3, etc.) and their corresponding buttons (nextbtn4, nextbtn5, nextbtn6, etc.).
  - For each set of movie elements, there are next and previous buttons to navigate forward and backward.
  - Each click on the next button increments the index of the displayed movie element, and each click on the previous button decrements the index.
  - The code ensures that the index stays within the valid range of movie elements.
  - It calculates the scroll distance needed based on the offset of the selected movie element and the container's offset, then smoothly scrolls the container horizontally to display the desired movie element.

* index.css:
  - Provides the code necesary for some animations and visual effects of the index page such as increasing scale when a movie is hovered over etc.

* genrePage.html:
  - ThIs page is displayed after the user submits a basic search query through the search bar on the navigation bar of layout.html, it displays the results of the basic search as well a form to be able to execute an advanced search. Furthermore, this page also displays a wide range of movies from a specific genre if that specific genre was clicked on index.html
    
* genrePage.js:
  - The js side of things does not contain any major functions except the code to transition opacity of the navigation bar.

* genrePage.css:
  - Provides the basic code for a nice visual.

* tv.html,  tv.js, tv.css and genrePagetv.html, genrePagetv.js, and genrePagetv.css:
  - All the above work in an identical fashion to the index page, the only difference is that it use a different package of data which has tv shows data rather than movies.

* movie_details.html:
  - This page is displayed when a movie name is clicked.
  - it has a div which houses a backdrop of the movie, and on top of that container, there is another container which houses more information about the movie as well as a nice smaller poster.
  - The section of the page has the basic information about the movie such as its star rating, production companies etc.
  - another section of the page containes the cast of te movie.
  - below that, there is a container for similar movies which is receieved through an api request
  - below that there is a review section through which the user can submit one review, all the reviews for the movie are then displayed below that, through which the user can edit their own review.

* movieDetails.js:
  - DOMContentLoaded Event Listener: Executes JavaScript code once the DOM content is loaded. It sets the opacity of the navigation bar to 1 and initializes some variables.
  - Tab Click Event Listeners: Toggle between the general information and cast tabs when clicked. This changes the display style of the corresponding sections accordingly.
  - findstars Function: Converts the numerical rating into visual stars representation, considering whole stars, half stars, and off stars.
  - colourbtns Function: Changes the color of buttons (like 'Add to Liked List' and 'Add to Watchlist') based on whether the movie is already in the user's list. It fetches data from the server to determine this.
  - Review Submission Event Listener: Submits a review for the movie when the submit button is clicked. It validates the input fields and sends a POST request to the server to save the review.
  - Edit Review Event Listener: Handles the editing of a review. It switches the review content to input fields, pre-filling them with the existing review data.
  - Save Review Event Listener: Saves the edited review when the save button is clicked. It validates the input fields and sends a POST request to the server to update the review.

* movieDetails.css:
  - Provides the code to make the page look nice, a notable section of this page is the accordion section which the functionalty for the similar movie section, it has a comprehensive set of css rules that allow for nice animations when a similar movie is hovered over.
 
* tvdetails.html, tvdetails.js and tvdetails.css:
  - All those have almost identical code to the movieDetails files, the only difference is that it use tv show packages rather movies, and it swaps the cast section for a season and episodes section. 

* profile.html:
  - This page can be views if the user is logged in, it containes the default profile pictur as well as the username.
  - Below that, it containes 3 sections, the middle one houses all the reviews the user has submitted, on the left there is a list of the movies the user liked, and on the right there is a list of the movies the user watchlsited.
  - There 2 buttons to allows the user to switch between the tv show section and the movies section.

* profile.js:
  - The js code allows the user to toggle between the tv show section and the movies section as each section does not have what the other does
  - The js code also handles the deletion of movies and tv shows from watchlists and liked lists.
 
* profile.css:
  - Provides the code necessary to organise the page nicely. 



**-------------------------------------------------------------------------------------------------------------------------------------------------------------**


Requirements: The projects doesn't need any special installation package, it needs the standard installation packages to run django, js, html, css and python, the file can then be run by executing "python manage.py runserver"





