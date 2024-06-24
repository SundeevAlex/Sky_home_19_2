from django.shortcuts import render, get_object_or_404

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products_list')


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')


class ProductListView(ListView):
    model = Product

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        products = self.get_queryset(*args, **kwargs)

        for product in products:
            versions = Version.objects.filter(product=product)
            active_versions = versions.filter(is_active_version=True)
            if active_versions:
                product.active_version = active_versions.last().version_title
            else:
                product.active_version = 'Нет активной версии'

        context_data['object_list'] = products
        return context_data


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
