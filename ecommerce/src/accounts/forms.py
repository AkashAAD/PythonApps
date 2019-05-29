from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestForm(forms.Form):
  email = forms.CharField()


class LoginForm(forms.Form):
  user_name = forms.CharField()
  password  = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
  user_name           = forms.CharField()
  email               = forms.CharField()
  password            = forms.CharField(widget=forms.PasswordInput)
  confirmed_password  = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

  def clean_user_name(self):
    user_name = self.cleaned_data.get("user_name")
    qs = User.objects.filter(username=user_name)
    if qs.exists():
      raise forms.ValidationError("Username is already taken.")
    return user_name

  def clean_email(self):
    email = self.cleaned_data.get("email")
    qs = User.objects.filter(email=email)
    if qs.exists():
      raise forms.ValidationError("Email is already taken.")
    return email

  def clean(self):
    data = self.cleaned_data
    password = self.cleaned_data.get('password')
    confirmed_password = self.cleaned_data.get('confirmed_password')

    if password != confirmed_password:
      raise forms.ValidationError("Passwords must match.")
    return data

