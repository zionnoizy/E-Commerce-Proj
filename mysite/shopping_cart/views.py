from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal


from accounts.forms import Registration_form
from products.models import Product_model
from . import models
# Create your views here.


def pending_order(request):
    order = models.Shopping_cart_model.objects.filter(username=request.user)
    if order.exists():
        return order[0]
    return 0

@login_required()
def cart_detail(request, order_total=0):
    one_order = models.Shopping_cart_model.objects.all()
    my_items = models.Shopping_cart_item_model.objects.all()
    existing_order = pending_order(request)
    order_total = Decimal(0.00)
    # for item in my_items:
    #     order_total += (item.product.price * item.quantity)
    context = {
    "existing_order": existing_order,
    "one_order": one_order,
    "my_items": my_items,
    # "order_total": order_total,
    }
    return render(request, 'shopping_cart/shopping_cart.html', context=context)




@login_required()
def cart_add(request, product_id):
    if request.method == 'POST':
        my_product = Product_model.objects.get(id=product_id)
        cart_item, status = models.Shopping_cart_item_model.objects.get_or_create(product=my_product)
        cart_item.quantity += 1
        cart_item.save()
        # messages.success(request, "item added to cart", extra_tags='cart_add')
    cart_item = models.Shopping_cart_item_model.objects.all()
    context = {
        "cart_item":cart_item,
        "product_id":product_id,
        "my_product":my_product,
    }
    return redirect('/shopping_cart/')


def cart_remove(request, product_id):
    if request.method == 'POST':
        item_to_delete = models.Product_model.objects.get(pk=product_id)
        quantity = item_to_delete.stock
        item_to_delete.delete()
    # messages.add_message(request, messages.SUCCESS ,"item deleted to cart")
    # update_cart(request)
    return redirect('/')

# def update_cart(request):
#     request.session['cart_count'] = get_cart_count(request)
