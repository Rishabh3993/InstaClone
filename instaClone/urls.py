from django.conf.urls import url
from django.contrib import admin

from instaapp.views import signup_view
from instaapp.views import login_view
from instaapp.views import feed_view
from instaapp.views import post_view
from instaapp.views import like_view
from instaapp.views import comment_view
from instaapp.views import logout_view

urlpatterns = [url('logout/', logout_view),
               url('comment/', comment_view),
               url('like/', like_view),
               url('post/', post_view),
               url('feed/',feed_view),
               url('login/',login_view),
               url('', signup_view)]