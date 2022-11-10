from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib import messages

class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"type":"email", 'name':"email", 'class':"form-control", "id":"yourEmail"}), required=True, )
    username = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'name':"username", 'class':"form-control", 'id':"yourUsername"}),required= True, max_length=30)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'name':"nome", 'class':"form-control", 'id':"yourName"}), max_length=40)
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"type":"password", 'name':"passwordconfirm", 'class':"form-control", 'id':"yourPassword"}), help_text=password_validation.password_validators_help_text_html())
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"type":"password", 'name':"passwordconfirm", 'class':"form-control", 'id':"yourPassword2"}))

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']    


    def clean_password2(request, self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            messages.error(request, "")
        return password2
    
    def save(self, commit=True):
        user = super(NovoUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'type':"text", 'name':'username', 'class':'form-control', 'id':'yourUsername'}))
    password = forms.CharField(widget=
    forms.PasswordInput(attrs={'type':'password', 'name':"password", 'class':'form-control', 'id':'yourPassword'}))

    