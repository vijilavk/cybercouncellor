from django.urls import path

from account_app.views import *
from .views import *

urlpatterns = [
    
    path('councellor',Councellorsample.as_view(),name='councellorsample12'),
     path('videoupload',VideoUpload.as_view(),name='videoupload12'),
      path('viewvideoupload',viewvideoupload.as_view(),name='viewvideoupload12'),
       path('thoughtupload',Thoughtupload.as_view(),name='thoughtupload12'),
        path('viewthought',Viewthought.as_view(),name='viewthought12'),
        path('viewreview',Viewreviewandrating.as_view(),name='viewreview12'),
        path('userrequest',Userrequestview.as_view(),name="userrequest12"),
          path('userrequestaccept/<int:lid>/',userrequestaccept.as_view(),name="userrequestaccept12"),
           path('viewusersbycouncellor',viewusersbycouncellor.as_view(),name="viewusersbycouncellor")
       

        
        
     
    ]
