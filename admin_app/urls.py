from django.urls import path

from account_app.views import *
from admin_app.views import *

urlpatterns = [
     
    path('adminhome',Adminhome.as_view(),name="adminhome1"),
    path('managecouncellor',Managecouncellor.as_view(),name="managecouncellor1"),
    path('accept/<int:lid>/',Acceptcouncellor.as_view(),name="acceptcouncellor"),
    path('reject/<int:lid>/',Rejectcouncellor.as_view(),name="rejectcouncellor"),
     path('manageuser',Manageuser.as_view(),name="manageuser1"),
      path('acceptuser/<int:lid>/',Acceptuser.as_view(),name="acceptuser"),
    path('rejectuser/<int:lid>/',Rejectuser.as_view(),name="rejectuser"),
    path('viewcomplaint',Viewcomplaint.as_view(),name="viewcomplaint"),
    path('complaintreply/<int:cid>/',Complaintreply.as_view(),name="complaintreply"),
    path('Viewreviewandrating',Viewreviewandrating.as_view(),name="Viewreviewandrating")
    ]
