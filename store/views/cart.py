from django.shortcuts import render
from store.models.products import Product

def cart(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
        
    ids = list(request.session.get('cart').keys())
    products = Product.get_all_products().filter(id__in=ids)
    
    return render(request, 'store/cart.html', {'products': products})
