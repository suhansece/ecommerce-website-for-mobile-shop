from django.shortcuts import render
from .models import *

def home(request):
    data=Product.objects.all().order_by('-id')
    return render(request,'index.html',{'data':data})

def cart(request):
  
  if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
  else:
    items=[]
    
  context= {'items': items,'order':order}
  return render(request,'cart.html',context)
 


