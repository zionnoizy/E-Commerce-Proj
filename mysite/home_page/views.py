from django.shortcuts import render

from products.models import Product_model
from products.models import Category_model


from . import models
from . import forms
# Create your views here.
def home(request):
    all_products = Product_model.objects.all()
    all_catrgories = Category_model.objects.all()
    context = {
    "all_products":all_products,
    "all_catrgories":all_catrgories,
    }
    return render(request, 'home_page/home_page.html', context=context)


def category(request, category):
    if request.method == 'GET':
        find_catrgory = models.Product_model.objects.get(category=category)
        context = {
        "find_catrgory":find_catrgory,
        }
    return redirect('/')


def discussion_board(request):
    if request.method == 'POST':
        my_form = forms.Discussion_form(request.POST)
        if my_form.is_valid():
            conversation = models.Discussion_model(
                conversation=my_form.cleaned_data["conversation"]
            )
            conversation.save()
            my_form=forms.Discussion_form()
    else:
        my_form=forms.Discussion_form()
    conversation = models.Discussion_model.objects.all()
    context = {
        "my_form":my_form,
        "conversation":conversation,
    }
    return render(request, 'home_page/discussion_board.html', context=context)


def rest_chat(request):
    if request.method == 'GET':
        conversation = models.Discussion_model.objects.all()
        list_of_conversation = []
        for x in conversation:
            list_of_conversation+=[{
                "conversation":x.conversation,
                "id":x.id
            }]
        return JsonResponse({"conversation":list_of_conversation},safe=False)
    else:
        return HttpResponse("Invalid HTTP Method")


def employee(request, price=0, quantity=0, total=0, counter=0, all_products=None):
    all_products = Product_model.objects.all()
    for all_item in all_products:
        price += all_item.price
        quantity += all_item.stock
        total += (all_item.price * all_item.stock)
        counter += all_item.stock
    context = {
    "all_products": all_products,
    "total": total,
    "counter": counter,
    "price": price,
    "quantity": quantity
    }
    return render(request, 'home_page/employee.html', context=context)
