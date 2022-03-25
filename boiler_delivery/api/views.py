from django.http import HttpResponse
from .utils import getCart, getMenus, createMenuItem, signup

# Create your views here.

def test(request):
    cust_id = signup("a", "b", "c", "d")
    getCart(cust_id)
    return (HttpResponse("sup"))