from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CustomUser 
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Register your models here.
class UserModel(UserAdmin):
    pass

def admin_home(request):
    return render(request, "admin_template/admin_home.html")

def add_admin(request):
    return render(request, "admin_template/add_admin.html")

def save_admin(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=1, is_superuser=1)
            user.save()
            messages.success(request,"Successfully Added Admin")
            return HttpResponseRedirect(reverse("add_admin"))
        except:
            messages.error(request,"Failed to Add Admin")
            return HttpResponseRedirect(reverse("add_admin"))

admin.site.register(CustomUser, UserModel)
