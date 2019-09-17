from django import forms

from .models import Checkout_model

class Checkout_form(forms.ModelForm):

    class Meta:
        model = Checkout_model
        fields = ('first_name', 'last_name')

    def save(self, commit=True):
        user =super(Checkout_model,self).save(commit=False)
        # user.email=self.cleaned_data["email"]
        # user.is_admin = self.cleaned_data['is_admin']
        if commit:
            user.save()
        return user
