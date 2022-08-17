from django import forms
from .models import ModelFeedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ModelFeedback
        fields = "__all__"
        # field = ('name','mobile')
