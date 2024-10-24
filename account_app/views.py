import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate
from account_app.form import councellor
from account_app.models import Councellortable, Logintable, Token

# Create your views here.
class Login(View):
    templates_name = 'admintemp/login.html'

    def get(self, request):
        return render(request, "admintemp/login.html")

    def post(self, request):
        print("$$$$$$$$$$$$$$$$$$$$$")
        response_dict = {"success": False}
        landing_page_url = {
            "Councellor": "councellor12/councellor",
            "ADMIN": "admin12/adminhome"     
            # main url l kodutha name specify cheyyanam 
        }

        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, 'username')
        print(password, 'password******************')

        user = Logintable.objects.filter(username=username).first()
        if not user:
            response_dict["reason"] = "No account found for this username, please sign up."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})

        # Check if the user is inactive
        if not user.is_active:
            response_dict["reason"] = "User is inactive, please contact admin."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})

        # Check if the user type is pending
        if user.user_type == "pending":
            response_dict["reason"] = "User is pending, please contact admin."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user:
            session_dict = {"real_user": user.id}
            token, created = Token.objects.get_or_create(
                user=user, defaults={"session_dict": json.dumps(session_dict)}
            )

            request.session["data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "status": user.is_active,
            }
            print(user)
            print(user.user_type)
            print(f"4444444444444444User Type: {user.user_type}")
            print("session",request.session["data"]["user_id"])
            print(f"77777777777777777Landing Page URLs: {landing_page_url}")
            return redirect(landing_page_url[user.user_type])
        else:
            response_dict["reason"] = "Invalid credentials."
            messages.error(request, response_dict["reason"])
            return render(request, self.templates_name, {"error_message": response_dict["reason"]})

class Registercouncellor(View):
    def get(self, request):
        return render(request, 'counsellortemp/counsellorreg.html')

    def post(self, request):
        frm = councellor(request.POST)
        if frm.is_valid():
            councellorform = frm.save(commit=False)
            lo = Logintable.objects.create_user(username=request.POST["username"], password=request.POST["password"])
            lo.user_type = 'PENDING'
            lo.save()  # Make sure to save the user
            councellorform.login_id = lo
            councellorform.save()
            return HttpResponse('''<script>alert("Inserted successfully")</script>''')
        return HttpResponse('''<script>alert("Invalid")</script>''')

