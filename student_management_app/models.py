from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, 'root'),(2, 'director'),(3, 'teacher'),(4, 'student'))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)

class Root(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

class Director(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    school = models.OneToOneField(School, on_delete=models.CASCADE)
    objects = models.Manager()

class SchoolClass(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.DO_NOTHING)
    objects = models.Manager()

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    schoolclass = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    objects = models.Manager()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    subject = models.ManyToManyField(Subject)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    objects = models.Manager()


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            Root.objects.create(admin=instance)
        if instance.user_type==2:
            Director.objects.create(admin=instance, school=School.objects.get(id=1))
        if instance.user_type==3:
            Teacher.objects.create(admin=instance)
        if instance.user_type==4:
            Student.objects.create(admin=instance)

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.root.save()
    if instance.user_type==2:
        instance.director.save()
    if instance.user_type==3:
        instance.teacher.save()
    if instance.user_type==4:
        instance.student.save()