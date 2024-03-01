from django.views.generic import ListView
from .models import Product, ArtistProfile
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView
from django.urls import reverse_lazy
from .models import Product, Order, Review
from .forms import OrderForm, ReviewForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

class ProductDetailView(DetailView):
    model = Product
    template_name = 'marketplace/product_detail.html'
    context_object_name = 'product'

class OrderProductView(FormView):
    template_name = 'marketplace/order_product.html'
    form_class = OrderForm

    def form_valid(self, form):
        product_id = self.kwargs['pk']
        product = Product.objects.get(pk=product_id)
        quantity = form.cleaned_data['quantity']
        total_price = product.price * quantity
        customer = self.request.user.customerprofile
        Order.objects.create(customer=customer, product=product, quantity=quantity, total_price=total_price)
        return redirect('product-detail', pk=product_id)

class ReviewCreateView(FormView):
    template_name = 'marketplace/review_create.html'
    form_class = ReviewForm

    def form_valid(self, form):
        artist_id = self.kwargs['artist_id']
        artist = ArtistProfile.objects.get(pk=artist_id)
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        customer = self.request.user.customerprofile
        Review.objects.create(artist=artist, customer=customer, rating=rating, comment=comment)
        return redirect('artist-detail', pk=artist_id)

