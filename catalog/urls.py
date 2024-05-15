from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import products_list, home, contacts

app_name = NewappConfig.name

urlpatterns = [
    path('', products_list),
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
