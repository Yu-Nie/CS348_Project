from django.http import HttpResponse
from .utils import getMenus,createMenuItem

# Create your views here.

def test(request):
    print(createMenuItem('a', 123))
    return (HttpResponse("sup"))