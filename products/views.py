from django.shortcuts import render
from .models import *
# Create your views here.
def index(req):
    product=Product.objects.all()
    
    context={
        'product':product,
    }
    
    return render(req,'index.html',context)