from django.shortcuts import render
from django.views.generic.base import TemplateView


from checkout.models import Checkout_model
from . import models
from . import forms
# Create your views here.
def check_out(request):
    if request.method == 'POST':
        my_form = forms.Checkout_form(request.POST)
        if my_form.is_valid():
            conversation = models.Discussion_model(
                conversation=my_form.cleaned_data["conversation"]
            )
            conversation.save()
            my_form=forms.Checkout_form()
    else:
        my_form=forms.Checkout_form()
    conversation = models.Checkout_model.objects.all()
    context = {
        "my_form":my_form,
        "conversation":conversation,
    }
    return render(request, 'checkout/checkout.html', context=context)


    personal_info_form = forms.Checkout_form()
    if request.method == 'POST':
        personal_info = models.Checkout_model.objects.all()
        form_instance = forms.Checkout_form(request.POST)
        if form_instance.is_valid():
            if request.user.is_authenticated:
                my_checkout = models.Checkout_model(
                first_name=form_instance.cleaned_data["first_name"],
            )
        my_checkout.save()
        form_instance = forms.Checkout_form()
    my_checkout = models.Checkout_model.objects.all()
    context = {
        # "personal_info":personal_info,
        # "username":username,
        "my_checkout":my_checkout,
        "form_instance":form_instance
    }
    return render(request, 'checkout/checkout.html', context=context)


def success(request):
    if request.method == 'POST':
        return render(request, 'checkout/success.html')
