from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection

# Create your views here.
from .utils import *
from .models import *
from .forms import *


def searchFoodWithPriceView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            lower = request.POST.get("lower")
            upper = request.POST.get("upper")
            cursor = connection.cursor()
            cursor.execute("call sp_findFoodInRange(%s, %s)", [lower, upper])
            results = cursor.fetchall()
            cursor.close()
            print(results)
            return render(request, "showFoodPrice.html", {"results": results})
        else:
            form = searchPriceForm()
            return render(request, "searchPrice.html", {"form":form})

def searchFoodWithName(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            cursor = connection.cursor()
            cursor.execute("call sp_findFoodWithName(%s)", [name])
            results = cursor.fetchall()
            cursor.close()
            return render(request, "showFoodPrice.html", {"results": results})
        else:
            form = searchNameForm()
            return render(request, "searchName.html", {"form":form})

def searchRestaurant(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            name = request.POST.get("name")
            cursor = connection.cursor()
            cursor.execute("call findRestWithName(%s)", [name])
            results = cursor.fetchall()
            cursor.close()
            return render(request, "showRest.html", {"results": results})
        else:
            form = searchRestForm()
            return render(request, "searchRest.html", {"form":form})

def test(request):
    # cust_id = signup("a", "b", "c", "d")
    # getCart(cust_id)
    return (HttpResponse("Sup, this is the defualt page"))


def mainPageView(request):
    # print("Welcome to Boiler Delivery!")
    return render(request, "mainPage.html")


def customerView(request):
    return render(request, "customer.html", {"authenticated": request.user.is_authenticated })


def customerLoginView(request, username=None, password=None):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        Customer.objects.create(email=email, password=password)

        return HttpResponse("log in successful!")

    return render(request, "userlogin.html")


def successRedirectView(request):
    return render(request, "redirectMain.html", {"message": "Success!"})


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

            return render(request, "usersignup_success.html")
        else:
            render(request, "usersignup.html", {"form":form})
    else:
        form = SignupForm()

    return render(request, "usersignup.html", {"form":form})



def restaurantView(request):
    return render(request, "restaurant.html", {"authenticated": request.user.is_authenticated })


def addRestaurantView(request):
    print(request.user.is_authenticated)
    print(request.user.username)
    if request.user.is_authenticated:
        if request.method == "POST":
            address = request.POST.get("address")
            image_url = request.POST.get("image_url")
            name = request.POST.get("name")
            phone = request.POST.get("phone")

            cust_obj = getCustomer(request.user.username)
            Restaurant.objects.create(address=address, image_url=image_url, name=name, phone=phone, owner=cust_obj)

            return HttpResponse("Restaurant Registered!   <button onclick=\"location.href = \'/restaurant\'\" style=\"width:auto;\">Back</button>")
            
        else:
            form = AddRestaurantForm()
            return render(request, "restaurant_add.html", {"form":form})
        
    else:
        return render(request, "login_request.html")


def addFoodSelectRestView(request):
    if request.user.is_authenticated:
        cust = getCustomer(request.user.username)
        rests = getRestrantsOwner(cust)

        #print(rests)
        return render(request, "restaurant_owner_list.html", {"objects":rests})
        
    else:
        return render(request, "login_request.html")


def addFoodView(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            description = request.POST.get("description")
            image_url = request.POST.get("image_url")
            name = request.POST.get("name")
            price = request.POST.get("price")
            
            fullpath = request.get_full_path()
            fullpath = fullpath.split('/')
            rest_id = int(fullpath[3])
            rest_object = getRestrant(rest_id)

            if rest_object.owner != getCustomer(request.user.username):
                return render(request, "redirectMain.html", {"message": "This is not your restaurant."})

            Food.objects.create(description=description, image_url=image_url, name=name, price=price, restaurant_Id=rest_object)

            return HttpResponse("Food Added!  <button onclick=\"location.href = \'/restaurant/addFood\'\" style=\"width:auto;\">Back</button>")
            
        else:
            form = AddFoodForm()
            return render(request, "food_add.html", {"form":form})
        
    else:
        return render(request, "login_request.html")


def getMenusView(request):
    fullpath = request.get_full_path()
    fullpath = fullpath.split('/')

    rest_id = int(fullpath[2])

    rest_object = getRestrant(rest_id)
    if not rest_object:
        return (HttpResponse("no such restaurant.  <button onclick=\"location.href = \'/restaurants\'\" style=\"width:auto;\">Back</button>"))
    menu = getMenus(rest_object)
    if not menu:
        return (HttpResponse("This restaurant has no food. <button onclick=\"location.href = \'/restaurants\'\" style=\"width:auto;\">Back</button>"))
    return render(request, "menu_list.html", {"rest": rest_object, "menu_objects":menu})



def getAllRestaurants(request):
    return render(request, "restaurant_list.html", {"restaurants": getRestrants});
    # return (HttpResponse(all_rest_ser, content_type='application/json'))


def addCartView(request):
    fullpath = request.get_full_path()
    fullpath = fullpath.split('/')

    food_id = int(fullpath[3])
    food_obj = getFood(food_id)

    cart_obj = getCart(getCustomer(request.user.username).email)

    ordered = OrderItem.objects.filter(food_Id=food_obj, cart_Id=cart_obj)
    #print(ordered)
    if ordered:
        ordered[0].quantity += 1
        ordered[0].save()
    else:
        OrderItem.objects.create(name=food_obj.name, description=food_obj.description, 
                                price=food_obj.price, quantity=1, food_Id=food_obj, cart_Id=cart_obj)
    
    rest_id = int(fullpath[2])

    return render(request, "cart_add_success.html", {"rest_id": rest_id})


def clearCartView(request):
    if request.user.is_authenticated:
        cart_obj = getCart(request.user.username)
        oi = getOrderItem(cart_obj)
        if oi:
            oi.delete()

        return redirect("/cart/")

    else:
        return render(request, "login_request.html")


def getCartView(request):
    if request.user.is_authenticated:
        cart = getCart(getCustomer(request.user.username).email)
        ordered = getOrderItem(cart)
        return render(request, "cart_list.html", {"ordered": ordered});
    else:
        return render(request, "login_request.html")


def checkoutView(request):
    if request.user.is_authenticated:
        cart = getCart(getCustomer(request.user.username).email)
        ordered = getOrderItem(cart)

        if not ordered:
            redirect("/cart")

        price_sum = sum(oi.price * oi.quantity for oi in ordered)
        return render(request, "cart_checkout.html", {"ordered": ordered, "price_sum": price_sum});
    else:
        return render(request, "login_request.html")


def purchasedView(request):
    if request.user.is_authenticated:
        cart = getCart(getCustomer(request.user.username).email)
        ordered = getOrderItem(cart)
        if ordered:
            ordered.delete()

        return render(request, "redirectMain.html", {"message": "Thank you for shopping with Boiler Delivery! Your order will be on the way."})
    else:
        return render(request, "login_request.html")