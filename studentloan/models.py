from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.

#


class Customer(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 to_field='username', primary_key=True, blank=True)
    aadharCardNo = models.CharField(verbose_name="Aadhar Card No", max_length=12)
    panCardNo = models.CharField(verbose_name="Pan Card No", max_length=10)
    frontPan = models.FileField(verbose_name="Front Pan", upload_to='studentloan/images',
                                default="")
    backPan = models.FileField(verbose_name="Back Pan", upload_to='studentloan/images', default="")
    frontAadhar = models.FileField(verbose_name="Front Aadhar",
                                   upload_to='studentloan/images/', default="")
    backAadhar = models.FileField(verbose_name="Back Aadhar",
                                  upload_to='studentloan/images/', default="")
    selfie = models.FileField(verbose_name="Selfie",
                              upload_to='studentloan/images/', blank=True, null=True)
    fine = models.IntegerField(verbose_name="Fine", default=0, blank=True)
    completion = models.CharField(verbose_name="status", blank=True,
                                  default="partial", max_length=10)

    def __str__(self):
        return self.aadharCardNo


class Bank(models.Model):
    banks = open("studentloan/static/studentloan/files/bank.txt", 'r')
    bank = []
    for i in banks:
        bank.append((i.rstrip(), i.rstrip()))
    banks.close()
    bank_id = models.AutoField(primary_key=True, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE,
                                 to_field='username', blank=True)
    acc_no = models.CharField(verbose_name="Account Number", max_length=10, default="")
    bank_name = models.CharField(verbose_name="Bank Name", max_length=50, default="", choices=bank)
    acc_hol_name = models.CharField(verbose_name="Account Holder Name", max_length=30, default="")
    ifsc = models.CharField(verbose_name="IFSC", max_length=10, default="")

    def __str__(self):
        return self.bank_name


amt_choices = [
    (500, '500'),
    (1000, '1000'),
    (1500, '1500')
]
time_choices = [
    (1, '1 Month'),
    (2, '2 Months'),
    (3, '3 Months')
]

class Borrow(models.Model):
    trasaction_id = models.AutoField(primary_key=True)
    trasaction_date = models.DateField(auto_now=True)
    username = models.ForeignKey(User, to_field="username" ,on_delete=models.CASCADE,blank=True)
    borrow_amt = models.IntegerField( blank=True,choices=amt_choices)
    borrow_month = models.IntegerField( blank=True,choices=time_choices)

class Lend(models.Model):
    trasaction_id = models.AutoField(primary_key=True)
    trasaction_date = models.DateField(auto_now=True)
    username = models.ForeignKey(Customer, on_delete=models.CASCADE,blank=True)
    lend_amt = models.IntegerField(blank=True,choices=amt_choices)
    lend_month = models.IntegerField( blank=True,choices=time_choices)
    # payment = models.IntegerField(unique=False, blank=True, default="")
    def __str__(self):
        return self.username
