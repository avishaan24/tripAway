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
MERCHANT_KEY = "E0c6h8GCaHIvQKvZ";
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

def contact(request):
    return render(request,'tour/contact.html');

def news(request):
    return render(request,'tour/news.html');

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

def payment(request):
    if request.method=="POST" and request.user.is_authenticated:
        bid=request.POST['bid']
        booking=Booking.objects.get(id=int(request.POST['bid']))
        fee=str(booking.amount)
        name=str(booking.username)
        # print(type(bid),type(fee),type(name))
        param_dict = {
            'MID': 'ZFQqQS88985919412502',
            'ORDER_ID': bid,
            'TXN_AMOUNT': fee,
            'CUST_ID': name,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'tour/paytm.html', {'param_dict':param_dict})
    else:
        return render(request,'index')
        
def payment_initial(request):
    if request.method=="POST" and request.user.is_authenticated:
        number=int(request.POST['num'])
        bid=int(request.POST['bid'])
        for i in range(1,number+1):
            p1=Passenger(booking_id=bid,name=request.POST['name'+str(i)],aadhar=request.POST['aadhar'+str(i)],gender=request.POST['gender'+str(i)],age=int(request.POST['age'+str(i)]))
            p1.save()
        book=Booking.objects.get(id=bid)
        pack=Packages.objects.get(id=book.package_id)
        data={'book':book,'pack':pack}
        return render(request,'tour/payment.html',data)

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