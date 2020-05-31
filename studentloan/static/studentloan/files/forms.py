from django import forms


class signUpForm(forms.Form):
    fullName = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Full Name'}), label='Full Name', max_length=50)
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Email'}), label='Email', max_length=100)
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Username', 'id': 'username', 'onblur': 'ucheck()'}), label='Username', max_length=50)
    mobileNumber = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'type': 'number', 'placeholder': 'Mobile Number'}), max_value=9999999999)
    password = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'password'}), label='Password', max_length=30)
    cnfPassword = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'form-control', 'type': 'password', 'placeholder': 'confirm Password'}), label='Password', max_length=30)


class customers(forms.Form):
    panCardNo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'panCardNo', 'type': 'text', 'placeholder': 'Pan Card No'}))
    aadharCardNo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'aadharCardNo', 'type': 'text', 'placeholder': 'Aadhar Card No'}))
    frontPan = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'id': 'frontPan'}))
    backPan = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'id': 'backPan'}))
    frontAadhar = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'id': 'frontAadhar'}))
    backAadhar = forms.FileField(widget=forms.FileInput(
        attrs={'class': 'custom-file-input', 'id': 'backAadhar'}))


class loginFrom(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mr-sm-2', 'type': 'username', 'placeholder': 'username'}), label='Username', max_length=50)
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mr-sm-2', 'type': 'password', 'placeholder': 'password'}), label='Password', max_length=30)
