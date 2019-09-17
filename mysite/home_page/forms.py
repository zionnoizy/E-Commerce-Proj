from django import forms
from .models import Discussion_model#, Password_model
# from django.core import validators
from django.forms import PasswordInput

# Create your models here.
class Discussion_form(forms.ModelForm):
    conversation = forms.CharField(
        # validators=[validators.validate_slug],
        label='conversation',
        max_length=240)

    class Meta:
        model = Discussion_model
        fields = ['conversation']



# class Password_from(forms.ModelForm):
#     password = models.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = Password_model
