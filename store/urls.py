from django.urls import path
from .views import store_home, login_user, logout_user, signup_user, cart, checkout, orders

urlpatterns = [
    path('', store_home, name='homepage'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('signup/', signup_user, name='signup'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),
]
