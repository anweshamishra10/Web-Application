from django.shortcuts import redirect, render
from .forms import SignUpForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.crypto import get_random_string

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Perform login logic here
    return render(request, 'login.html')

def create_account_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        # Perform create account logic here
        # Generate and send OTP to phone
        return redirect('verification')
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Perform account creation logic
            messages.success(request, 'Account created successfully!')
            return redirect('verification')
    else:
        form = SignUpForm()
    return render(request, 'create_account.html', {'form': form})

def verification_view(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        # Verify OTP logic here
        return redirect('account_created')
    return render(request, 'verification.html')

def account_created_view(request):
    return render(request, 'account_created.html')

def send_otp_email(request):
    # Generate OTP
    otp = get_random_string(length=6, allowed_chars='0123456789')

    # Send OTP via email
    subject = 'OTP Verification'
    message = f'Your OTP is: {otp}'
    email = EmailMessage(subject, message, to=['user@example.com'])
    email.send()

    return render(request, 'verification.html', {'otp': otp})

