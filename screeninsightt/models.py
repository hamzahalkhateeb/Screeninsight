from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass


class Movie(models.Model):
    
    movie_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=5000)
    movieid = models.CharField(max_length=10, null=True)
    comments = models.ManyToManyField("Comment")

    def __str__(self):
        return f"{self.movie_title} id: {self.movieid}"
    

class LikedMovies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LikedMovie = models.ManyToManyField(Movie)

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    WatcheListMovies = models.ManyToManyField(Movie)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    CommentedOnMovie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.CharField(max_length = 5000)
    rating = models.IntegerField(null=True)
    poster_path = models.CharField(max_length=5000, null=True)


class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    RepliedToComment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)


#########################################################################################
    
class Tv(models.Model):
    
    movie_title = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=5000)
    movieid = models.CharField(max_length=10, null=True)
    comments = models.ManyToManyField("Commenttv")

    def __str__(self):
        return f"{self.movie_title} id: {self.movieid}"
    

class Likedtv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LikedMovie = models.ManyToManyField(Tv)

class WatchListtv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    WatcheListMovies = models.ManyToManyField(Tv)

class Commenttv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    CommentedOnMovie = models.ForeignKey(Tv, on_delete=models.CASCADE)
    text = models.CharField(max_length = 5000)
    rating = models.IntegerField(null=True)
    poster_path = models.CharField(max_length=5000, null=True)


class Replytv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    RepliedToComment = models.ForeignKey(Commenttv, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)