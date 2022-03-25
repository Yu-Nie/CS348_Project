from django.db import models

# Create your models here.
class Authorities(models.Model):
    email = models.CharField(max_length=255, null=False, blank=False)
    authorities = models.BooleanField(default=False)

class Cart(models.Model):
    totalPrice = models.FloatField()

class Restaurant(models.Model):
    address = models.TextField()
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.BigIntegerField(null=False)
    image_url = models.TextField()


# https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#django.contrib.auth.hashers.make_password
# ^ function to encrypt password

class Customer(models.Model):
    email = models.CharField(max_length=255,null=False, blank=False)
    firstName = models.CharField(max_length=255,null=False, blank=False)
    lastName = models.CharField(max_length=255,null=False, blank=False)
    password = models.CharField(max_length=255,null=False, blank=False)
    enable = models.BooleanField(default=False)
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)


class MenuItem(models.Model):
    name = models.CharField(max_length=255,null=False, blank=False)
    price = models.FloatField(null=False)
    description = models.TextField(null=False, blank=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class OrderItem(models.Model):
    quantity = models.IntegerField(null=False)
    price = models.FloatField(null=False)
    menuItem_id = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
