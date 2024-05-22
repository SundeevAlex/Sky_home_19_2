from django.urls import path, include
from catalog.apps import NewappConfig
from catalog.views import ProductListView, home, ProductDetailView, ContactsTemplateView

app_name = NewappConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_details'),
    # path('', home, name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts')
]
