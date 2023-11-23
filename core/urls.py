from django.urls import path
from .views import home, products, register,nosotros


urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('register/', register, name='register'),
    path('nosotros/', nosotros, name="nosotros"),
]