from django.urls import path, include
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', mainPageView),
    path('customer', customerView, name = 'customer'),
    path('usersignup/', customerSignupView),
    path('food/', getMenusView),
    path('cart/', getCartView),
    #path('restaurant/', restaurantView),
    #path('restaurant/login', restaurantView),
    path('restaurant/addRestaurant', addRestaurantView),

    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),

]
