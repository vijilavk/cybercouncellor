from django.shortcuts import render
from rest_framework  import status
from rest_framework.views import APIView
from rest_framework.response import Response

from user_app.serializer import *


class RegisterUserView(APIView):
    def post(self, request):
        print("%%%%%%%%%%%%%%%%%%%%%%")
        # Extract all data under the key 'userreg'
        userreg_data = request.data.get('userreg')
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@", userreg_data)

        # Step 1: Prepare the data for Logintable
        login_data = {
            'username': userreg_data.get('username'),
            'password': userreg_data.get('password'),
            'user_type': userreg_data.get('user_type')
        }

        # Create the serializer for Logintable
        login_serializer = LogintableSerializer(data=login_data)

        if login_serializer.is_valid():
            # Save login data to Logintable
            login_instance = login_serializer.save()
            login_instance.set_password(userreg_data.get('password'))  # Hash the password
            login_instance.save()  # Save the instance again

            # Step 2: Prepare the data for Usertable
            user_data = {
                'name': userreg_data.get('name'),
                'age': userreg_data.get('age'),
                'gender': userreg_data.get('gender'),
                'place': userreg_data.get('place'),
                'phone': userreg_data.get('phone'),
                'login_id': login_instance.id
            }

            # Create the serializer for Usertable
            user_serializer = UsertableSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({
                    'login': login_serializer.data,
                    'user': user_serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                print("User errors:", user_serializer.errors)  # Log user errors
                return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        print("Login errors:", login_serializer.errors)  # Log login errors
        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllCounselorsView(APIView):
    def get(self, request):
        # Fetch all counselors based on the user_type being 'councellor' in Logintable
        login_counselors = Logintable.objects.filter(user_type='Councellor')
        
        # Create an empty list to store the combined data for each counselor
        counselor_data = []
        
        # Iterate through each counselor's login data
        for login_data in login_counselors:
            # Fetch the corresponding profile data from Councellortable
            try:
                counselor_profile = Councellortable.objects.get(login_id=login_data)
                
                # Serialize both the login data and counselor profile data
                login_serializer = LogintableviewSerializer(login_data)
                profile_serializer = UsertableSerializer(counselor_profile)
                
                # Combine the serialized data and append to the list
                counselor_data.append({
                    "login_data": login_serializer.data,
                    "counselor_profile_data": profile_serializer.data,
                })
                
            except Councellortable.DoesNotExist:
                # If there's no profile data for this counselor, skip it
                continue

        # Return the combined data for all counselors
        return Response(counselor_data, status=status.HTTP_200_OK)
class Getallmotivationalvideos(APIView):
    def get(self, request):
     try:  
        videos=Videotable.objects.filter(is_active=True)
         # If no active videos are found, return a 204 No Content status
        if not videos.exists():
                return Response({"detail": "No videos found."}, status=status.HTTP_204_NO_CONTENT)
            
            # Serialize the queryset
        vserialiser = Videoserializer(videos, many=True)
        # videodata=[]
        # for i in videos:
        #     vserialiser=Videoserializer(i) instead of this we can use many=True too vconvert all data to serialised model,here inthis line iterate one by one field using for loop and convert taht to serialised form ,isted of that we use many=True and convert all in once
        #     videodata.append(vserialiser)
        
        return Response(vserialiser.data,status=status.HTTP_200_OK)
     except Exception as e:
            # In case of any error, return a 500 Internal Server Error with the error message
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class Getallmotivationalthoughts(APIView):
    def get(self,request):
     try:  
        thoughts=Thoughttable.objects.filter(is_active=True)
         # If no active videos are found, return a 204 No Content status
        if not thoughts.exists():
                return Response({"detail": "No thoughts found."}, status=status.HTTP_204_NO_CONTENT)
            
            # Serialize the queryset
        tserialiser = Thoughtserializer(thoughts, many=True)
        # videodata=[]
        # for i in videos:
        #     vserialiser=Videoserializer(i) instead of this we can use many=True too vconvert all data to serialised model,here inthis line iterate one by one field using for loop and convert taht to serialised form ,isted of that we use many=True and convert all in once
        #     videodata.append(vserialiser)
        
        return Response(tserialiser.data,status=status.HTTP_200_OK)
     except Exception as e:
            # In case of any error, return a 500 Internal Server Error with the error message
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Addcomplaint(APIView):
    def post(self, request):
        # # Get login ID and description from the request body
        # login_id = request.data.get('login_id')
        # complaint = request.data.get('complaint')

        # # Validate the input
        # if not login_id or not complaint:
        #     return Response({"error": "Login ID and complaint are required"}, status=status.HTTP_400_BAD_REQUEST)

        # # Retrieve the user using the login_id
        # try:
        #     user = Logintable.objects.get(id=login_id)  # Use the correct model here
        # except Logintable.DoesNotExist:
        #     return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # # Create a new complaint with the foreign key set correctly
        # complaint_data = {
        #     'login_id': user,  # Use the user object directly since it's a OneToOneField
        #     'complaint': complaint,
        # }

        serializer = Complaintserializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewComplaintAndReply(APIView):  # Class names should typically be in CamelCase
    def get(self, request, lid):
        try:
            # Fetch complaints related to the provided login_id (lid)
            valu = Complainttable.objects.filter(login_id=lid)
            print("vallllllllll", valu)

            # Check if there are any complaints
            if not valu.exists():
                return Response({"detail": "No complaint and reply."}, status=status.HTTP_204_NO_CONTENT)

            # Serialize the queryset with many=True to handle multiple objects
            complaints = Complaintserializer(valu, many=True)
            print("cccccc", complaints.data)

            # Return the serialized data
            return Response(complaints.data, status=status.HTTP_200_OK)

        except Exception as e:
            # In case of any error, return a 500 Internal Server Error with the error message
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class Addreviewandrating(APIView):
    def post(self,request):
        serialiser=RatingandReviewserializer(data=request.data)

        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)

        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

class Sendrequest(APIView):
    def post(self,request):
        ser=Requestserializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)


class Viewuserprofile(APIView):
    def get(self, request, lid):
        try:
            # Try to get the user with the given login_id
            val = Usertable.objects.get(login_id=lid)
            print(val)

            # Serialize the single object (no need for many=True since it's not a queryset)
            user = UsertableSerializer(val)
            print(user)
            # Return the serialized data with a 200 status
            return Response(user.data, status=status.HTTP_200_OK)

        except Usertable.DoesNotExist:
            # If no user is found, return a 404 response
            return Response({"detail": "No user found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            # Catch any other errors and return a 500 response
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
class UpdateUserProfile(APIView):

    def put(self, request, lid):
        try:
            user = Usertable.objects.get(login_id=lid)
            serializer = UsertableSerializer(user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Usertable.DoesNotExist:
            return Response({"detail": "No user found."}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

