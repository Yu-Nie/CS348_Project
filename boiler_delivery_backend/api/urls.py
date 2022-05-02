from django.urls import path, re_path, include
from django.contrib import admin
from .views import *


urlpatterns = [
    path('', mainPageView, name = 'main'),
    path('customer', customerView, name = 'customer'),

    path('restaurants/', getAllRestaurants),
    path('restaurant/', restaurantView),
    re_path('restaurant/addFood$', addFoodSelectRestView),
    re_path('restaurant/addFood/[0-9]+$', addFoodView),
    path('restaurant/addRestaurant', addRestaurantView),
    re_path('^menus/[0-9]+', getMenusView),
    re_path('^addToCart/[0-9]+/[0-9]+', addCartView),
    path('cart/', getCartView),
    path('clearCart/', clearCartView),
    path('checkout/', checkoutView),
    path('purchased/', purchasedView),
    path('customer/searchRest', searchRestaurant),
    path('customer/searchPrice', searchFoodWithPriceView),
    path('customer/searchName', searchFoodWithName),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
    path('usersignup/', customerSignupView),
    path('success/', successRedirectView),

]
