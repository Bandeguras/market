from rest_framework import serializers
from webapp.models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'stock', 'price', 'category', 'description']
        read_only_fields = ['id']


class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title']


class OrderSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['products'] = ProductOrderSerializer(instance.products.all(), many=True).data
        return data

    class Meta:
        model = Order
        fields = ['name', 'phone', 'address', 'created_at', 'products', 'user']
        read_only_fields = ['id', 'created_at', 'user']


