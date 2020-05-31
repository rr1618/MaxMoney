import base64
import json
from django.db import connections
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import Context, Template
import datetime
import hashlib
from .Checksum import *
from random import randint
from .models import Customer, Bank, Borrow, Lend
from django.contrib import messages
from django.core.files.base import ContentFile
from django.contrib.auth.models import User, auth
from .forms import signUpForm, loginFrom, customers, bank, paymentForm, borrowForm, lendForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse, request, JsonResponse
MERCHANT_KEY = 'f2tSYW5ayEjP_Eld'
# Forms
lform = loginFrom()
pay = paymentForm()
lendForm = lendForm()
# data manipulation Functions
# base64_file


def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

# check_username


def check_username(request):
    username = request.GET.get('username', None)
    # print("username", username)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

# render functions
# home


def signup(request):
    cform = customers()
    data = {'cform': cform}
    return render(request, "studentloan/signup.html", data)


def register(request):
    if(request.method == "POST"):
        form = signUpForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(
                username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            messages.success(request, 'Your account has been successfully created')
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('studentloan:signup')
        else:
            return JsonResponse({'error': 'username already exists'})
    else:
        return redirect('studentloan:home')


def home(request):
    form = signUpForm()
    loan_list = Borrow.objects.all()
    if(request.user.is_authenticated):
        details = Customer.objects.get(username=request.user)
        print(details)
    else:
        details = {""}
    page = request.GET.get('page', 5)
    paginator = Paginator(loan_list, 5)
    try:
        loanRequests = paginator.page(page)
    except PageNotAnInteger:
        loanRequests = paginator.page(1)
    except EmptyPage:
        loanRequests = paginator.page(paginator.num_pages)
    return render(request, 'studentloan/home.html', {'lform': lform, 'forms': form, 'loanRequests': loanRequests, 'details': details})

# contact


def contact(request):
    details = Customer.objects.get(username=request.user)
    return render(request, 'studentloan/contact.html', {'lform': lform, 'details': details})

# forms render


def login_request(request):
    if(request.method == "POST"):
        form = loginFrom(request.POST)
        if(form.is_valid()):
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(password=password, username=username)
        if(user is not None):
            auth.login(request, user)
            print('login successful')
            return redirect('studentloan:dashboard')
        else:
            return redirect('studentloan:home')
    return redirect('/studentloan')


# render dashboard
@login_required
def basicForm(request):
    # print("basicForm called")
    if(request.method == "POST"):
        cform = customers(request.POST, request.FILES)
        if(cform.is_valid()):
            f = cform.save(commit=False)
            f.username = request.user
            f.completion = "partial"
            f.save()
            cform.save_m2m()
            print("saved")
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
        else:
            return JsonResponse({'error': True, 'errors': cform.errors})
    else:
        cform = customers()
        data = {'cform': cform}
        return render(request, 'studentloan/signup.html', data)


@login_required
def dashboard(request):
    form_to_render = ""
    form_to_render = request.GET.get('name')
    print(form_to_render)
    if(Customer.objects.filter(username=request.user, completion="completed")):
        details = Customer.objects.get(username=request.user)
        banks = Bank.objects.all().filter(username=request.user)
        bankForm = bank()
        bform = borrowForm()
        print("completed")
        data = {'details': details, 'bankForm': bankForm,
                'banks': banks, 'paymentFrom': pay, 'borrowForm': bform, 'lendForm': lendForm, 'form_to_render': form_to_render}
        return render(request, 'studentloan/dashboard.html', data)
    return redirect("studentloan:dashboard")


@login_required
def borrow(request):
    print("borrow")
    if(request.method == "POST"):
        print("borrow")
        bform = borrowForm(request.POST)
        print(bform)
        if(bform.is_valid()):
            print("valid")
            f = bform.save(commit=False)
            f.username = request.user
            f.save()
            bform.save_m2m()
            return redirect('studentloan:home')


# add bank
@login_required
def add_bank(request):
    if(request.method == "POST"):
        bankForm = bank(request.POST)
        print("add bank")
        if(bankForm.is_valid()):
            print("form is valid")
            f = bankForm.save(commit=False)
            f.username = request.user
            f.save()
            bankForm.save_m2m()
            print("Saved")
        return redirect('studentloan:dashboard')


# submit selfie
@csrf_exempt
@login_required()
def submitSelfie(request):
    if(request.method == "POST"):
        selfie = request.POST['selfie']
        selfie = base64_file(selfie, 'rahul.jpg')
        cus = Customer.objects.get(username=request.user)
        cus.selfie = selfie
        cus.completion = "completed"
        cus.save()
        print("saved")
        return JsonResponse({'error': False})
    else:
        print("else executed")
        return JsonResponse({'error': True})
    return redirect('/studentloan')


# loginFrom
@login_required
def logout_request(request):
    auth.logout(request)
    return redirect('/studentloan')


def checkout(request):
    if(request.method == "POST"):
        print("post")
        # checkout_dict = request.POST
        order_id = request.POST['order_id']
        amt = request.POST['amt']
        cust_id = request.POST['cust_id']
        exp_return = request.POST['exp_return']
        borrow_month = request.POST['borrow_month']
        final_list = {
            'order_id': order_id,
            'amount': amt,
            'cust_id': cust_id,
            'exp_return': exp_return,
            'borrow_month': borrow_month
        }
        return render(request, 'studentloan/checkout.html', {'checkout_dict': final_list})


def paynow(request):
    if(request.method == "POST"):
        print(request.POST['order_id'])
        param_dict = {
            'MID': 'rvBMLs79345789604937',
            'ORDER_ID': str(request.POST['order_id']),
            'TXN_AMOUNT': str(request.POST['amt']),
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/studentloan/handlePayment/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        print(param_dict)
    return render(request, 'studentloan/paytm.html', {'param_dict': param_dict})


@csrf_exempt
def handlePayment(request):
    return HttpResponse("done")
