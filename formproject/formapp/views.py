from django.shortcuts import render
from .forms import FeedbackForm


# Create your views here.
def show(r):
    form = FeedbackForm()
    my_dict = {'form': form}

    return render(r, 'feedback.html', context=my_dict)
