from django.urls import path, include
from api_v1.views import ProductViewSet, OrderViewSet, OrderProductViewSet
from rest_framework.routers import DefaultRouter

app_name = 'api_v1'

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('order', OrderViewSet)
router.register('product_order', OrderProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]