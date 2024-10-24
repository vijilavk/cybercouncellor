from django.urls import path

from account_app.views import *
from user_app.views import *

urlpatterns = [
    
    
    path('adduser', RegisterUserView.as_view(), name='user-create'),
     path('getallcouncellor', GetAllCounselorsView.as_view(), name='getallcouncellor12'),
     path('getallvideos', Getallmotivationalvideos.as_view(), name='getallvideos12'),
     path('getallthoughts', Getallmotivationalthoughts.as_view(), name='getallthoughts12'),
     path('addcomplaint', Addcomplaint.as_view(), name='addcomplaint12'),
     path('viewcomplaint/<int:lid>/', ViewComplaintAndReply.as_view(), name='viewcomplaint12'),
     path('addreview', Addreviewandrating.as_view(), name='addreview12'),
     path('sendrequest', Sendrequest.as_view(), name='sendrequest12'),
     path('viewuserprofile/<int:lid>/', Viewuserprofile.as_view(), name='viewuserprofile12'),
     path('updateuserprofile/<int:lid>/', UpdateUserProfile.as_view(), name='updateuserprofile12'),





     
     
    
]
    
