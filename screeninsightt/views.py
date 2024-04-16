import json
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import requests
import random
from .models import Comment, Commenttv, LikedMovies, Likedtv, Tv, User, Movie, WatchList, WatchListtv



def debug(str1, str2):
    if str1 < str2:
        key = str1
        key2 = str2
    elif str2 < str1:
        key = str2
        key2 = str1
    elif len(str1) == len(str2):
        key = str1
        key2= str2

    print(f"1: key: {key}")
    print(f"2: {key2}")
            

    emptystring = ""
    i = 1
    found = 0
    print("0: basic variables have been initiated")
    
    
    while found == 0:
        result = []
        print(f"3: first empty result {result}")
        char = key[:i]
        print(f"4: first char {char}")
        remainder = len(key) % len(char)
        print(f"5: first remainder {remainder}")
        if i >len(key):
            print(f"6: i is bigger than the length of key, loop has been broken")
            return emptystring
            

        if not remainder == 0:
            i += 1
        else:
            mult = len(key) // len(char)
            print(f"7: how many times to repeat{char}, it is:{mult}")
            for k in range(mult):
                result.append(char)
            divisor = ''.join(result)
            print(f"8: divisor {divisor}")
            
            if not divisor == key:
                i += 1
                print(f"9: the divisor isn't equal to the key, i has been increased, the loop has been restarted")
            elif divisor == key:
                """found = 1
                return char"""
                if not len(key2) % len(divisor) == 0:
                    print(f"9.2: length of {key2}: {len(key2)}")
                    print(f"9.3: length of {divisor}: {len(divisor)}")
                    k = len(key2) % len(divisor)
                    print(f"9.2: {k}")
                    print(f"10: the length of {key2} can't be divided by length of {divisor}, i has increased and loop restarted")
                    i+=1
                else:
                    result2 = []
                    print(f"11: second empty result: {result2}")
                    q = len(key2) // len(divisor)
                    print(f"12: how many times to repeat char: {q}")
                    for h in range(q):
                        result2.append(divisor)
                    char2 = ''.join(result2)
                    print(f"13: second char, which will be compared to key 2: {char2}")
                    if char2 == key2:
                        found = 1
                        print(f"14: {char2} : does indeed equal {key2}")
                        return char
                    else:
                        print(f"15: {char2} doesn't equal{key2}")
                        return emptystring

def index(request):

    





    #genres-----------------------------------------------------------------
    url2 = "https://api.themoviedb.org/3/genre/movie/list?language=en"
    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }
    response2 = requests.get(url2, headers=headers2)
    if response2.status_code == 200:
        proper_response2 = json.dumps(response2.json(), indent=2)
        data2 = json.loads(response2.text)
        genres = data2['genres']
        


    #Trending Movies api--------------------------------------------------
    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"
    api_key = "54ac68f2b6a331df423a224512d8e936"  
    headers = {"accept": "application/json"}
    params = {"api_key": api_key, "page": 1}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        proper_response = json.dumps(response.json(), indent=2)
        data = json.loads(response.text)
        TrendingMovies = data['results'][:10]
        
    #------------------------------added genres to movies
    for movie in TrendingMovies:
        movie['genres'] = []
        for genre in genres:
            if genre['id'] in movie['genre_ids']:
                movie['genres'].append(genre['name'])

    

   
    #action movies ---------------------------------------------------------
        
    url4 = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=7&with_genres=28"

    headers4 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response4 = requests.get(url4, headers=headers4)

    if response4.status_code == 200:
        properresponse4 = json.dumps(response4.json(), indent=2)
        data4 = json.loads(response4.text)
        actionMovies = data4['results'][:10]
    
    #comedy movies-------------------------------------------------------------
    url5 = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=7.00&with_genres=35"

    headers5 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response5 = requests.get(url5, headers=headers5)

    if response5.status_code == 200:
        properresponse5 = json.dumps(response5.json(), indent=2)
        data5 = json.loads(response5.text)
        comedyMovies = data5['results'][:10]

    #drama movies---------------------------------------------------------------
    url6 = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=7.00&with_genres=18"

    headers6 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response6 = requests.get(url6, headers=headers6)

    if response6.status_code == 200:
        properresponse6= json.dumps(response6.json(), indent=2) 
        data6 = json.loads(response6.text)
        dramaMovies = data6['results'][:10]
        
    #Fantasy movies----------------------------------------------------
    
    url7 = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=7.00&with_genres=14"

    headers7 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response7 = requests.get(url7, headers=headers7)

    if response7.status_code == 200:
        properresponse7= json.dumps(response7.json(), indent=2) 
        data7 = json.loads(response7.text)
        fantasyMovies = data7['results'][:10]
        
    #Horror movies----------------------------------------------------
    
    url8 = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=7.00&with_genres=27"

    headers8 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response8 = requests.get(url8, headers=headers8)

    if response8.status_code == 200:
        properresponse8= json.dumps(response8.json(), indent=2) 
        data8 = json.loads(response8.text)
        horrorMovies = data8['results'][:10]
        

    #Romance movies----------------------------------------------------
    url9 = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte=7.00&with_genres=10749"

    headers9 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response9 = requests.get(url9, headers=headers9)

    if response9.status_code == 200:
        properresponse9= json.dumps(response9.json(), indent=2) 
        data9 = json.loads(response9.text)
        romanceMovies = data9['results'][:10]

    #Top 10 rated movies----------------------------------------------------------

    url10 = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    headers10 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response10 = requests.get(url10, headers=headers10)

    if response10.status_code == 200:
        properresponse10= json.dumps(response10.json(), indent=2) 
        data10 = json.loads(response10.text)
        topRated = data10['results'][:10]

    #recommended movies----------------------------------------------------------------
        finalmovies = []
        if request.user.is_authenticated:
            user = request.user
            lmids = []
            movieids = []
            
            likedlist = LikedMovies.objects.filter(user=user).first()
            if likedlist:

                likedmovies = likedlist.LikedMovie.all()
                
                for movie in likedmovies:
                    if movie.movieid in lmids:
                        continue
                    else:
                        lmids.append(movie.movieid)

                if len(lmids) <= 5:
                    movieids = lmids

                else:
                    movieids = random.sample(lmids)

                for id in movieids:
                    url2 = f"https://api.themoviedb.org/3/movie/{id}/similar?language=en-US&page=1"

                    headers2 = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
                    }
                    response2 = requests.get(url2, headers=headers2)
                    data1 = json.loads(response2.text)
                    randoms = random.sample(range(1,11), 2)

                    movie1 = data1['results'][randoms[0]]
                    movie2 = data1['results'][randoms[1]]
                    finalmovies.append(movie1)
                    finalmovies.append(movie2)
            else:
                finalmovies=[]

                


        
        
    return render(request, "screeninsightt/index.html", {
        "TrendingMovies": TrendingMovies,
        "genres": genres,
        "actionMovies": actionMovies,
        "comedyMovies": comedyMovies,
        "dramaMovies": dramaMovies,
        "fantasyMovies": fantasyMovies,
        "horrorMovies": horrorMovies,
        "romanceMovies": romanceMovies,
        "topRated": topRated,
        "recommended": finalmovies

    })

def tv(request):
    
    #genres-----------------------------------------------------------------
    url2 = "https://api.themoviedb.org/3/genre/tv/list?language=en"
    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }
    response2 = requests.get(url2, headers=headers2)
    if response2.status_code == 200:
        proper_response2 = json.dumps(response2.json(), indent=2)
        data2 = json.loads(response2.text)
        genres = data2['genres']
        


    #Trending Movies api--------------------------------------------------
    url = "https://api.themoviedb.org/3/trending/tv/day?language=en-US"

    api_key = "54ac68f2b6a331df423a224512d8e936"  
    headers = {"accept": "application/json"}
    params = {"api_key": api_key, "page": 1}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        proper_response = json.dumps(response.json(), indent=2)
        data = json.loads(response.text)
        TrendingMovies = data['results'][:10]
        
    #------------------------------added genres to movies
    for movie in TrendingMovies:
        movie['genres'] = []
        for genre in genres:
            if genre['id'] in movie['genre_ids']:
                movie['genres'].append(genre['name'])

    



    




    
    #action movies ---------------------------------------------------------
        
    url4 = "https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_count.gte=7&with_genres=10759"

    headers4 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response4 = requests.get(url4, headers=headers4)

    if response4.status_code == 200:
        properresponse4 = json.dumps(response4.json(), indent=2)
        data4 = json.loads(response4.text)
        actionMovies = data4['results'][:10]
    
    #comedy movies-------------------------------------------------------------
    url5 = "https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_count.gte=7&with_genres=35"

    headers5 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response5 = requests.get(url5, headers=headers5)

    if response5.status_code == 200:
        properresponse5 = json.dumps(response5.json(), indent=2)
        data5 = json.loads(response5.text)
        comedyMovies = data5['results'][:10]

    #drama movies---------------------------------------------------------------
    url6 = "https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_count.gte=7&with_genres=18"

    headers6 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response6 = requests.get(url6, headers=headers6)

    if response6.status_code == 200:
        properresponse6= json.dumps(response6.json(), indent=2) 
        data6 = json.loads(response6.text)
        dramaMovies = data6['results'][:10]
        
    #Fantasy movies----------------------------------------------------
    
    url7 = "https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_count.gte=7&with_genres=10765"

    headers7 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response7 = requests.get(url7, headers=headers7)

    if response7.status_code == 200:
        properresponse7= json.dumps(response7.json(), indent=2) 
        data7 = json.loads(response7.text)
        fantasyMovies = data7['results'][:10]
        
    #animation movies----------------------------------------------------
    
    url8 = "https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_count.gte=7&with_genres=16"

    headers8 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response8 = requests.get(url8, headers=headers8)

    if response8.status_code == 200:
        properresponse8= json.dumps(response8.json(), indent=2) 
        data8 = json.loads(response8.text)
        horrorMovies = data8['results'][:10]
        

    #mystery movies----------------------------------------------------
    url9 = "https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_count.gte=7&with_genres=9648"

    headers9 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response9 = requests.get(url9, headers=headers9)

    if response9.status_code == 200:
        properresponse9= json.dumps(response9.json(), indent=2) 
        data9 = json.loads(response9.text)
        romanceMovies = data9['results'][:10]

    #Top 10 rated movies----------------------------------------------------------

    url10 = "https://api.themoviedb.org/3/tv/top_rated?language=en-US&page=1"

    headers10 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response10 = requests.get(url10, headers=headers10)

    if response10.status_code == 200:
        properresponse10= json.dumps(response10.json(), indent=2) 
        data10 = json.loads(response10.text)
        topRated = data10['results'][:10]
    ###############################################################################################
    finalmovies = []    
    if request.user.is_authenticated:
            user = request.user
            lmids = []
            movieids = []
            
            likedlist = Likedtv.objects.filter(user=user).first()
            if likedlist:

                likedmovies = likedlist.LikedMovie.all()
                
                for movie in likedmovies:
                    if movie.movieid in lmids:
                        continue
                    else:
                        lmids.append(movie.movieid)

                if len(lmids) <= 5:
                    movieids = lmids

                else:
                    movieids = random.sample(lmids)

                for id in movieids:
                    url2 = f"https://api.themoviedb.org/3/tv/{id}/similar?language=en-US&page=1"

                    headers2 = {
                        "accept": "application/json",
                        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
                    }
                    response2 = requests.get(url2, headers=headers2)
                    data1 = json.loads(response2.text)
                    randoms = random.sample(range(1,11), 2)

                    movie1 = data1['results'][randoms[0]]
                    movie2 = data1['results'][randoms[1]]
                    finalmovies.append(movie1)
                    finalmovies.append(movie2)
        
    return render(request, "screeninsightt/tv.html", {
        "TrendingMovies": TrendingMovies,
        "genres": genres,
        "actionMovies": actionMovies,
        "comedyMovies": comedyMovies,
        "dramaMovies": dramaMovies,
        "fantasyMovies": fantasyMovies,
        "horrorMovies": horrorMovies,
        "romanceMovies": romanceMovies,
        "topRated": topRated,
        "recommended": finalmovies

    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "screeninsightt/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "screeninsightt/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "screeninsightt/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "screeninsightt/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "screeninsightt/register.html")

def movieDetails(request, movieid):

    #Get movie information///////////////////////
    url = f"https://api.themoviedb.org/3/movie/{movieid}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)



    #Get associated images/////////////////////////////////

    url3 = f"https://api.themoviedb.org/3/movie/{movieid}/credits?language=en-US"

    headers3 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response3 = requests.get(url3, headers=headers3)
    data3 = json.loads(response3.text)
    cast = data3["cast"]
        


    #Get similar movies///////////////////////////
    url2 = f"https://api.themoviedb.org/3/movie/{movieid}/similar?language=en-US&page=1"

    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }
    response2 = requests.get(url2, headers=headers2)
    data1 = json.loads(response2.text)
    similarMovies = data1['results'][:10]


    movieinstance = Movie.objects.filter(movieid = movieid)
    reviews =  []

    if movieinstance.exists():
        for movie in movieinstance:
            comments = movie.comments.all()
            for comment in comments:
                reviews.append(comment)
    
    



    return render(request, "screeninsightt/movie_details.html", {
           "datas": data,
           "cast": cast,
           "similarMovies": similarMovies,
           "reviews":reviews
    })

def tvdetails(request, movieid):
     #Get movie information///////////////////////
    url = f"https://api.themoviedb.org/3/tv/{movieid}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    


    #Get associated images/////////////////////////////////

    url3 = f"https://api.themoviedb.org/3/tv/{movieid}/images"

    headers3 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response3 = requests.get(url3, headers=headers3)
    data3 = json.loads(response3.text)
    backdrops = data3["backdrops"]
        


    #Get similar movies///////////////////////////
    url2 = f"https://api.themoviedb.org/3/tv/{movieid}/similar?language=en-US&page=1"

    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }
    response2 = requests.get(url2, headers=headers2)
    data1 = json.loads(response2.text)
    similarMovies = data1['results'][:10]


    ###################################

    movieinstance = Tv.objects.filter(movieid = movieid)
    reviews =  []

    if movieinstance.exists():
        for movie in movieinstance:
            comments = movie.comments.all()
            for comment in comments:
                reviews.append(comment)

    ############################################################
    


    return render(request, "screeninsightt/tvdetails.html", {
           "datas": data,
           "backdrops": backdrops,
           "similarMovies": similarMovies,
           "reviews": reviews,
           
    })

def genrePage(request, genreid):
    genrediq = [{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'}, {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]

    for genre in genrediq:
        if genre['id'] == genreid:
            genrename = genre['name']

    



    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.lte=7.00&with_genres={genreid}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        properresponse= json.dumps(response.json(), indent=2) 
        data = json.loads(response.text)
        batch1movies = data['results']


    url2 = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=2&sort_by=popularity.desc&vote_average.lte=7.00&with_genres={genreid}"

    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response2 = requests.get(url2, headers=headers2)

    if response2.status_code == 200:
        properresponse2= json.dumps(response2.json(), indent=2) 
        data2 = json.loads(response2.text)
        batch2movies = data2['results']

    
    return render(request, "screeninsightt/genrePage.html", {
        "batch1movies": batch1movies,
        "batch2movies": batch2movies, 
        "genrename": genrename,
        "genres": genrediq
    })

def genrePagetv(request, genreid):
    genrediq = [
        {"id": 10759, "name": "Action & Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 10762, "name": "Kids"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10763, "name": "News"},
        {"id": 10764, "name": "Reality"},
        {"id": 10765, "name": "Sci-Fi & Fantasy"},
        {"id": 10766, "name": "Soap"},
        {"id": 10767, "name": "Talk"},
        {"id": 10768, "name": "War & Politics"},
        {"id": 37, "name": "Western"}
    ]


    for genre in genrediq:
        if genre['id'] == genreid:
            genrename = genre['name']

    url = f"https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_count.gte=7&with_genres={genreid}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        properresponse = json.dumps(response.json(), indent=2)
        data = json.loads(response.text)
        batch1movies = data['results']

    url2 = f"https://api.themoviedb.org/3/discover/tv?include_adult=true&include_null_first_air_dates=false&language=en-US&page=2&sort_by=popularity.desc&vote_count.gte=7&with_genres={genreid}"

    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response2 = requests.get(url2, headers=headers2)

    if response2.status_code == 200:
        properresponse2 = json.dumps(response2.json(), indent=2)
        data2 = json.loads(response2.text)
        batch2movies = data2['results']

    return render(request, "screeninsightt/genrePagetv.html", {
        "batch1movies": batch1movies,
        "batch2movies": batch2movies,
        "genrename": genrename,
        "genres": genrediq
    })
     
def filter(request):
    name = request.GET.get("name", "")
    
    genre = request.GET.get("genre", "")
    
    country = request.GET.get("country", "")
    
    rating = request.GET.get('rating', "")
    
    genrediq = [{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'}, {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]

    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte={rating}&with_genres={genre}&with_keywords={name}&with_origin_country={country}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response = requests.get(url, headers=headers)

    data = json.loads(response.text)
    batch1movies = data['results']

    url2 = f"https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=false&language=en-US&page=2&sort_by=popularity.desc&vote_average.gte={rating}&with_genres={genre}&with_keywords={name}&with_origin_country={country}"

    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response2 = requests.get(url2, headers=headers2)

    data2 = json.loads(response2.text)
    batch2movies = data2['results']

    return render(request, "screeninsightt/genrePage.html", {
        "batch1movies": batch1movies,
        "batch2movies": batch2movies, 
        "genrename": "Filtered Results...",
        "genres": genrediq
        }
        )

def filtertv(request):
    name = request.GET.get("name", "")
    genre = request.GET.get("genre", "")
    country = request.GET.get("country", "")
    rating = request.GET.get('rating', "")

    genrediq = [{'id': 10759, 'name': 'Action & Adventure'}, {'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 10762, 'name': 'Kids'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10763, 'name': 'News'}, {'id': 10764, 'name': 'Reality'}, {'id': 10765, 'name': 'Sci-Fi & Fantasy'}, {'id': 10766, 'name': 'Soap'}, {'id': 10767, 'name': 'Talk'}, {'id': 10768, 'name': 'War & Politics'}, {'id': 37, 'name': 'Western'}]  
    
    url = f"https://api.themoviedb.org/3/discover/tv?include_adult=false&include_null_first_air_dates=false&language=en-US&page=1&sort_by=popularity.desc&vote_average.gte={rating}&with_genres={genre}&with_keywords={name}&with_origin_country={country}"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response = requests.get(url, headers=headers)

    data = json.loads(response.text)
    batch1movies = data['results']

    url2 = f"https://api.themoviedb.org/3/discover/tv?include_adult=false&include_null_first_air_dates=false&language=en-US&page=2&sort_by=popularity.desc&vote_average.gte={rating}&with_genres={genre}&with_keywords={name}&with_origin_country={country}"

    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response2 = requests.get(url2, headers=headers2)

    data2 = json.loads(response2.text)
    batch2movies = data2['results']

    return render(request, "screeninsightt/genrePage.html", {
        "batch1movies": batch1movies,
        "batch2movies": batch2movies, 
        "genrename": "Filtered Results...",
        "genres": genrediq
        }
        )

def basicsearch(request):
    name = request.GET.get("name", "")
    

    
    url = f"https://api.themoviedb.org/3/search/movie?query={name}&include_adult=true&language=en-US&page=1"


    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response = requests.get(url, headers=headers)

    data = json.loads(response.text)
    batch1movies = data['results']

    url2 = f"https://api.themoviedb.org/3/search/movie?query={name}&include_adult=true&language=en-US&page=2"


    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response2 = requests.get(url2, headers=headers2)

    data2 = json.loads(response2.text)
    batch2movies = data2['results']

    return render(request, "screeninsightt/genrePage.html", {
        "batch1movies": batch1movies,
        "batch2movies": batch2movies, 
        "genrename": "Filtered Results..."
        
        }
        )

def basicsearchtv(request):
    name = request.GET.get("name", "")
    

    
    url = f"https://api.themoviedb.org/3/search/tv?query={name}&include_adult=true&language=en-US&page=1"


    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response = requests.get(url, headers=headers)

    data = json.loads(response.text)
    batch1movies = data['results']

    url2 = f"https://api.themoviedb.org/3/search/tv?query={name}&include_adult=true&language=en-US&page=2"


    headers2 = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1NGFjNjhmMmI2YTMzMWRmNDIzYTIyNDUxMmQ4ZTkzNiIsInN1YiI6IjY1NzU0OGM2ODlkOTdmMDBlMzc0YTI5ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.mmLv6VA0O7dWEKaUwFX-HKqeIeacdbl6eSCijy1uPSg"
    }

    response2 = requests.get(url2, headers=headers2)

    data2 = json.loads(response2.text)
    batch2movies = data2['results']

    return render(request, "screeninsightt/genrePagetv.html", {
        "batch1movies": batch1movies,
        "batch2movies": batch2movies, 
        "genrename": "Filtered Results..."
        
        }
        )

def addobjectL(request):
    movie_data = json.loads(request.body)

    moviename = movie_data.get("moviename")
    posterpath = movie_data.get("posterpath")
    user = movie_data.get("user")
    user2 = User.objects.get(pk=user)
    movieid = movie_data.get('movieid')
    
    movie = Movie.objects.filter(movieid = movieid).first()

    if movie:
        user_liked_movies = LikedMovies.objects.filter(user=user2)
        if user_liked_movies.exists():
            if movie in user_liked_movies.first().LikedMovie.all():
                user_liked_movies.first().LikedMovie.remove(movie)
                to_grey = True
            else:
                user_liked_movies.first().LikedMovie.add(movie)
                to_grey = False
        else:
            new_likedmovie = LikedMovies.objects.create(user=user2)
            new_likedmovie.LikedMovie.add(movie)
            to_grey = False
        
    else:
        new_movie=Movie.objects.create(
            movie_title=moviename,
            poster_path=posterpath,
            movieid=movieid
        )
        

        user_liked_movies2 = LikedMovies.objects.filter(user=user2)
        if user_liked_movies2.exists():
            user_liked_movies2.first().LikedMovie.add(new_movie)
            to_grey= False
        else:
            new_likedmovie2 = LikedMovies.objects.create(user=user2)
            new_likedmovie2.LikedMovie.add(new_movie)
            to_grey = False

        

    
    return JsonResponse({"to_grey": to_grey})

def addobjectW(request):
    movie_data = json.loads(request.body)

    moviename = movie_data.get("moviename")
    posterpath = movie_data.get("posterpath")
    user = movie_data.get("user")
    user2 = User.objects.get(pk=user)
    movieid = movie_data.get("movieid")
    
    movie = Movie.objects.filter(movieid=movieid).first()

    if movie:
        user_watched_movies = WatchList.objects.filter(user=user2)
        if user_watched_movies.exists():
            if movie in user_watched_movies.first().WatcheListMovies.all():
                user_watched_movies.first().WatcheListMovies.remove(movie)
                to_grey = True
            else:
                user_watched_movies.first().WatcheListMovies.add(movie)
                to_grey = False
        else:
            new_watchedmovie = WatchList.objects.create(user=user2)
            new_watchedmovie.WatcheListMovies.add(movie)
            to_grey = False
        
    else:
        new_movie=Movie.objects.create(
            movie_title=moviename,
            poster_path=posterpath,
            movieid=movieid
        )
        

        user_watched_movies2 = WatchList.objects.filter(user=user2)
        if user_watched_movies2.exists():
            user_watched_movies2.first().WatcheListMovies.add(new_movie)
            to_grey = False
        else:
            new_watchedmovie2 = WatchList.objects.create(user=user2)
            new_watchedmovie2.WatcheListMovies.add(new_movie)
            to_grey = False

        

    
    return JsonResponse({"to_grey": to_grey})

def profile(request):
    userid = ""

    if request.method == "POST":
        userid = request.POST.get("userid")

        userObjectInstance = get_object_or_404(User, pk=userid)

        Watchlistmovies = WatchList.objects.filter(user = userObjectInstance)
        Likedmovies = LikedMovies.objects.filter( user = userObjectInstance)
        reviews = Comment.objects.filter(user = userObjectInstance)
        
        watchlisttv = WatchListtv.objects.filter(user = userObjectInstance)
        likedtv = Likedtv.objects.filter( user = userObjectInstance)
        reviewstv = Commenttv.objects.filter(user = userObjectInstance)





    Wtv2 = []
    Ltv2 = []
    reviewstv2 = []

    
    if watchlisttv.exists():
        for watchlist in watchlisttv:
            Wmovies = watchlist.WatcheListMovies.all()
            for movie in Wmovies:
                Wtv2.append(movie)


    if likedtv.exists():
        for likedlist in likedtv:
            Lmovies = likedlist.LikedMovie.all()
            for movie in Lmovies:
                Ltv2.append(movie)

    for review in reviewstv:
        reviewstv2.append(review)


    Wmovies2 = []
    Lmovies2 = []
    reviews2 = []

    
    if Watchlistmovies.exists():
        for watchlist in Watchlistmovies:
            Wmovies = watchlist.WatcheListMovies.all()
            for movie in Wmovies:
                Wmovies2.append(movie)


    if Likedmovies.exists():
        for likedlist in Likedmovies:
            Lmovies = likedlist.LikedMovie.all()
            for movie in Lmovies:
                Lmovies2.append(movie)

    for review in reviews:
        reviews2.append(review)


    
    
        
        



    return render(request, "screeninsightt/profile.html", {
        "WatchlistMovies" : Wmovies2,
        "Likedmovies" : Lmovies2,
        "reviews":reviews2,
        "watchlisttv": Wtv2,
        "likedtv":Ltv2,
        "reviewstv": reviewstv2
    })

def exists(request):

    data = json.loads(request.body)

    user = data.get("user")
    userinstance = User.objects.get(pk=user)
    id = data.get("movieid")
    movieinstance = Movie.objects.filter(movieid=id)
    movieinstance2 = movieinstance.first()
    
    watchlist_exists = WatchList.objects.filter(user=userinstance).exists()
    

    if (watchlist_exists):
        watchlists = WatchList.objects.filter(user=userinstance).prefetch_related("WatcheListMovies")
        
        for movie in watchlists:
            movies = movie.WatcheListMovies.all()
            
            
        if movieinstance2 in movies:
            in_watchlist = True
        else:
            in_watchlist = False
    else:
        in_watchlist = False

    


    liked_exists = LikedMovies.objects.filter(user=userinstance).exists()

    if(liked_exists):
        likedlists = LikedMovies.objects.filter(user=userinstance).prefetch_related("LikedMovie")

        for movie in likedlists:
            movies2 = movie.LikedMovie.all()

        if movieinstance2 in movies2:
            in_likedlist =True
        else:
            in_likedlist = False
    else:
        in_likedlist = False    
    

    
    return JsonResponse({"in_likedlist": in_likedlist,
                         "in_watchlist": in_watchlist})

def review(request):
    data = json.loads(request.body)

    

    heading = data.get("reviewHeading")
    body = data.get("reviewBody")
    rating = data.get("rating")
    movie = data.get("movieid")
    user = data.get("userid")
    moviename = data.get("moviename")
    posterpath = data.get("posterpath")
    

    userinstance = get_object_or_404(User, pk=user)

    

    if Movie.objects.filter(movieid=movie).first():
        
        movieinstance = Movie.objects.get(movieid=movie)

        existingrvu = Comment.objects.filter(user = userinstance, CommentedOnMovie = movieinstance)

        if existingrvu.first():
            return JsonResponse({"exists": "true",
                                 "success": "false"})
        else:
            review = Comment.objects.create(
                user = userinstance,
                headline = heading,
                text = body,
                rating = rating,
                CommentedOnMovie = movieinstance,
                poster_path = posterpath
            )
            
            movieinstance.comments.add(review)
            return JsonResponse({"success": "true",
                                 "exists": "false"})
        
    else:
        
        new_movie=Movie.objects.create(
            movie_title=moviename,
            poster_path=posterpath,
            movieid=movie
        )
        
        review = Comment.objects.create(
            user = userinstance,
            headline = heading,
            text = body,
            rating = rating,
            CommentedOnMovie = new_movie,
            poster_path = posterpath
        )
        new_movie.comments.add(review)
        return JsonResponse({"success":"true",
                             "exists": "false"})
        
def edit(request):
    
    data = json.loads(request.body)

    

    heading = data.get("reviewHeading")
    body = data.get("reviewBody")
    rating = data.get("rating")
    movie = data.get("movieid")
    user = data.get("userid")
    moviename = data.get("moviename")
    posterpath = data.get("posterpath")
    
    

    userinstance = get_object_or_404(User, pk=user)
    movieinstance = get_object_or_404(Movie, movieid=movie)
    

    review = Comment.objects.filter(user=userinstance, CommentedOnMovie=movieinstance).first()

    review.headline = heading
    review.text = body
    review.rating = rating
    review.save()
    
    return JsonResponse({"edited":"true"})

def delete(request):
    data = json.loads(request.body)

    movieid = data.get("movieid")
    userid  = data.get("userid")
    LorW = data.get("LorW")

    movieinstance = Movie.objects.filter(movieid = movieid).first()
    userinstance = get_object_or_404(User, pk=userid)
    if LorW == "watchlist":
        watchlist = WatchList.objects.filter(user=userinstance).first()
        watchlist.WatcheListMovies.remove(movieinstance)
        
        return JsonResponse({"deleted":"true"})
        

    elif LorW == "likelist":
        likelist = LikedMovies.objects.filter(user=userinstance).first()
        likelist.LikedMovie.remove(movieinstance)
        return JsonResponse({"deleted":"true"})

def tvaddobjectsL(request):
    movie_data = json.loads(request.body)

    moviename = movie_data.get("moviename")
    posterpath = movie_data.get("posterpath")
    user = movie_data.get("user")
    user2 = User.objects.get(pk=user)
    movieid = movie_data.get('movieid')
    
    movie = Tv.objects.filter(movieid = movieid).first()

    if movie:
        user_liked_movies = Likedtv.objects.filter(user=user2)
        if user_liked_movies.exists():
            if movie in user_liked_movies.first().LikedMovie.all():
                user_liked_movies.first().LikedMovie.remove(movie)
                to_grey = True
            else:
                user_liked_movies.first().LikedMovie.add(movie)
                to_grey = False
        else:
            new_likedmovie = Likedtv.objects.create(user=user2)
            new_likedmovie.LikedMovie.add(movie)
            to_grey = False
        
    else:
        new_movie=Tv.objects.create(
            movie_title=moviename,
            poster_path=posterpath,
            movieid=movieid
        )
        

        user_liked_movies2 = Likedtv.objects.filter(user=user2)
        if user_liked_movies2.exists():
            user_liked_movies2.first().LikedMovie.add(new_movie)
            to_grey= False
        else:
            new_likedmovie2 = Likedtv.objects.create(user=user2)
            new_likedmovie2.LikedMovie.add(new_movie)
            to_grey = False

        

    
    return JsonResponse({"to_grey": to_grey})
    
def tvaddobjectsW(request):
    movie_data = json.loads(request.body)

    moviename = movie_data.get("moviename")
    posterpath = movie_data.get("posterpath")
    user = movie_data.get("user")
    user2 = User.objects.get(pk=user)
    movieid = movie_data.get("movieid")
    
    movie = Tv.objects.filter(movieid=movieid).first()

    if movie:
        user_watched_movies = WatchListtv.objects.filter(user=user2)
        if user_watched_movies.exists():
            if movie in user_watched_movies.first().WatcheListMovies.all():
                user_watched_movies.first().WatcheListMovies.remove(movie)
                to_grey = True
            else:
                user_watched_movies.first().WatcheListMovies.add(movie)
                to_grey = False
        else:
            new_watchedmovie = WatchListtv.objects.create(user=user2)
            new_watchedmovie.WatcheListMovies.add(movie)
            to_grey = False
        
    else:
        new_movie=Tv.objects.create(
            movie_title=moviename,
            poster_path=posterpath,
            movieid=movieid
        )
        

        user_watched_movies2 = WatchListtv.objects.filter(user=user2)
        if user_watched_movies2.exists():
            user_watched_movies2.first().WatcheListMovies.add(new_movie)
            to_grey = False
        else:
            new_watchedmovie2 = WatchListtv.objects.create(user=user2)
            new_watchedmovie2.WatcheListMovies.add(new_movie)
            to_grey = False

        

    
    return JsonResponse({"to_grey": to_grey})

def tvexists(request):
    data = json.loads(request.body)

    user = data.get("user")
    userinstance = User.objects.get(pk=user)
    id = data.get("movieid")
    movieinstance = Tv.objects.filter(movieid=id)
    movieinstance2 = movieinstance.first()
    
    watchlist_exists = WatchListtv.objects.filter(user=userinstance).exists()
    

    if (watchlist_exists):
        watchlists = WatchListtv.objects.filter(user=userinstance).prefetch_related("WatcheListMovies")
        
        for movie in watchlists:
            movies = movie.WatcheListMovies.all()
            
            
        if movieinstance2 in movies:
            in_watchlist = True
        else:
            in_watchlist = False
    else:
        in_watchlist = False

    


    liked_exists = Likedtv.objects.filter(user=userinstance).exists()

    if(liked_exists):
        likedlists = Likedtv.objects.filter(user=userinstance).prefetch_related("LikedMovie")

        for movie in likedlists:
            movies2 = movie.LikedMovie.all()

        if movieinstance2 in movies2:
            in_likedlist =True
        else:
            in_likedlist = False
    else:
        in_likedlist = False    
    

    
    return JsonResponse({"in_likedlist": in_likedlist,
                         "in_watchlist": in_watchlist})

def tvreview(request):
    data = json.loads(request.body)

    

    heading = data.get("reviewHeading")
    body = data.get("reviewBody")
    rating = data.get("rating")
    movie = data.get("movieid")
    user = data.get("userid")
    moviename = data.get("moviename")
    posterpath = data.get("posterpath")
    

    userinstance = get_object_or_404(User, pk=user)

    

    if Tv.objects.filter(movieid=movie).first():
        
        movieinstance = Tv.objects.get(movieid=movie)

        existingrvu = Commenttv.objects.filter(user = userinstance, CommentedOnMovie = movieinstance)

        if existingrvu.first():
            return JsonResponse({"exists": "true",
                                 "success": "false"})
        else:
            review = Commenttv.objects.create(
                user = userinstance,
                headline = heading,
                text = body,
                rating = rating,
                CommentedOnMovie = movieinstance,
                poster_path = posterpath
            )
            
            movieinstance.comments.add(review)
            return JsonResponse({"success": "true",
                                 "exists": "false"})
        
    else:
        
        new_movie=Tv.objects.create(
            movie_title=moviename,
            poster_path=posterpath,
            movieid=movie
        )
        
        review = Commenttv.objects.create(
            user = userinstance,
            headline = heading,
            text = body,
            rating = rating,
            CommentedOnMovie = new_movie,
            poster_path = posterpath
        )
        new_movie.comments.add(review)
        return JsonResponse({"success":"true",
                             "exists": "false"})

def tvedit(request):
    data = json.loads(request.body)

    

    heading = data.get("reviewHeading")
    body = data.get("reviewBody")
    rating = data.get("rating")
    movie = data.get("movieid")
    user = data.get("userid")
    moviename = data.get("moviename")
    posterpath = data.get("posterpath")
    
    

    userinstance = get_object_or_404(User, pk=user)
    movieinstance = get_object_or_404(Tv, movieid=movie)
    

    review = Commenttv.objects.filter(user=userinstance, CommentedOnMovie=movieinstance).first()

    review.headline = heading
    review.text = body
    review.rating = rating
    review.save()
    
    return JsonResponse({"edited":"true"})

def deletetv(request):
    data = json.loads(request.body)

    movieid = data.get("movieid")
    userid  = data.get("userid")
    LorW = data.get("LorW")

    movieinstance = Tv.objects.filter(movieid = movieid).first()
    userinstance = get_object_or_404(User, pk=userid)
    if LorW == "watchlist":
        watchlist = WatchListtv.objects.filter(user=userinstance).first()
        watchlist.WatcheListMovies.remove(movieinstance)
        
        return JsonResponse({"deleted":"true"})
        

    elif LorW == "likelist":
        likelist = Likedtv.objects.filter(user=userinstance).first()
        likelist.LikedMovie.remove(movieinstance)
        return JsonResponse({"deleted":"true"})
    