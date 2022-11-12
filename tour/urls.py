from django.urls import path
# from tour import views
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('about/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('package/<int:pid>/passenger',views.passenger,name='passenger'),
    path('packageview/<int:pid>',views.packageview,name='packageview'),
    path('payment/',views.payment_initial,name='payment'),
    path('handlerequest/',views.handlerequest,name='handlerequest')
    # path('package/<int:pid>',views.packagebook,name='packagebook'),
]