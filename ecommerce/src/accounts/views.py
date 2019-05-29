from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import GuestEmail
from .forms import LoginForm, RegisterForm, GuestForm
from django.utils.http import is_safe_url

def guest_register_view(request):
  guest_email_form = GuestForm(request.POST or None)
  context    = { "form": guest_email_form }

  next_ = request.GET.get('next')
  next_post = request.POST.get('next')
  redirect_path = next_ or next_post or None

  if guest_email_form.is_valid():
    email     = guest_email_form.cleaned_data.get("email")
    new_guest_email = GuestEmail.objects.create(email=email)
    request.session['guest_email_id'] = new_guest_email.id
    if is_safe_url(redirect_path, request.get_host()):
      return redirect(redirect_path)
    else:
      return redirect("/register/")
  return redirect("/register/")


# Create your views here.
def login_page(request):
  login_form = LoginForm(request.POST or None)
  context    = { "form": login_form }

  next_ = request.GET.get('next')
  next_post = request.POST.get('next')
  redirect_path = next_ or next_post or None

  if login_form.is_valid():
    user_name = login_form.cleaned_data.get("user_name")
    password  = login_form.cleaned_data.get("password")
    user = authenticate(request, username=user_name, password=password)
    # import pdb; pdb.set_trace()
    if user is not None:
      login(request, user)
      try:
        del request.session['guest_email_id']
      except:
        pass
      if is_safe_url(redirect_path, request.get_host()):
        return redirect(redirect_path)
      else:
        return redirect("/")
    else:
      print("Error")

  return render(request, "accounts/login.html", context)

User = get_user_model()

def register_page(request):
  register_form    = RegisterForm(request.POST or None)
  context = { "form": register_form }
  if register_form.is_valid():
    print(register_form.cleaned_data)
    user_name = register_form.cleaned_data.get("user_name")
    email = register_form.cleaned_data.get("email")
    password  = register_form.cleaned_data.get("password")
    new_user = User.objects.create_user(user_name, email, password)
    print(new_user)
  return render(request, "accounts/register.html", context)