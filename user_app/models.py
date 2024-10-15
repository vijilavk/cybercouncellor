from django.db import models

from account_app.models import Logintable
class Complainttable(models.Model):
    login_id=models.OneToOneField(Logintable,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.CharField(max_length=35,null=True,blank=True)
    reply=models.CharField(max_length=35,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)
class Ratingandreviewtable(models.Model):
    login_id=models.OneToOneField(Logintable,on_delete=models.CASCADE,null=True,blank=True)
    rating=models.CharField(max_length=35,null=True,blank=True)
    review=models.CharField(max_length=35,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    is_active=models.BooleanField(default=True,blank=True,null=True)