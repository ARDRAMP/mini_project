from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def index(request):
    return render(request,'index.html')
    
def c1(request):
    return render(request,'c1.html')
def c2(request):
    return render(request,'c2.html')
def c3(request):
    return render(request,'c3.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CustomUser # Import your CustomUser model

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        disability_type = request.POST['disability_type']
        assistance_required = request.POST['assistance_required']
        parent_name = request.POST['parent_name']
        parent_nam = request.POST['parent_nam']
        parent_contact = request.POST['parent_contact']

        # Validate passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Create a new CustomUser instance
        user = CustomUser(
            username=username,
            first_name=name,
            email=email,
            disability_type=disability_type,
            assistance_required=assistance_required,
            father_name=parent_name,
            mother_name=parent_nam,
            parent_contact=parent_contact
        )

        # Set the password using set_password to hash it
        user.set_password(password)

        # Save the user instance
        user.save()

        # Redirect to a success page or any other desired page
        return redirect('user_login')

    return render(request, 'register.html')

    
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Replace 'index' with the name of your home page URL pattern
        else:
            error_message = "Invalid credentials. Please try again."

            # You can pass the error message to the template for display
            return render(request, "login.html", {'error_message': error_message, 'username': username})

    # If the request method is GET, just render the login page
    return render(request, "login.html")

