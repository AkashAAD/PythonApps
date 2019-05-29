from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
# import tablib

def home_page(request):
  # print(request.session.get('name', 'Unknown')) getter
  # request.session['name']
  context = {"title": "Hello World!"}
  return render(request, "home_page.html", context)

def about_page(request):
  context = {"title": "About Page!"}
  return render(request, "home_page.html", context)

def contact_page(request):
  # print(request.POST)
  print(request.POST.get('full_name'))

  contact_form = ContactForm(request.POST or None)
  context = {
    "title": "About Page!",
    "content": "Welcome to the contact page.",
    "form": contact_form
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  return render(request, "contact/view.html", context)
