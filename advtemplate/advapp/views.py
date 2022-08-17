from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# Create your views here.
def index(r):
    return render(r,'advapp/index.html')
def about(r):
    return render(r,'advapp/about.html')
def contact(r):
    return render(r,'advapp/contact.html')
# @login_required
def python(r):
    return render(r,'advapp/python.html')
def java(r):
    return render(r,'advapp/java.html')