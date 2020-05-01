from django import forms

from student_management_app.models import School

class DateInput(forms.DateInput):
    input_type = "date"

class AddDirectorForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    password=forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    school=School.objects.all()
    school_list=[]
    for schools in school:
        small_school=(schools.id,schools.name)
        school_list.append(small_school)

    school=forms.ChoiceField(label="School",choices=school_list,widget=forms.Select(attrs={"class":"form-control"}))
    