from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('authentication/', include('authentication.urls')),
    path('cart/', include('cart.urls')),
    path('shop/', include('shop.urls')),
]
