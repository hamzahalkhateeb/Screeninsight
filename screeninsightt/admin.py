from django.contrib import admin

from .models import Movie, LikedMovies, WatchList, Comment, Reply, Tv, Likedtv, WatchListtv, Commenttv, Replytv

admin.site.register(Movie)
admin.site.register(LikedMovies)
admin.site.register(WatchList)
admin.site.register(Comment)
admin.site.register(Reply)

admin.site.register(Tv)
admin.site.register(Likedtv)
admin.site.register(WatchListtv)
admin.site.register(Commenttv)
admin.site.register(Replytv)
