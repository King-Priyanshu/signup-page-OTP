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
        print(f"Entered OTP: {otp}")

        print(username, otp, email)

        # Get the OTP stored in session
        session_otp = request.session.get('otp', '')






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
     



