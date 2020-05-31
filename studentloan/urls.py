from django.urls import path
from django.conf import settings
from .views import *

app_name = 'studentloan'

urlpatterns = [
    path('', home, name="home"),
    path('register/', register, name="register"),
    path('signup/', signup, name="signup"),
    path('login/', login_request, name='login'),
    path('check_username/', check_username, name='check_username'),
    path('contact/', contact, name="contact"),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/borrow/', borrow, name='borrow'),
    path('dashboard/basicForm', basicForm, name='basicForm'),
    path('dashboard/submitSelfie/', submitSelfie, name='selfie'),
    path('dashboard/addbank/', add_bank, name='add_bank'),
    path('logout/', logout_request, name='logout'),
    path('checkout/', checkout, name='checkout'),
    path('paynow/',paynow,name="paynow"),
    path('handlePayment/', handlePayment, name='handlePayment'),
]
