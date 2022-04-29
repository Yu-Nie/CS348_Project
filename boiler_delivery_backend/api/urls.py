from django.urls import path, re_path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', mainPageView),
    path('customer', customerView),
    path('customer/login/', customerLoginView),
    path('customer/signup/', customerSignupView),
    path('food/', getMenusView),
    path('restaurant/', restaurantView),
    path('restaurant/login', restaurantView),
    path('restaurant/addRestaurant', addRestaurantView),
    path('admin/', admin.site.urls),

]
