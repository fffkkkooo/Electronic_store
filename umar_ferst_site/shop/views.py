from django.shortcuts import render
from .models import Products


def shop_pages(request):
    product = Products.objects.all()
    context = {
        'product': product
    }
    return render(request, 'shop/shop_pages.html', context)
