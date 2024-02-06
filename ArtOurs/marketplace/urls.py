from django.urls import path
from .views import ProductListView, ProductDetailView, OrderProductView, ReviewCreateView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:pk>/order/', OrderProductView.as_view(), name='order-product'),
    path('artists/<int:artist_id>/review/', ReviewCreateView.as_view(), name='create-review'),

]
