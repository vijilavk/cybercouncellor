from django.forms import ModelForm

from account_app.models import *


class councellor(ModelForm):
    class Meta:
        model=Councellortable
        fields=['fname','lname','age','gender','email','place','phone','pincode','district','state','qualification']
    