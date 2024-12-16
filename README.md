# signup-page-OTP

Here’s a detailed note on implementing a Signup Page with OTP Gmail Verification in Django:

Signup Page with OTP Gmail Verification in Django
Overview
This implementation allows users to sign up on your Django web application with an extra layer of security using OTP (One-Time Password) verification sent to their Gmail account. The process ensures that the email provided during signup is valid and accessible by the user.


        for i in range(4):
            otp_digit = request.POST.get(f'otp_digit_{i}')
            if otp_digit:  # Ensure the OTP digit exists
                otp_digits.append(otp_digit)
            else:
                otp_digits.append('') 

        # Join OTP digits into a single string
        otp = ''.join(otp_digits)
        


        # Get the OTP stored in session
        session_otp = request.session.get('otp', '')






            otp = str(random.randint(1000, 9999))
            request.session['otp'] = otp  # Store OTP in session

          

           
                send_mail(
                    subject,
                    message,
                    'your_email@gmail.com',  # Sender email
                    [email],  # Recipient email
                    fail_silently=False,
                )
     



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'  # Use an app password for Gmail

