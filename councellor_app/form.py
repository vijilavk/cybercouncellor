from django.forms import ModelForm

from account_app.models import *
from .models import *


class videouploadform(ModelForm):
    class Meta:
        model=Videotable
        fields=[ 'councellor_logid','title','video_file','description']
class thoughtuploadform(ModelForm):
    class Meta:
        model=Thoughttable
        fields=['thought']
    