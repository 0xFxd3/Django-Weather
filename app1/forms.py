from django import forms
from django.forms import ModelForm
from .models import customerInquiry
from .models import registerModel



class myForm(ModelForm):
    class Meta:
        model = customerInquiry
        fields = {"accountName","email","birthDate","message"}
        label = {"Name","Email","Email","Birthdate","Message"}
        widgets = {
            "accountName":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "dateOfBirth":forms.DateInput(attrs={"class":"form-control"}),
            "Message":forms.TextInput(attrs={"class":"form-control"}),
        }

class registerForm(ModelForm):
    class Meta:
        model = registerModel
        fields = {"accountName","password","email","birthDate","localArea"}
        label = {"Name","Password","Email","Email","Birthdate","Local Location"}
        widgets = {
            "accountName":forms.TextInput(attrs={"class":"form-control","Rows" : 2}),
            "Password":forms.TextInput(attrs={"class":"form-control","Rows" : 2}),
            "area":forms.TextInput(attrs={"class":"form-control","Rows" : 2}),
            "email":forms.EmailInput(attrs={"class":"form-control","Rows" : 2}),
            "dateOfBirth":forms.DateInput(attrs={"class":"form-control","Rows" : 2}),
        }
