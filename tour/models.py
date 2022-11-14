from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer_detail(models.Model):
    avatar=models.ImageField(upload_to="pics",blank=True,default='pics/default.jpg')
    username=models.ForeignKey(User,on_delete=models.CASCADE,default='user')
    firstname=models.CharField(max_length=50,default="firstname")
    lastname=models.CharField(max_length=50,default="lastname")
    email=models.CharField(max_length=100,default="email")
    dob=models.CharField(max_length=20,null=True)
    mobile = models.CharField( max_length=20,null=True, default="+91 00000-00000")
    address = models.CharField(max_length=200,null=True,default="")
    passport = models.CharField(max_length=20,null=True,default="")
    aadhar = models.CharField(max_length=20,null=True,default="")
    gender = models.CharField(max_length=20,null=True,default="")
    

class Packages(models.Model):
    id = models.AutoField(primary_key=True)
    city=models.CharField(max_length=50)
    heading=models.CharField(max_length=150)
    sub_title=models.CharField(max_length=150,blank=True)
    price=models.IntegerField()
    desc=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='pics',blank=True)
    duration=models.IntegerField()


class Booking(models.Model):
    id = models.AutoField(primary_key=True);
    username=models.ForeignKey(User,on_delete=models.CASCADE,default='user')
    package=models.ForeignKey('Packages',on_delete=models.CASCADE)
    persons=models.IntegerField()
    startdate=models.CharField(max_length=100,default="1/1/2022")
    amount=models.IntegerField(default=0)
    paid=models.BooleanField(default=False)
    agent=models.CharField(max_length=200,blank=True,null=True)
    agent_mobile=models.CharField(max_length=20,blank=True,null=True)

class Passenger(models.Model):
    booking=models.ForeignKey('Booking',on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    aadhar=models.CharField(max_length=200)
    age=models.IntegerField()

class newsbar(models.Model):
    id=models.AutoField(primary_key=True)
    photo=models.ImageField(upload_to="pics",blank=True,default='pics/default.png')
    date=models.IntegerField()
    month=models.CharField(max_length=25)
    heading=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)   

class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=1000)


