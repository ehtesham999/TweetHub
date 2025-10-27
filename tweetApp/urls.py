from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name = 'home'),
    path('tweets/', tweet_list, name = 'list'),
    path('tweets/create/', tweet_create, name = 'create'),
    path('tweets/<int:tweet_id>/edit/', tweet_edit, name = 'edit'),
    path('tweets/<int:tweet_id>/delete/', tweet_delete, name = 'delete'),
]