from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import signupform
from django.http import HttpResponseRedirect

# Create your views here.
def home(r):
    return render(r,'loanapp/base.html')
def about(r):
    return render(r,'loanapp/about.html')
def contact(r):
    return render(r,'loanapp/contact.html')
@login_required
def homeloan(r):
    return render(r,'loanapp/homeloan.html')
@login_required
def carloan(r):
    return render(r,'loanapp/carloan.html')
@login_required
def creditcard(r):
    return render(r,'loanapp/creditcard.html')
def logout(r):
    return render(r,'loanapp/logout.html')

def signup(r):
    if r.method == 'POST':
       form = signupform(r.POST)
       if form.is_valid():
           user=form.save(commit=True)
           user.set_password(user.password)
           user.save()
           return HttpResponseRedirect('/accounts/login')
    else:
        form = signupform()
    return render(r,'loanapp/signup.html',{'form':form})