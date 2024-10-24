from django.urls import path

from account_app.views import *

urlpatterns = [
    path('',Login.as_view(),name="login"),
    path('register', Registercouncellor.as_view(), name='register1')
     
    ]
