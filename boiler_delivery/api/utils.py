from .models import MenuItem, Restaurant

def getMenus(restaurant_name):
    return MenuItem.objects.filter(restaurant__name=restaurant_name)

def createMenuItem(name, restaurant_name, price=0.0, description=''):

    rest, created = Restaurant.objects.get_or_create(name=restaurant_name, defaults={'phone': 0})
    print(rest)
    MenuItem.objects.create(name=name, price=price, description=description, restaurant=rest)


def getRestrants():
    pass

def getCart():
    pass

def checkout():
    pass

def addToCart():
    pass


getMenus('a')