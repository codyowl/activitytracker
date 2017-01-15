from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your Username'}))
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Email'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name')
        
class LoginForm(forms.Form):
	username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your Username'}))
	password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter your Password'}))
