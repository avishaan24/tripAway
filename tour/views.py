from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .paytm import Checksum
MERCHANT_KEY = "merchantkey";
from datetime import datetime
import datetime

# Create your views here.
from .forms import CreateUser

def index(request):
    package=Packages.objects.all()
    data={'package':package}
    return render(request, 'tour/home.html',data);

def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,('Invalid Credentials..'))
            return redirect('login')
    return render(request,'tour/login_page.html');

def logout_page(request):
    logout(request)
    messages.success(request,("You were successfully logged out!"))
    return redirect('login')


def about(request):
    return render(request,'tour/about.html');

def register(request):
    form=CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            user = User.objects.get(username=username)
            customer = Customer_detail(username=user,email=email,firstname=first_name,lastname=last_name)
            customer.save()
            messages.success(request,("Registration Successful"))
            return redirect('login')
        else:
            messages.error(request,("Unable to register!"))
            return render(request,'tour/register.html',{'form': form});
    else:
        form = CreateUser()
        return render(request, 'tour/register.html', {'form': form})

def profile(request):
    if request.user.is_authenticated:
        details=Customer_detail.objects.get(username=request.user)
        print(details.avatar)
        data={'details':details}
        return render(request,'tour/my_profile.html',data)
    else:
        messages.error(request,("Logged in first!"))
        return redirect('login')

def packageview(request,pid):
    package=Packages.objects.filter(id=pid)
    # print(package[0].sub_title)
    return render(request,'tour/packageview.html',{'package':package[0]})


def passenger(request,pid):
    if request.method=="POST" and request.user.is_authenticated:
        start=request.POST['startdate']
        package=Packages.objects.get(id=pid)
        price=int(package.price)*int(request.POST['number'])
        booking=Booking(username=request.user,package_id=pid,persons=request.POST['number'],amount=price,startdate=start)
        booking.save()
        a=[]
        return render(request,"tour/add_passenger.html",context={'booking':booking,'no':[a]*int(booking.persons)});
    elif request.user.is_authenticated:
        return render(request,'index')
    else:
        messages.error(request,("Logged in first!"))
        return redirect('login')

# def packagebook(request, pid):
#     package=Packages.objects.get(id=pid)
#     if request.method == 'POST' and package is not None:
#         price=int(package.price)*int(request.POST['number'])
#         # print(package.price, request.POST['number'])
#         return render(request, 'tour/packagebook.html', {'price': price, 'pid': pid})
#     else:
#         return redirect('index')

        
def payment_initial(request):
    if request.method=="POST" and request.user.is_authenticated:
        # data=[]
        number=int(request.POST['num'])
        bid=int(request.POST['bid'])
        for i in range(1,number+1):
            p1=Passenger(booking_id=bid,name=request.POST['name'+str(i)],aadhar=request.POST['aadhar'+str(i)],gender=request.POST['gender'+str(i)],age=int(request.POST['age'+str(i)]))
            p1.save()
            # data.append({'name': request.POST['name'+str(i)], 'aadhar': request.POST['aadhar'+str(i)], 'gender': request.POST['gender'+str(i)], 'age': request.POST['age'+str(i)]})
        # print(data)
        param_dict = {
            'MID': 'merchantid',
            'ORDER_ID': 'order1',
            'TXN_AMOUNT': '1',
            'CUST_ID': 'email',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'tour/paytm.html', {'param_dict':param_dict})

    else:
        return render(request,'index')

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    global checksum
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'tour/paymentstatus.html', {'response': response_dict})