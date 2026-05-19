from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from store.models.customer import Customer

def login_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # We assume email is the username
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            username = None
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Invalid email or password.')
            
    return render(request, 'store/login.html')

def logout_user(request):
    logout(request)
    return redirect('homepage')

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('homepage')
        
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Validation
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('signup')
            
        # Create standard User
        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        user.save()
        
        # Create Customer profile
        customer = Customer(user=user, first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        customer.save()
        
        login(request, user)
        return redirect('homepage')
        
    return render(request, 'store/signup.html')
