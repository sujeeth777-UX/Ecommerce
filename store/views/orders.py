from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from store.models.orders import Order
from store.models.customer import Customer

@login_required(login_url='/login/')
def orders(request):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('homepage')
        
    orders = Order.get_orders_by_customer(customer.id)
    return render(request, 'store/orders.html', {'orders': orders})
