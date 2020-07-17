from django.urls import path
from . import views

urlpatterns = [

    #Leave as empty string for base url
	path('', views.store, name= "store"), #showing store info
	path('cart/', views.cart, name= "cart"), #showing cart related info
	path('checkout/', views.checkout, name= "checkout"), #showing checkout info

]