from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Customer, Bank, Borrow, Lend


class signUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']


class customers(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class loginFrom(forms.Form):
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control validate', 'type': 'password', 'id': 'pass'}), max_length=30)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control validate', 'type': 'text', 'id': 'pass'}), max_length=30)


class bank(ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(bank, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


amt_choices = [
    ('500', '500'),
    ('1000', '1000'),
    ('1500', '1500')
]
time_choices = [
    ('1', '1 Month'),
    ('2', '2 Months'),
    ('3', '3 Months')
]


class borrowForm(ModelForm):
    class Meta:
        model = Borrow
        fields = ['borrow_amt', 'borrow_month']

class lendForm(ModelForm):
    class Meta:
        model=Lend
        fields=['lend_amt','lend_month']

class paymentForm(forms.Form):
    amount = forms.ChoiceField(choices=amt_choices)
    time = forms.ChoiceField(choices=time_choices)
    # first_name = forms.CharField()
    # email = forms.CharField()
    # product_info = forms.CharField()
