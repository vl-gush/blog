from django.db.models import Count, Sum, Max
from django.http import HttpResponse

from shop.models import Product, Purchase


def products(request):
    get_params = request.GET.items()
    product_list = Product.objects.all()
    purchase_list = Purchase.objects.all()
    for key, value in get_params:
        if key == "cost":
            product_list = product_list.filter(cost__lt=value)
    return HttpResponse(", ".join([x.title for x in product_list]))
