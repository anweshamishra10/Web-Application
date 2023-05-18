This is a web application developed using Python and Django framework.

**Description**

This project aims to provide a user authentication system with email and password. It allows users to create an account, login with their credentials, and perform various tasks within the application.

**Features**

1. User registration and account creation
2. Email verification for account activation
3. User login and authentication
4. Password reset functionality
5. Secure storage of user data
6. Basic frontend using HTML and CSS

Screen 1: Login

User enters “Email ID” and “Password” and then clicks on “Login” button to Sign-in.
Facebook and Google Sign-in is disabled for time being.

Screen 2. Create new account

User clicks on “Create Account” on Screen 1 to get redirected to Screen 2. User enters 
“Name”, “Email ID”, “Phone”, “Password” (Password is masked, and can be seen by clicking 
eye button). User then clicks on “Sign Up” button to receive OTP on phone for verification in 
Screen 3.
If user already has an account, then user can click on “Signin” to get redirected to Screen 1.

Screen 3. Signup Verification

User enters the OTP received on Phone and then clicks on “Submit” button to complete the 
verification process.
A timer of 60 seconds is displayed on Screen 3. If user didn’t receive OTP in 60 seconds, then 
user clicks on “Resend” to resend OTP. This resent OTP has to be the same OTP that was sent 
in the first Attempt.

Screen 4. Account Created

User gets a prompt message than account has been created. User then clicks on “Login Now” 
button to get redirected to Screen 1.

**NOTE**

The _init_.py, admins.py, apps.py, forms.py, models.py, tests.py and views.py should be in a folder named "authentication".
The _init_.py, asgi.py, settings.py, urls.py and wsgi.py should be in a folder named "web_app".
The style.css file should be inside a folder named "static", which is inside the authentication folder.
The html files should be inside a folder named "templates", which is inside the authentication folder.
