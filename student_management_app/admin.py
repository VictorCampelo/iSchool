from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CustomUser, School, Director
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from student_management_app.forms import AddDirectorForm

# Register your models here.
class UserModel(UserAdmin):
    pass

def admin_home(request):
    return render(request, "admin_template/admin_home.html")
def add_admin(request):
    return render(request, "admin_template/add_admin.html")
def add_director(request):
    form=AddDirectorForm()
    return render(request, "admin_template/add_director.html", {"form":form})
def add_student(request):
    return render(request, "admin_template/add_student.html")
def add_teacher(request):
    return render(request, "admin_template/add_teacher.html")
def add_school(request):
    return render(request, "admin_template/add_school.html")

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

def save_school(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name=request.POST.get("name")
        try:
            school=School(name=name)
            school.save()
            messages.success(request,"Successfully Added School")
            return HttpResponseRedirect(reverse("add_school"))
        except:
            messages.error(request,"Failed to Add School")
            return HttpResponseRedirect(reverse("add_school"))

def save_director(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddDirectorForm(request.POST,request.FILES)
        if form.is_valid():
            first_name=form.cleaned_data["first_name"]
            last_name=form.cleaned_data["last_name"]
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            school_id=form.cleaned_data["school"]
            try:
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
                schoolobj=School.objects.get(id=school_id)
                user.director.school=schoolobj
                user.save()
                messages.success(request,"Successfully Added Director")
                return HttpResponseRedirect(reverse("add_director"))
            except:
                messages.error(request,"Failed to Add Director")
                return HttpResponseRedirect(reverse("add_director"))
        
def save_student(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=4, is_superuser=0)
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        except:
            messages.error(request,"Failed to Add Student")
            return HttpResponseRedirect(reverse("add_student"))

def save_teacher(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3, is_superuser=0)
            user.save()
            messages.success(request,"Successfully Added Teacher")
            return HttpResponseRedirect(reverse("add_teacher"))
        except:
            messages.error(request,"Failed to Add Teacher")
            return HttpResponseRedirect(reverse("add_teacher"))

admin.site.register(CustomUser, UserModel)
