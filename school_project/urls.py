"""school_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from student_management_app import views, admin
from school_project import settings

urlpatterns = [
    path('demo', views.showDemoPage),
    path('', views.showLoginPage),
    path('doLogin',views.doLogin),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('admin_home',admin.admin_home,name="admin_home"),
    path('add_admin',admin.add_admin,name="add_admin"),
    path('add_director',admin.add_director,name="add_director"),
    path('add_student',admin.add_student,name="add_student"),
    path('add_teacher',admin.add_teacher,name="add_teacher"),
    path('add_school',admin.add_school,name="add_school"),

    path('save_admin',admin.save_admin,name="save_admin"),
    path('save_director',admin.save_director,name="save_director"),
    path('save_teacher',admin.save_teacher,name="save_teacher"),
    path('save_student',admin.save_student,name="save_student"),
    path('save_school',admin.save_school,name="save_school"),
]+static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
