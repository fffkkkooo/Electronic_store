from django.shortcuts import render


def shop_pages(request):
    return render(request, 'shop/shop_pages.html')
