from django.http import HttpResponse

from shop.models import Product


def products(request):
    product_list = Product.objects.all()
    return HttpResponse(", ".join([x.title for x in product_list]))
