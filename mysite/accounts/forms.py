from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your forms here.
class Registration_form(UserCreationForm):
    email = forms.EmailField(label="Email",required=True)
    # is_admin = forms.BooleanField(default=False)

    class Meta:
        model = User
        fields = ("username", "email","password1","password2")

    def save(self, commit=True):
        user =super(Registration_form,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        # user.is_admin = self.cleaned_data['is_admin']
        if commit:
            user.save()
        return user
