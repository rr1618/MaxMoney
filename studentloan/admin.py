from django.contrib import admin

# Register your models here.
from .models import Customer, Bank, Borrow,Lend

admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(Borrow)
admin.site.register(Lend)
