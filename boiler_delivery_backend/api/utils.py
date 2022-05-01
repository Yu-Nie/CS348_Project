from tkinter.messagebox import NO
from scipy.fftpack import cs_diff
from sympy import re
from .models import *



# Creates a customer with the given information, and returns its id.
# Also creates a cart 
#  
# TODO: encrypt the password
def signup(email, firstname, lastname, password, enable=False):
    cust = Customer.objects.filter(email=email)
    if cust:
        return cust.id

    cart = Cart.objects.create(totalPrice=0)
    cust = Customer.objects.create(email=email, firstName=firstname, lastName=lastname, password=password, cartId=cart)
    
    return cust.id

#  username is the same as email
# TODO: encrypt the password
def customerLogin(username, password):
    cust = Customer.objects.filter(email=username)
    if not cust:
        return False

    if cust.password == password:
        return True

    return False


# Returns a customer object with a given customer username / email
def getCustomer(username):
    cust = Customer.objects.filter(email=username)
    if not cust:
        return None

    return cust[0]


# Returns a list of menu Items of the given restaurant object
def getMenus(restaurant_id):
    menu = Food.objects.filter(restaurant_Id=restaurant_id)
    print("menu:", menu)
    return menu


# Creates a menu item for a restaurant. Default price is 0.
def createFood(name, restaurant_name, price=0.0, description=''):

    rest, created = Restaurant.objects.get_or_create(name=restaurant_name, defaults={'phone': 0})
    #print(rest)
    new_mi = Food.objects.create(name=name, price=price, description=description, restaurant=rest)
    return new_mi.id

# Returns Food with given id
def getFood(food_Id):
    food_obj = Food.objects.filter(food_Id=food_Id)
    if food_obj:
        return food_obj[0]
    return None

# Returns all restaurants
def getRestrants():
    return Restaurant.objects.all()

# Returns all restaurants owned by a given Customer object
def getRestrantsOwner(cust):
    rest_obj = Restaurant.objects.filter(owner=cust)
    return rest_obj

# Returns restaurant with given id
def getRestrant(rest_id):
    rest_obj = Restaurant.objects.filter(restaurant_Id=rest_id)
    if rest_obj:
        return rest_obj[0]
    return None


# Returns the content of the cart a given customer username (email)
def getCart(username):
    cust_obj = Customer.objects.filter(email=username)
    if not cust_obj:
        return None
    
    #print(cust_obj[0])
    cart = cust_obj[0].cart_Id
    return cart


# Returns a list of ordered items of a given cart object
def getOrderItem(cart):
    order_objects = OrderItem.objects.filter(cart_Id=cart)
    if not order_objects:
        return None
    return order_objects



def checkout():
    pass


# creates a new orderitem object and assigns a menu item it to a cart.
# will return -1 if cart or menu iten does not exist.
def addToCart(cartId, foodId, quantity=1, price=0.0):
    food_object = Food.get(id=foodId)
    cart_object = Cart.get(id=cartId)
    if not food_object or not cart_object:
        return -1

    new_oi = OrderItem.objects.create(quantity=quantity, price=price, food_id=food_object, cart_id=cart_object)
    return new_oi.id
