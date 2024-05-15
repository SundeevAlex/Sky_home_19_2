from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import products_list, home, contacts, products_details

app_name = NewappConfig.name

urlpatterns = [
    path('', products_list, name='products_list'),
    path('products/<int:pk>/', products_details, name='products_details'),
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
