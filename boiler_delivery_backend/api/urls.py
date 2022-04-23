from django.urls import path, re_path
from django.contrib import admin
from .views import *

urlpatterns = [
    # path('', test),
    path('login/', customerLoginView),
    path('signup/', customerSignupView),
    path('food/', getMenusView),
    path('restaurants/', getAllRestaurants),
    path('admin/', admin.site.urls)
]
