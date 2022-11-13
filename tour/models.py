from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Customer_detail(models.Model):
    avatar=models.ImageField(upload_to="pics",blank=True,default='pics/default.png')
    username=models.ForeignKey(User,on_delete=models.CASCADE,default='user')
    firstname=models.CharField(max_length=50,default="firstname")
    lastname=models.CharField(max_length=50,default="lastname")
    email=models.CharField(max_length=100,default="email")
    age=models.IntegerField(null=True)
    mobile = models.CharField( max_length=13,null=True)
    address = models.CharField(max_length=200,null=True)
    passport = models.CharField(max_length=20,null=True)
    aadhar = models.CharField(max_length=20,null=True)
    gender = models.CharField(max_length=20,null=True)
    

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

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=1000)
    


