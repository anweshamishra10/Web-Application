from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email ID')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')

class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())

class VerificationForm(forms.Form):
    otp = forms.CharField(label='OTP')
