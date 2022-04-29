from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
from .utils import *
from .models import *
from .forms import *


def test(request):
    # cust_id = signup("a", "b", "c", "d")
    # getCart(cust_id)
    return (HttpResponse("Sup, this is the defualt page"))


def mainPageView(request):
    # print("Welcome to Boiler Delivery!")
    return render(request, "mainPage.html")


def customerView(request):
    return render(request, "customer.html")


def customerLoginView(request, username=None, password=None):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        Customer.objects.create(email=email, password=password)

        return HttpResponse("log in successful!")

    return render(request, "userlogin.html")


def customerSignupView(request):
    if request.method == "POST":
        new_post = request.POST.copy()
        new_post['email'] = new_post['username']
        #print(new_post)

        form = SignupForm(new_post)
        if form.is_valid():

            # adding to customer table / creating cart  ~ :D
            first_name = new_post.get("first_name")
            last_name = new_post.get("last_name")
            email = new_post.get("email")
            address = new_post.get("address")
            password = new_post.get("password1")
            cart = Cart(totalPrice=0.0)
            cart.save()

            Customer.objects.create(email=email, firstName=first_name, lastName=last_name, address=address,
                                        password=password, cart_Id=cart)

            form.save()

            return render(request, "usersignupsuccess.html")
        else:
            render(request, "usersignup.html", {"form":form})
    else:
        form = SignupForm()

    return render(request, "usersignup.html", {"form":form})



def restaurantView(request):
    return render(request, "restaurant.html", {"authenticated": request.user.is_authenticated })


def addRestaurantView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            address = request.POST.get("address")
            image_url = request.POST.get("image_url")
            name = request.POST.get("name")
            phone = request.POST.get("phone")

            cust_obj = getCustomer(request.user.username)
            Restaurant.objects.create(address=address, image_url=image_url, name=name, phone=phone, owner=cust_obj)

            return HttpResponse("Restaurant Registered!")
            
        else:
            form = AddRestaurantForm()
            return render(request, "addRestaurant.html", {"form":form})
        
    else:
        return render(request, "requestlogin.html")


def addFoodSelectRestView(request):
    if request.user.is_authenticated:
        cust = getCustomer(request.user.username)
        rests = getRestrantsOwner(cust)

        print(rests)
        return render(request, "listownerrest.html", {"objects":rests})
        
    else:
        return render(request, "requestlogin.html")


def addFoodView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            description = request.POST.get("description")
            image_url = request.POST.get("image_url")
            name = request.POST.get("name")
            price = request.POST.get("price")
            
            fullpath = fullpath.split('/')
            rest_id = int(fullpath[3])
            rest_object = getRestrant(rest_id)

            Food.objects.create(description=description, image_url=image_url, name=name, price=price, restaurant_Id=rest_object)

            return HttpResponse("Restaurant Registered!")
            
        else:
            form = AddFoodForm()
            return render(request, "addFood.html", {"form":form})
        
    else:
        return render(request, "requestlogin.html")





def getMenusView(request):
    fullpath = request.get_full_path()
    fullpath = fullpath.split('/')

    rest_id = int(fullpath[2])

    rest_object = getRestrant(rest_id)
    if not rest_object:
        return (HttpResponse("no such restaurant"))
    menu = getMenus(rest_object)
    if not menu:
        return (HttpResponse("This restaurant has no food."))
    return render(request, "showmenu.html", {"menu_objects":menu})



def getAllRestaurants(request):
    return render(request, "restaurant_list.html", {"restaurants": getRestrants});
    # return (HttpResponse(all_rest_ser, content_type='application/json'))


def getCartView(request):
    if request.user.is_authenticated:
        #print(getCart(request.user.username))
        return (HttpResponse("logged in"))
    else:
        print("not logged in!")
        return (HttpResponse("sup"))

