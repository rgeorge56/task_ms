from django.urls import path
from .views import *

urlpatterns = [

    path(
        'login/',
        loginfn,
        name='login'
    ),

    path(
        'register/',
        registerfn,
        name='register'
    ),

    path(
        'logout/',
        logoutfn,
        name='logout'
    ),

]