from django.contrib import admin
from .models import Customer_detail,Packages,Booking,Passenger

# Register your models here.

admin.site.register(Customer_detail)
admin.site.register(Packages)
admin.site.register(Booking)
admin.site.register(Passenger)
