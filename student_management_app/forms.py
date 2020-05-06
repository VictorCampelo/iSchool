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

class AddClassForm(forms.Form):
    school=School.objects.all()
    school_list=[]
    for schools in school:
        small_school=(schools.id,schools.name)
        school_list.append(small_school)
    sr = [
    (1, "1ª Série"), 
    (2, "2ª Série"), 
    (3, "3ª Série"), 
    (4, "4ª Série"),
    (5, "5ª Série"), 
    (6, "6ª Série"), 
    (7, "7ª Série"), 
    (8, "8ª Série"),  
    (9, "1º Ano "),
    (10, "2º Ano"),
    (11, "3º Ano")]
    sb=[
        (1, "A"),
        (2, "B"),
        (3, "C"), 
        (4, "D"),
        (5, "E")]
    tr=[(1, 'Manhã'), (2, 'Tarde'), (3, "Noite")]
    school=forms.ChoiceField(label="School",choices=school_list,widget=forms.Select(attrs={"class":"form-control"}))
    serie=forms.ChoiceField(label="Serie",choices=sr,widget=forms.Select(attrs={"class":"form-control"}))
    shift=forms.ChoiceField(label="Shift",choices=tr,widget=forms.Select(attrs={"class":"form-control"}))
    subclass=forms.ChoiceField(label="Subclass",choices=sb,widget=forms.Select(attrs={"class":"form-control"}))
    
class AddSchoolForm(forms.Form):
    name=forms.CharField(label="Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    level=forms.ChoiceField(label="Level",choices=[(1, 'Médio'), (2, 'Fundamental')],widget=forms.Select(attrs={"class":"form-control"}))