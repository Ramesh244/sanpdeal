from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import *

from .forms import Detailsaboutpage,Contact_us,Singup

from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm


from django.contrib import messages

#from django.contrib.auth import authenticate


from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def deletedata(request, id):
    if request.method == 'POST':
        pi = DetailsForm.objects.get(pk=id)
        pi.delete()
    return render(request,'details.html')

def updatedata(request,id):
    if request.method == 'POST':
        pi = DetailsForm.objects.get(pk=id)
        fm = Detailsaboutpage(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            fm=Detailsaboutpage()
    else:
        pi = DetailsForm.objects.get(pk=id)
        fm = Detailsaboutpage(instance=pi)

    return render(request,"update.html",{'form':fm})


def Home(request):
    return render(request,"home.html")

def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,"store.html",context)


def Checkout(request):
    return render(request,"checkout.html")

def cart(request):
    return render(request,"cart.html")

def about(request):
    return render(request,"about.html")


def detialsform(request):
    if request.method == 'POST':
        fm = Detailsaboutpage(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name_of_product']
            pp = fm.cleaned_data['price_of_product']
            mp = fm.cleaned_data['manufature_of_product']
            rt = fm.cleaned_data['rating']
            re = fm.cleaned_data['reviews']
            reg = DetailsForm(name_of_product=nm, price_of_product=pp, manufature_of_product=mp,rating=rt,reviews=re)
            reg.save()
            messages.info(request, 'Now You can add product deatils !!!')
            print(messages.get_level(request))
            messages.debug(request, 'This is Debug')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is New Debug')
            print(messages.get_level(request))
            fm = Detailsaboutpage()
    else:
        fm = Detailsaboutpage()
    ram = DetailsForm.objects.all()
            
    return render(request,"details.html",{'form':fm,'ram':ram})




# Create your views here.

def contact(request):
    if request.method =='POST':
        rm=Contact_us(request.POST)
        if rm.is_valid():
            rm.save()

    else:
        rm=Contact_us()

    rm=Contact_us()

    return render(request,'contact.html',{'form':rm})


# def signingup(request):
#     if request.method == "POST":
#         pm = UserCreationForm(request.POST)
#         if pm.is_valid():
#              pm.save()
#     else:
#         pm = UserCreationForm()
#     return render(request, 'singup.html', {'form':pm})



# Create your views here.





# Create your views here.
def signingup(request):
    if request.method == "POST":
        fm = Singup(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!') 
            fm.save()
    else:
        fm = Singup()
    return render(request, 'singup.html', {'form':fm})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return render(request,'store.html')
        else:
            fm = AuthenticationForm()
            return render(request, 'login.html', {'form':fm})
    else:
        return render(request,'store.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('snaplogin')