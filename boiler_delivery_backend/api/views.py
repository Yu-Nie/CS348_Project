from django.http import HttpResponse
from .utils import getCart, getMenus, getRestrants, signup, customerLogin

from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

import json

# Create your views here.

def test(request):
    cust_id = signup("a", "b", "c", "d")
    getCart(cust_id)
    return (HttpResponse("Sup, this is the defualt page"))


def customerLoginView(request, username=None, password=None):
    username = request.GET.get('username')
    password = request.GET.get('password')

    if not username or not password:
        login_success = False
    else:
        login_success = customerLogin(username, password)

    res = {
        "success": login_success,
    }
    return (HttpResponse(json.dumps(res, cls=DjangoJSONEncoder), content_type='application/json'))


def getMenusView(request):
    fullpath = request.get_full_path()
    fullpath = fullpath.split('/')

    rest_id = int(fullpath[2])

    menus = getMenus(rest_id)
    menus_serialized = serializers.serialize("json", menus)

    return (HttpResponse(menus_serialized, content_type='application/json'))
    #return(HttpResponse("just testing"))

def getAllRestaurants(request):
    all_rest = getRestrants()
    all_rest_ser = serializers.serialize("json", all_rest)
    return (HttpResponse(all_rest_ser, content_type='application/json'))
