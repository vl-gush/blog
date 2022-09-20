from django.shortcuts import render
from django.core.paginator import Paginator

from shop.models import Product
from shop.services import get_sorted_product


def products(request):
    if request.GET.get("color"):
        product_list = Product.objects.filter(color=request.GET.get("color"))
    else:
        product_list = Product.objects.all()

    order_by = request.GET.get("order_by")
    product_list = get_sorted_product(product_list, order_by)

    page_number = request.GET.get("page")
    paginator = Paginator(product_list, 15)
    paginator = paginator.get_page(page_number)

    return render(request, "index.html", {"paginator": paginator})
