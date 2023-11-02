from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Category,Products,Profile,Cart,CartItem
from django.http import JsonResponse
import json
from django.db.models import Q

# Create your views here.
def home(request):
        if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            return render(request,"home.html",{"cart":cart})
        else:
             return render(request,"home.html")


def about(request):
    return render(request, "about.html")

def products(request):
    cat= Category.objects.all()
    pro=Products.objects.all()
    if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            return render(request,"menu.html",{'products':pro,'category':cat, 'cart':cart})
    else:
        return render(request, "menu.html",{'products':pro,'category':cat})

def register(request):
    if request.method=="POST":
        first_name=request.POST["firstname"]
        last_name=request.POST["lastname"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse('username taken')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('email taken')
            else:
               user = User.objects.create_user(username=username, email=email,first_name=first_name, last_name=last_name, password=password1)
               user.save()
               return redirect("/")
        else:
            messages.info(request, 'Password do not match')
            return redirect("/")
        
    
    

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect("/")

def search(request):
    item=request.GET['item']
    keyword = Q(name__icontains=item) | Q(category__name__icontains=item)
    pro = Products.objects.filter(keyword)
    return render(request, "products.html",{"products":pro})



def addtocart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created= CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
       
        cartitem.save()

        num_of_item = cart.num_of_items

        print(cartitem)
    return JsonResponse(num_of_item, safe=False)

def cart(request):
    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems= cart.cartitems.all()
        
        return render(request, "cart.html",{'cart':cart, 'items':cartitems})
    
def profile(request):
    if request.user.is_authenticated:
            cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
            return render(request,"profile.html",{'cart':cart})
    
def quantitymore(request,id):
    cartitem= CartItem.objects.get(id=id)
    cartitem.quantity += 1
       
    cartitem.save()
    return redirect("/cart")

def quantityless(request,id):
    cartitem= CartItem.objects.get(id=id)
    cartitem.quantity = cartitem.quantity - 1
       
    cartitem.save()
    return redirect("/cart")