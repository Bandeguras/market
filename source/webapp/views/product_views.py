from django.contrib.auth.mixins import  PermissionRequiredMixin

from webapp.models import Product
from webapp.forms import ProductForm, SimpleSearchForm
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from django.utils.http import urlencode
from django.urls import reverse_lazy


class IndexViews(ListView):
    template_name = 'product/index.html'
    context_object_name = 'products'
    model = Product
    ordering = ('category', 'title')
    paginate_by = 5
    search_form_class = SimpleSearchForm
    search_fields = ['category__icontains', 'title__icontains']

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(category__icontains=self.search_value) | Q(title__icontains=self.search_value))
        return queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context



class ProductView(DetailView):
    template_name = 'product/product_view.html'
    model = Product


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = "product/create.html"
    model = Product
    form_class = ProductForm
    permission_required = 'webapp.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "product/product_update.html"
    form_class = ProductForm
    model = Product
    context_object_name = 'product'
    permission_required = 'webapp.change_product'



class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = "product/product_delete.html"
    success_url = reverse_lazy('index')
    permission_required = 'webapp.delete_product'

