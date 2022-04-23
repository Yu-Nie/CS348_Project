from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cart, Customer, Restaurant, Food, OrderItem


# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_Id', 'totalPrice']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user_Id', 'email', 'firstName', 'lastName', 'password', 'address', 'cart_Id']


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['restaurant_Id', 'address', 'image_url', 'name', 'phone']


class FoodAdmin(admin.ModelAdmin):
    list_display = ['food_Id', 'description', 'image_url', 'name', 'price', 'restaurant_Id']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['item_Id', 'name', 'description', 'price', 'quantity', 'food_Id', 'cart_Id']


admin.site.register(Cart, CartAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(OrderItem, OrderItemAdmin)