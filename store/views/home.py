from django.shortcuts import render, redirect
from store.models.products import Product
from store.models.category import Category

def store_home(request):
    if request.method == 'POST':
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            
        request.session['cart'] = cart
        return redirect('homepage')
        
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    
    # Initialize cart in session if not exists
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
        
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
        
    data = {}
    data['products'] = products
    data['categories'] = categories
    
    return render(request, 'store/home.html', data)
