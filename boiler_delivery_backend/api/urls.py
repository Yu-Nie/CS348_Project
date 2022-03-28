from django.urls import path, re_path
from .views import test, customerLoginView, getMenusView, getAllRestaurants

urlpatterns = [
    path('', test),
    path('login', customerLoginView),
    re_path(r'restaurant/[0-9]+/menu', getMenusView),
    path('restaurants/', getAllRestaurants),

]
