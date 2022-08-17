from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    mobile = forms.IntegerField()
    email = forms.EmailField()
    date = forms.DateField()
