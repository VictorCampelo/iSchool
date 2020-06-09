from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from student_management_app.models import CustomUser, School, Director, Subject, SchoolClass
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from student_management_app.forms import *
import traceback
# Register models here.
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
    context = {}
    school = request.GET.get('school')
    context['form'] = SchoolForm(school)
    return render(request, 'admin_template/add_student.html', context)

def load_class(request):
    school = request.GET.get('school')
    classes = SchoolClass.objects.filter(school=school)
    return render(request, 'admin_template/class_list.html', {'class': classes})

def load_teacher(request):
    school = request.GET.get('school')
    teachers = Teacher.objects.filter(school=school)
    return render(request, 'admin_template/teacher_list.html', {'teacher': teachers})

def add_teacher(request):
    form=AddDirectorForm()
    return render(request, "admin_template/add_teacher.html", {"form":form})

def add_school(request):
    form=AddSchoolForm()
    return render(request, "admin_template/add_school.html", {"form":form})

def add_class(request):
    form=AddClassForm()
    return render(request, "admin_template/add_class.html", {"form":form})

def add_subject(request):
    context = {}
    school = request.GET.get('school')
    context['form'] = AddSubjectForm(school)
    return render(request, 'admin_template/add_subject.html', context)

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
        form=AddSchoolForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data["name"]
            level=form.cleaned_data["level"]
            try:
                school=School(name=name, level=level)
                school.save()
                if level == '1':
                    for i in range(1,4):
                        for j in range(1,4):
                            classes=SchoolClass(name=str(i)+"º Ano", serie=i, shift=j, school=school)
                            classes.save()
                elif level == '2':
                     for i in range(5,9):
                        for j in range(1,4):
                            classes=SchoolClass(name=str(i)+"ª Série Fundamental", serie=i, shift=j, school=school)
                            classes.save()
                else:
                    for i in range(1,5):
                        for j in range(1,4):
                            classes=SchoolClass(name=str(i)+"ª Série Básico", serie=i, shift=j, school=school)
                            classes.save()

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

def save_class(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        form=AddDirectorForm(request.POST,request.FILES)
        if form.is_valid():
            school_id=form.cleaned_data["school"]
            serie=form.cleaned_data["serie"]
            shift=form.cleaned_data["shift"]
            try:
                school = School.objects.get(id=school_id)

                if school.level == '1':
                    name = str(serie)+"º Ano"
                else:
                    name = str(serie)+"ª Série"

                schoolClass=SchoolClass(name=name,school=school_id, serie=serie, shift=shift)
                schoolClass.save()
                messages.success(request,"Successfully Added Class")
                return HttpResponseRedirect(reverse("add_class"))
            except:
                messages.error(request,"Failed to Add Class")
                return HttpResponseRedirect(reverse("add_class"))
        
def save_student(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        class_id=request.POST.get("classes")
        try:
            print(request.POST)
            user = CustomUser.objects.create_user(username=username,
                password=password,
                email=email,
                last_name=last_name,
                first_name=first_name,
                user_type=4, 
                is_superuser=0)
            print(user)
            schoolobj=SchoolClass.objects.get(id=class_id)
            user.student.schoolclass=schoolobj
            user.save()
            messages.success(request,"Successfully Added Student")
            return HttpResponseRedirect(reverse("add_student"))
        except Exception: 
            traceback.print_exc()
            messages.error(request,"Failed to Add Student")
            return HttpResponseRedirect(reverse("add_student"))

def save_subject(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        name=request.POST.get("name")
        class_id=request.POST.get("classes")
        teacher_id=request.POST.get("teachers")

        try:
            schoolObj=SchoolClass.objects.get(id=class_id)
            teacherObj=Teacher.objects.get(id=teacher_id)

            subject=Subject(name=name,schoolclass=schoolObj, teacher=teacherObj)
            subject.save()
            messages.success(request,"Successfully Added Subject")
            return HttpResponseRedirect(reverse("add_subject"))
        except Exception: 
            traceback.print_exc()
            messages.error(request,"Failed to Add Subject")
            return HttpResponseRedirect(reverse("add_subject"))

def save_teacher(request):
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
                user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=3)
                schoolobj=School.objects.get(id=school_id)
                user.teacher.school=schoolobj
                user.save()
                messages.success(request,"Successfully Added Teacher")
                return HttpResponseRedirect(reverse("add_teacher"))
            except:
                messages.error(request,"Failed to Add Teacher")
                return HttpResponseRedirect(reverse("add_teacher"))

admin.site.register(CustomUser, UserModel)
