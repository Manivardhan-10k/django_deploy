from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import bcrypt
import cloudinary 
import cloudinary_storage
from .serializer import UserSerializer
# Create your views here.


def welcome(req):
    return HttpResponse("response from deployment")

@csrf_exempt
def reg_user(request):

    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = request.POST.copy()
        uploaded_file = request.FILES.get("profile_pic")  ## to access the file from request

        # Password validation
        if not data.get("password"):
            return JsonResponse({"error": "Password is required"}, status=400)

        # Hash password
        hashed_pw = bcrypt.hashpw(
            data["password"].encode("utf-8"), bcrypt.gensalt()
        )
        data["password"] = hashed_pw.decode("utf-8")

        # Upload image to Cloudinary if provided
        if uploaded_file:
            result = cloudinary.uploader.upload(
                uploaded_file,
                folder="deployment_folder"  # Cloudinary folder
            )
            data["profile_pic"] = result.get("secure_url")  # store URL in DB

        # Save user
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            return JsonResponse({
                "message": "User registered successfully",
                "profile_pic_url": user.profile_pic
            }, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)