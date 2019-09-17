from django import forms
from .models import Chat_model
# from django.core import validators


# Create your models here.
class Chat_form(forms.ModelForm):
    conversation = forms.CharField(
        # validators=[validators.validate_slug],
        label='conversation',
        max_length=240)

    class Meta:
        model = Chat_model
        fields = ['conversation']
