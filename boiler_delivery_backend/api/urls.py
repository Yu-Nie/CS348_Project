from django.urls import path, re_path, include
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', mainPageView, name = 'main'),
    path('customer', customerView, name = 'customer'),

    path('cart/', getCartView),

    path('restaurants/', getAllRestaurants),
    path('restaurant/', restaurantView),
    re_path('restaurant/addFood$', addFoodSelectRestView),
    re_path('restaurant/addFood/[0-9]+$', addFoodView),
    path('restaurant/addRestaurant', addRestaurantView),

    re_path('menus/[0-9]+', getMenusView),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('usersignup/', customerSignupView),

]
