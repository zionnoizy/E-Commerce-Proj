from django.shortcuts import render, redirect
from . import forms

# Create your views here.
def register(request):
    if request.method == 'POST':
        registration_form = forms.Registration_form(request.POST)
        if registration_form.is_valid():
            registration_form.save(commit=True)
            return redirect("/accounts/login/")
    else:
        registration_form = forms.Registration_form()
    context = {
    "form":registration_form,
    }
    return render(request, "registration/register.html", context=context)
