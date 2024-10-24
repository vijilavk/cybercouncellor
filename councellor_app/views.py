
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages

from user_app.models import *

from .form  import *

class Councellorsample(View):
    def get(self,request):
         return render(request, "counsellortemp/councellorhome.html")

class VideoUpload(View):
    def get(self, request):
        # Display the form for video upload
        return render(request, 'counsellortemp/videoupload.html')

    def post(self, request):
    # Process the form submission for video upload
        form = videouploadform(request.POST, request.FILES)  # Handle both text and file inputs
        if form.is_valid():
           video_instance = form.save(commit=False)  # Create a video instance but don't save yet
           video_instance.councellor_logid = request.user  # Assign the counselor's login ID
           print("Counselor Log ID:", video_instance.councellor_logid)
           video_instance.save()  # Save the video object to the database
           messages.success(request, "Video uploaded successfully.")
           return redirect('councellorsample12')  # Redirect to a page showing the list of videos (create this view separately)
        else:
           messages.error(request, "Failed to upload video. Please correct the errors below.")
           return render(request, 'videoupload.html')
class viewvideoupload(View):
    def get(self, request):
        # Display the form for video upload
        vi=Videotable.objects.all()
        return render(request, 'counsellortemp/viewuploadedvideo.html',{'videos':vi})
# class deletevideo(View)
class Thoughtupload(View):
    def get(self,request):
        return render(request,'counsellortemp/thoughtupload.html')
    def post(self,request):
        form=thoughtuploadform(request.POST)
        if form.is_valid:
            thoughtins=form.save(commit=False)
            thoughtins.councellor_logid=request.user
            thoughtins.save()
            messages.success(request, "Thought uploaded successfully.")
            return redirect('councellorsample12')
class Viewthought(View):
    def get(self,request):
        thought=Thoughttable.objects.all()
        return render(request,'counsellortemp/viewthought.html',{'thought':thought})
class Viewreviewandrating(View):
    def get(self, request):
        # Use the correct field names for select_related
        rating = Ratingandreviewtable.objects.all().select_related('login_id__usertable')

        # Render the template and pass the ratings and reviews
        return render(request, "counsellortemp/ratingandreview.html", {'ra': rating})
# class Manageuser(View):
#     def get(self,request):
#          value = Usertable.objects.filter(login_id__user_type="User")
#          for i in value:
#             print(i.name)
#          return  render(request,"counsellortemp/manageuser.html",{'k':value})


class Userrequestview(View):
    def get(self, request):
        # Check if 'data' exists in session and contains 'user_type'
        if "data" in request.session and "user_type" in request.session["data"]:
            # Debugging: Print user type and username from the session
            print(f"Logged-in user type: {request.session['data']['user_type']}")
            print(f"Logged-in username: {request.session['data']['username']}")

            # Ensure the user is a counselor
            if request.session["data"]["user_type"] == 'Councellor':  # Or 'councellor' depending on DB value
                try:
                    # Fetch the counselor's record from Councellortable using the logged-in user's ID
                    counselor = Councellortable.objects.get(login_id=request.session["data"]["user_id"])
                    counselor_login_id = counselor.login_id.id  # This should give you the correct ID

                    print(f"Correct Counselor Login ID: {counselor_login_id}")

                    # Filter requests assigned to this counselor
                    user_requests = RequestTable.objects.filter(councellor_logid=counselor_login_id).select_related('user_logid')
                    print("request",user_requests)

                    return render(request, 'counsellortemp/userrequest.html', {'requests': user_requests})
                except Councellortable.DoesNotExist:
                    print("Counselor not found.")
                    return HttpResponse("Counselor record not found.")
            else:
                print("User is not a counselor.")
                return HttpResponse("You are not authorized to view this page.")
        else:
            print("Session data is missing or incomplete.")
            return HttpResponse("Session data is missing or incomplete.")
class userrequestaccept(View):
    def get(self, request, lid):
        # Fetch the login object using the login id
        
        obj = RequestTable.objects.get(id=lid)
        print(obj)
        print(obj.request_status)
        
        obj.request_status = 'accepted'
        obj.save()
        return HttpResponse('''<script>alert("accepted ")</script>''')
class viewusersbycouncellor(View):
    def get(self,request):
      accepted_requests = RequestTable.objects.filter(request_status='accepted').select_related('user_logid')
      for i in accepted_requests:
           print(i.user_logid.usertable.name)
      return  render(request,"counsellortemp/manageuser.html",{'k':accepted_requests})
        
        
    
            
        
        