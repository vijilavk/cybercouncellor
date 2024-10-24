# serializers.py in userapp
from account_app.models import *
# serializers.py
from rest_framework import serializers

from councellor_app.models import *
from .models import *

class LogintableSerializer(serializers.ModelSerializer):
    class Meta:
        model=Logintable
        fields=['username','password','user_type']



class UsertableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usertable
        fields = [
            'login_id',
            'name',
            'age',
            'gender',
            'email',
            'place',
            'phone',
            'created_at',
            'updated_at',
            'is_active'
        ]
class LogintableviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Logintable
        fields=['user_type']
class Videoserializer(serializers.ModelSerializer):
    class Meta:
        model=Videotable
        fields=['councellor_logid','title','video_file','description']
class Thoughtserializer(serializers.ModelSerializer):
    class Meta:
        model=Thoughttable
        fields=['councellor_logid','thought']
class Complaintserializer(serializers.ModelSerializer):
    class Meta:
        model=Complainttable
        fields=['login_id','complaint','reply']
class RatingandReviewserializer(serializers.ModelSerializer):
    class Meta:
        model=Ratingandreviewtable
        fields=['login_id','rating','review']
        
class Requestserializer(serializers.ModelSerializer):
    class Meta:
        model=RequestTable
        fields=['councellor_logid','user_logid','request_status']