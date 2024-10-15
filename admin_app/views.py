from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from account_app.models import *
from user_app.models import *


# Create your views here.
class Adminhome(View):
    def get(self,request):
        return render(request,'admintemp/adminhome.html')
class Managecouncellor(View):
    def get(self,request):
         value=Councellortable.objects.filter(is_active=True)
         for i in value:
             print(i.fname)
         return  render(request,"admintemp/managecouncellor.html",{'k':value})
class Acceptcouncellor(View):
    print("dfghjk")
    def get(self, request, lid):
        # Fetch the login object using the login id
        
        obj = Logintable.objects.get(id=lid)
        print(obj)
        print(obj.user_type)
        # Update the usertype to 'counselor'
        obj.user_type = 'Councellor'
        obj.save()
        return HttpResponse('''<script>alert("updated ")</script>''')
class Rejectcouncellor(View):
    print("dfghjk")
    def get(self, request, lid):
        # Fetch the login object using the login id
        
        obj = Logintable.objects.get(id=lid)
        print(obj)
        print(obj.user_type)
        # Update the usertype to 'counselor'
        obj.user_type = 'Rejected'
        obj.save()
        return HttpResponse('''<script>alert("updated ")</script>''')
class Manageuser(View):
    def get(self,request):
         value=Usertable.objects.filter(is_active=True)
         for i in value:
             print(i.name)
         return  render(request,"admintemp/manageuser.html",{'k':value})
class Acceptuser(View):
    print("dfghjk")
    def get(self, request, lid):
        # Fetch the login object using the login id
        
        obj = Logintable.objects.get(id=lid)
        print(obj)
        print(obj.user_type)
        # Update the usertype to 'counselor'
        obj.user_type = 'User'
        obj.save()
        return HttpResponse('''<script>alert("acepted ")</script>''')
class Rejectuser(View):
    print("dfghjk")
    def get(self, request, lid):
        # Fetch the login object using the login id
        
        obj = Logintable.objects.get(id=lid)
        print(obj)
        print(obj.user_type)
        # Update the usertype to 'counselor'
        obj.user_type = 'Rejected'
        obj.save()
        return HttpResponse('''<script>alert("rejected")</script>''')
class Viewcomplaint(View):
    def get(self, request):
        # Use select_related to fetch related user information in a single query
        comp = Complainttable.objects.filter(is_active=True).select_related('login_id__usertable')
        
        # Render the template and pass complaints with related user data
        return render(request, "admintemp/viewcomplaint.html", {'k': comp})
class Complaintreply(View):
    def get(self,request,cid):
        complaint=Complainttable.objects.get(id=cid)
        return render(request, "admintemp/complaintreply.html",{'complaint':complaint})
    def post(self,request,cid):
        try:
         complaint=Complainttable.objects.get(id=cid)
         complaint.reply=request.POST.get('reply')
         complaint.save()
         return redirect('viewcomplaint')  # Redirect after successful reply
        except Complainttable.DoesNotExist:
            return redirect('viewcomplaint')

class Viewreviewandrating(View):
    def get(self, request):
        # Use the correct field names for select_related
        rating = Ratingandreviewtable.objects.all().select_related('login_id__usertable')

        # Render the template and pass the ratings and reviews
        return render(request, "admintemp/ratingandreview.html", {'ra': rating})
