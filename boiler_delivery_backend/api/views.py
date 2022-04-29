from django.http import HttpResponse
from . import models
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from .utils import customerLogin, getMenus, getRestrants


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
        models.Customer.objects.create(email=email, password=password)

        return HttpResponse("log in successful!")

    return render(request, "userlogin.html")


def customerSignupView(request):

    """
    if request.method == "POST":
        first_name = request.POST.get("first")
        last_name = request.POST.get("last")
        email = request.POST.get("email")
        address = request.POST.get("address")
        password = request.POST.get("pwd")
        cart = models.Cart(totalPrice=0.0)
        cart.save()
        models.Customer.objects.create(email=email, firstName=first_name, lastName=last_name, address=address,
                                       password=password, cart_Id=cart)

        return HttpResponse("User Registered!")

    return render(request, "usersignup.html")
    """


    if request.method == "POST":
        new_post = request.POST.copy()
        new_post['email'] = new_post['username']
        #print(new_post)

        form = SignupForm(new_post)
        if form.is_valid():
            form.save()

            # adding to customer table / creating cart  ~ :D
            first_name = new_post.get("first_name")
            last_name = new_post.get("last_name")
            email = new_post.get("email")
            address = new_post.get("address")
            password = new_post.get("password1")
            cart = models.Cart(totalPrice=0.0)
            cart.save()

            models.Customer.objects.create(email=email, firstName=first_name, lastName=last_name, address=address,
                                        password=password, cart_Id=cart)


            return render(request, "usersignupsuccess.html")
        else:
            render(request, "usersignup.html", {"form":form})
    else:
        form = SignupForm()

    return render(request, "usersignup.html", {"form":form})



def restaurantView(request):
    return render(request, "restaurant.html")

def addRestaurantView(request):
    if request.method == "POST":
        address = request.POST.get("address")
        image_url = request.POST.get("image_url")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        models.Restaurant.objects.create(address=address, image_url=image_url, name=name, phone=phone)

        return HttpResponse("Restaurant Registered!")
    return render(request, "addRestaurant.html")


def getMenusView(request):
    fullpath = request.get_full_path()
    fullpath = fullpath.split('/')

    rest_id = int(fullpath[2])

    menus = getMenus(rest_id)
    menus_serialized = serializers.serialize("json", menus)

    return (HttpResponse(menus_serialized, content_type='application/json'))


def getAllRestaurants(request):
    all_rest = getRestrants()
    all_rest_ser = serializers.serialize("json", all_rest)
    # models.Cart.objects.getall()
    return render(request, "restaurant_list.html");
    # return (HttpResponse(all_rest_ser, content_type='application/json'))
