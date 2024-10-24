from django.db  import models 

from account_app.models import *

# Create your models here.
class Videotable(models.Model):
    councellor_logid =models.ForeignKey(Logintable,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=35,null=True,blank=True)
    video_file = models.FileField(upload_to='videos/') 
    description = models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)
class Thoughttable(models.Model):
        councellor_logid =models.ForeignKey(Logintable,on_delete=models.CASCADE,null=True,blank=True)
        thought = models.CharField(max_length=35,null=True,blank=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
        is_active=models.BooleanField(default=True,blank=True,null=True)

# class Chattable(models.Model):
#     USER_REQUEST = 'request'
#     COUNSELOR_RESPONSE = 'response'
#     INTERACTION_TYPE_CHOICES = [
#         (USER_REQUEST, 'User Request'),
#         (COUNSELOR_RESPONSE, 'Counselor Response'),
#     ]

#     user = models.ForeignKey(Logintable, on_delete=models.CASCADE)  # Link to the User model (requesting user or counselor)
#     interaction_type = models.CharField(max_length=10, choices=INTERACTION_TYPE_CHOICES)  # Type of interaction
#     text = models.TextField()  # The text of the request or response
#     created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the interaction was created
#     request_id = models.IntegerField(null=True, blank=True) 
class RequestTable(models.Model):
    councellor_logid = models.ForeignKey(Logintable,  on_delete=models.CASCADE, null=True,  blank=True,  related_name='counsellor_requests')
    user_logid = models.ForeignKey( Logintable,  on_delete=models.CASCADE,  null=True, blank=True, related_name='user_requests' )
    request_status = models.CharField(max_length=35, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
