from django.shortcuts import render
from .forms import FeedbackForm
from django.http import HttpResponse

# Create your views here.


def show(r):
    form = FeedbackForm()
    my_dict = {'forms': form}
    if r.method=="POST":
        form=FeedbackForm(r.POST)
        if form.is_valid():
            form.save(commit=True)
        return HttpResponse('<h1>data submit successfully</h1>')

    return render (r,'feedback.html', context=my_dict)
