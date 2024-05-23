from django.shortcuts import render, get_object_or_404
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя: {name}\nТел: {phone}\nСообщение: {message}')
        return super().get(request, *args, **kwargs)

# def products_list(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'products_list.html', context)


# def products_details(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'products_details.html', context)


def home(request):
    return render(request, 'home.html')


# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя: {name}\nТел: {phone}\nСообщение: {message}')
#     return render(request, 'contacts.html')
