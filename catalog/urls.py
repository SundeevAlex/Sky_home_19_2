from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import index, home, contacts

app_name = NewappConfig.name

urlpatterns = [
    path('', index),
    # path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
]
