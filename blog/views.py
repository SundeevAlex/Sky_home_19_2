from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'created_at')
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'created_at')

    def form_valid(self, form):
        if form.is_valid():
            new_rec = form.save()
            new_rec.slug = slugify(new_rec.title)
            new_rec.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


# def toggle_activity(request, pk):
#     blog_item = get_object_or_404(Blog, pk=pk)
#     if blog_item.published:
#         blog_item.published = False
#     else:
#         blog_item.published = True
#
#     blog_item.save()
#     return redirect(reverse('blog:list'))
