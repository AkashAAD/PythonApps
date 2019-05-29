from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from .forms import NewUserForm

#Home Page
def homepage(request):
    return render(request = request,
                  template_name='main/categories.html',
                  context = {"categories": TutorialCategory.objects.all()})

#Single slug
def single_slug(request, single_slug):
  categories = [c.category_slug for c in TutorialCategory.objects.all()]
  if single_slug in categories:
    return HttpResponse(f"{single_slug} as a category")

  tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
  if single_slug in tutorials:
    return HttpResponse(f"{single_slug} is a Tutorial")
  return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")

#Login User
def login_request(request):
  if request.method == "POST":
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f"you are now logged in as {username}")
        return redirect("/")
      else:
        messages.error(request, "Invalid username or password")
    else:
      messages.error(request, "Invalid username or password")

  form = AuthenticationForm()
  return render(request = request,
                template_name = "main/login.html",
                context={"form": form})

#Register & Login User
def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f"New account created: {username}")
      login(request, user)
      return redirect("main:homepage")
    else:
      for msg in form.error_messages:
        messages.error(request, f"{msg}: {form.error_messages[msg]}")
      return render(request = request,
                    template_name = "main/register.html",
                    context={"form":form})

  form = UserCreationForm
  return render(request = request,
                template_name = "main/register.html",
                context = {"form": form})

#Logout User
def logout_request(request):
  logout(request)
  messages.info(request, "Logged out successfully!")
  return redirect("main:homepage")

