from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.


CATEGORY = [('other', 'other'), ('pharmacy', 'pharmacy'), ('food', 'food')]


class Product(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="title")
    stock = models.PositiveIntegerField(verbose_name="stock")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="price")
    category = models.CharField(max_length=20, null=False, blank=False, choices=CATEGORY, default=CATEGORY[0][0],
                                verbose_name="category")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="description")



    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.pk}. {self.title}'


class OrderProduct(models.Model):
    product = models.ForeignKey('webapp.Product', on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey('webapp.Order', related_name='order_product', on_delete=models.CASCADE, verbose_name='Заказ')
    qty = models.PositiveIntegerField(verbose_name='Количество')

    def total_amount(self):
        return self.product.price * self.qty


class Order(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя пользователя')
    phone = models.CharField(max_length=100, null=False, blank=False, verbose_name='Телефон')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Адрес')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    products = models.ManyToManyField('webapp.Product', related_name='order', through='webapp.OrderProduct',
                                      through_fields=['order', 'product'], verbose_name='Товары')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')