from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_Id = models.BigAutoField(primary_key=True)
    totalPrice = models.FloatField()


class Customer(models.Model):
    user_Id = models.BigAutoField(primary_key=True)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=255, null=False, blank=False)
    lastName = models.CharField(max_length=255, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(default="N/A")
    cart_Id = models.ForeignKey(Cart, on_delete=models.CASCADE)


class Restaurant(models.Model):
    restaurant_Id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.TextField(default="N/A")
    image_url = models.TextField(default="N/A")
    phone = models.BigIntegerField(null=False)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='rest_name_idx'),
        ]


class Food(models.Model):
    food_Id = models.BigAutoField(primary_key=True)
    description = models.TextField(null=False, blank=True)
    image_url = models.TextField(default="N/A")
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.FloatField(null=False)
    restaurant_Id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='food_name_idx'),
            models.Index(fields=['price'], name='price_idx'),
        ]


class OrderItem(models.Model):
    item_Id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False, blank=False, default="N/A")
    description = models.TextField(null=False, blank=True)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)
    food_Id = models.ForeignKey(Food, on_delete=models.CASCADE, default=0)
    cart_Id = models.ForeignKey(Cart, on_delete=models.CASCADE, default=0)


# https://docs.djangoproject.com/en/1.8/topics/auth/passwords/#django.contrib.auth.hashers.make_password
# ^ function to encrypt password
