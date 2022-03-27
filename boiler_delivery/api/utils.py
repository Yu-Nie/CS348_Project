from .models import MenuItem, Restaurant, Customer, Cart, OrderItem



# Creates a customer with the given information, and returns its id.
# Also creates a cart 
#  
# TODO: encrypt the password
def signup(email, firstname, lastname, password, enable=False):
    cust = Customer.objects.get(email=email)
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


# Returns a list of menu Items of the given restaurant name 
def getMenus(restaurant_id):
    return MenuItem.objects.filter(id=restaurant_id)


# Creates a menu item for a restaurant. Default price is 0.
def createMenuItem(name, restaurant_name, price=0.0, description=''):

    rest, created = Restaurant.objects.get_or_create(name=restaurant_name, defaults={'phone': 0})
    #print(rest)
    new_mi = MenuItem.objects.create(name=name, price=price, description=description, restaurant=rest)
    return new_mi.id


# Returns all restaurants
def getRestrants():
    return Restaurant.objects.all()


# Returns the cart id of a given customer id
def getCart(customer_id):
    cust_obj = Customer.objects.get(id=customer_id)
    if not cust_obj:
        print("No such customer")
        return None
    
    cart = cust_obj.cartId
    #print(cart.id)
    return cart.id


def checkout():
    pass


# creates a new orderitem object and assigns a menu item it to a cart.
# will return -1 if cart or menu iten does not exist.
def addToCart(cartId, menuItemId, quantity=1, price=0.0):
    mi_object = MenuItem.get(id=menuItemId)
    cart_object = Cart.get(id=cartId)
    if not mi_object or not cart_object:
        return -1

    new_oi = OrderItem.objects.create(quantity=quantity, price=price, menuItem_id=mi_object, cart_id=cart_object)
    return new_oi.id
