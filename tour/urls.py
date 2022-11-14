from django.urls import path
# from tour import views
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('about/',views.about,name='about'),
    path('all_packages/',views.packages,name='all'),
    path('search/',views.search,name='search'),
    path('edit/',views.edit,name='edit'),
    path('contact/',views.contact,name='contact'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='prof'),
    path('bookings/',views.booking_details,name='booking'),
    path('package/<int:pid>/passenger',views.passenger,name='passenger'),
    path('packageview/<int:pid>',views.packageview,name='packageview'),
    path('paymentdetails/',views.payment,name='checkout'),
    path('payment/',views.payment_initial,name='payment'),
    path('handlerequest/',views.handlerequest,name='handlerequest')
    # path('package/<int:pid>',views.packagebook,name='packagebook'),
]