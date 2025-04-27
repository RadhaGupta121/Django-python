
from django.urls import path , include
from . import views

urlpatterns = [ 
    path('',views.home,name='home'),
    path('newTweet/',views.newTweet, name='newTweet'),
    path('profile/',views.profile, name='profile'),
    path('alltweets/',views.allTweets,name='alltweets'),
    path('<int:tweet_id>/editTweet/',views.editTweet,name='editTweet'),
    path('<int:tweet_id>/deleteTweet/',views.deleteTweet,name='deleteTweet'),
    path('register/',views.registerUser,name='registerUser'),
    path('searchbyUser/',views.searchbyUser, name='searchbyUser')
    
]