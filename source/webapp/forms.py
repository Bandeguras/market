from django import forms
from webapp.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'stock', 'price', 'category']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='поиск')


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'phone', 'address']