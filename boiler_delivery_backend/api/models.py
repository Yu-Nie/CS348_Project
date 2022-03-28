from django.db import models

# Create your models here.
class Customer(models.Model):
    user_Id = models.AutoField()
    email = models.CharField(max_length=255,null=False, blank=False)
    firstName = models.CharField(max_length=255,null=False, blank=False)
    lastName = models.CharField(max_length=255,null=False, blank=False)
    password = models.CharField(max_length=255,null=False, blank=False)
    address = models.TextField()


class Cart(models.Model):
    cart_Id = models.AutoField()
    totalPrice = models.FloatField()
    user_Id = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Restaurant(models.Model):
    restaurant_Id = models.AutoField()
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField()
    phone = models.BigIntegerField(null=False)


class Food(models.Model):
    food_Id = models.AutoField()
    name = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    price = models.FloatField(null=False)
    restaurant_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class OrderItem(models.Model):
    item_Id = models.AutoField()
    name = models.CharField(max_length=255,null=False, blank=False)
    description = models.TextField(null=False, blank=True)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    food_Id = models.ForeignKey(Food, on_delete=models.CASCADE)
    cart_Id = models.ForeignKey(Cart, on_delete=models.CASCADE)


# https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#django.contrib.auth.hashers.make_password
# ^ function to encrypt password
