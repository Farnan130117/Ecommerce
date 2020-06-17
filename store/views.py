from django.shortcuts import render

# Create your views here.
# FBV for store function
def store(request):
	context={}
	return render(request,'store/store.html',context)

# FBV for cart function
def cart(request):
	context={}
	return render(request,'store/cart.html',context)

# FBV for context function
def checkout(request):
	context={}
	return render(request,'store/checkout.html',context)
