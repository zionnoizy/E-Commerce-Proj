from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse


from products.models import Product_model
from . import models
# Create your views here.
def products_detail(request,product_id):
    all_products = models.Product_model.objects.all()
    single_item = get_object_or_404(Product_model,pk=product_id,available=True)
    context = {
    "all_products":all_products,
    "single_item":single_item,
    "product_id":product_id,
    }
    return render(request, 'products/product_descriptions.html', context=context)


def rest_all_products(request):
    if request.method == 'GET':
        all_products = models.Product_model.objects.all()
        json_list = []
        for x in all_products:
            json_list+=[{
                # json_dict = {}'
                "name":x.name,
                "price":x.price,
                "category":x.category.what_category,
    			"stock":x.stock,
                "description":x.description,
    			# item['amount"=round((int(cart.Quantity)*cart.Price),2)
    			# item['index"=index
                # json_list.append(json_dict)
            }]
        return JsonResponse({"all_products":json_list},safe=False)
    else:
        return HttpResponse("Invalid HTTP Method")
