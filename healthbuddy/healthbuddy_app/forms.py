from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
# from django.contrib.auth.models import User 
from django import forms 
from .models import AddUserData

class CustomUserForm(UserCreationForm):
    GENDER_CHOICES = [
        ('', 'Select'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    BLOOD_GROUP=[
        ('', 'Select'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB+', 'AB-'),
    ]

    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'name': 'firstName'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'name': 'lName'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobileNumber = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'mobNo'}))
    dob=forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'name': 'dob'}))
    height=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'name': 'height'}))
    weight=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control', 'name': 'weight'}))
    bloodGroup = forms.ChoiceField(choices=BLOOD_GROUP, required=True,widget=forms.Select(attrs={'class': 'form-control', 'name': 'bloodGroup'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control', 'name': 'gender'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = AddUserData
        fields = ['first_name','last_name','email','mobileNumber','dob','height','weight','bloodGroup','gender','password1','password2']

class AuthenticateLogin(AuthenticationForm):
    username=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control w-100'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control w-100 py-1'}))