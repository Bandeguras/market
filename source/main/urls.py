"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from webapp.views.product_views import IndexViews, ProductCreateView, ProductDeleteView, ProductView, ProductUpdateView
from webapp.views.cart_view import CartList, CartDelete, OrderCreate, OrderList, CartDeleteOne, AddItemToCart
from accounts.views import RegisterView


api_url = [
    path('v1/', include('api_v1.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(api_url)),

    path('', IndexViews.as_view(), name='index'),

    path('product/add/', ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/', ProductView.as_view(), name='view'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='delete'),
    path('product/<int:pk>/ad_to_cart/', AddItemToCart.as_view(), name='add_to_cart'),

    path('cart/', CartList.as_view(), name='cart_index'),
    path('cart/<str:pk>/delete/', CartDelete.as_view(), name='cart_delete'),
    path('cart/<str:pk>/delete/one', CartDeleteOne.as_view(), name='cart_delete_one'),
    path('order/', OrderCreate.as_view(), name='order_create'),
    path('orders/', OrderList.as_view(), name='order_list'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', RegisterView.as_view(), name='create'),
]
