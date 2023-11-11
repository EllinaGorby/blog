from django.urls import path

import articles
from .views import login_views

app_name = 'users'
urlpatterns = [
    path('login', login_views, name='login'),
    ]


