from django.shortcuts import render, redirect, reverse
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
import random
from django.core.validators import validate_email
from django.core.exceptions import ValidationError



# Signup page view
def signupPage(request):
    return render(request, "signup.html",{'otp_range': range(4)})

# Login page view
def loginPage(request):
    return render(request, "login.html")

# Signup logic
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        otp_digits = []
        
        # Collect OTP digits from the form
        for i in range(4):
            otp_digit = request.POST.get(f'otp_digit_{i}')
            if otp_digit:  # Ensure the OTP digit exists
                otp_digits.append(otp_digit)
            else:
                otp_digits.append('')  # Empty string if OTP digit is missing
        
        # Join OTP digits into a single string
        otp = ''.join(otp_digits)
        print(f"Entered OTP: {otp}")
        
        print(username, otp, email)
        
        # Get the OTP stored in session
        session_otp = request.session.get('otp', '')
        print(f"Session OTP: {session_otp}")
        
        if email and username and password and otp == session_otp:
            print('OTP checked')
            try:
                user = User.objects.get(email=email)
                pop = {'note': 'Email already exists'}
                return render(request, 'signup.html', pop)
            except User.DoesNotExist:
                # Create new user
                user = User(username=username, email=email, password=password)
                print('User added')
                user.save()
                return render(request, 'login.html', {'note': 'User created successfully'})
        else:
            pop = {'note': 'Invalid OTP or missing fields'}
            return render(request, 'signup.html', pop)





def send_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')

        if email and username:
            try:
                # Validate email format
                validate_email(email)
            except ValidationError:
                return JsonResponse({'status': 'error', 'message': 'Invalid email format'})

            otp = str(random.randint(1000, 9999))
            request.session['otp'] = otp  # Store OTP in session

            subject = "Your OTP Code"
            message = f"Your OTP code is: {otp}\n\nPlease use this code to proceed. It is valid for 10 minutes."

            try:
                send_mail(
                    subject,
                    message,
                    'your_email@gmail.com',  # Sender email
                    [email],  # Recipient email
                    fail_silently=False,
                )
                return JsonResponse({'status': 'success', 'message': 'OTP sent successfully!'})

            except Exception as e:
                print(e)
                return JsonResponse({'status': 'error', 'message': 'Failed to send OTP'})





def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email and password:
            try:
                user = User.objects.get(email=email)
                if user.password == password:
                    d = {
                        'email': user.email,
                        'username': user.username,
                    }
                    return render(request, 'home.html', d)
                else:
                    pop={
                    'note': 'Wrong Password'
                }
                    return render(request, 'login.html',pop)  # Password incorrect
            except User.DoesNotExist:
                pop={
                    'note': 'Email not found'
                }
                return render(request, 'login.html',pop)  # User does not exist


                    
                    
