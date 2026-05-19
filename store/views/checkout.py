from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from store.models.products import Product
from store.models.orders import Order
from store.models.customer import Customer
from django.contrib import messages

@login_required(login_url='/login/')
def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        
        if not cart:
            messages.error(request, "Your cart is empty.")
            return redirect('cart')
            
        try:
            customer = Customer.objects.get(user=request.user)
        except Customer.DoesNotExist:
            # If they are logged in (e.g. as admin) but don't have a customer profile, create one on the fly
            customer = Customer.objects.create(
                user=request.user,
                first_name=request.user.first_name or request.user.username,
                last_name=request.user.last_name or '',
                email=request.user.email or '',
                phone=phone
            )
            
        products = Product.get_all_products().filter(id__in=list(cart.keys()))
        
        for product in products:
            quantity = cart.get(str(product.id))
            order = Order(
                customer=customer,
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=quantity
            )
            order.save()
            
        request.session['cart'] = {}
        messages.success(request, "Your order has been placed successfully!")
        return redirect('orders')
        
    return redirect('cart')
