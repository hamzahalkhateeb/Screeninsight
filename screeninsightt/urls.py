from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tvshows", views.tv, name="tvshows"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('movieDetails/<int:movieid>', views.movieDetails, name='movieDetails'),
    path('tvdetails/<int:movieid>', views.tvdetails, name='tvdetails'),
    path("genrePage/<int:genreid>", views.genrePage, name="genrePage"),
    path("genrePagetv/<int:genreid>", views.genrePagetv, name="genrePagetv"),
    path("addobjectL", views.addobjectL, name="addobjectL"),
    path("addobjectW", views.addobjectW, name="addobjectL"),
    path('filter', views.filter, name="filter"), 
    path('filtertv', views.filtertv, name="filtertv"),
    path('basicsearch', views.basicsearch, name="basicsearch"),
    path('basicsearchtv', views.basicsearchtv, name="basicsearchtv"),
    path('profile', views.profile, name="profile"),
    path('exists', views.exists, name="exists"),
    path('review', views.review, name="review"),
    path('edit', views.edit, name="edit"), 
    path('delete', views.delete, name="delete"),
    path('tvaddobjectsL', views.tvaddobjectsL, name="tvaddobjectsL"),
    path('tvaddobjectsW', views.tvaddobjectsW, name="tvaddobjectsW"),
    path('tvexists', views.tvexists, name="tvexists"),
    path('tvreview', views.tvreview, name="tvreview"),
    path('tvedit', views.tvedit, name="tvedit"),
    path('deletetv', views.deletetv, name="deletetv"),
]
