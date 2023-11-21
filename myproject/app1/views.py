from telnetlib import LOGOUT
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Enrollment, Teacher

def index(request):
    return render(request,'index.html')
    
def c1(request):
    return render(request,'c1.html')
def c2(request):
    return render(request,'c2.html')
def c3(request):
    return render(request,'c3.html')
def studenthome(request):
    return render(request,'studenthome.html')
def teacherhome(request):
    return render(request,'teacherhome.html')
def enroll(request):
    if request.method == 'POST':
        # Get the course name from the form submission
        course_name = request.POST.get('courses')

        # Get the currently logged-in user
        user = request.user

        # Create an enrollment record
        Enrollment.objects.create(user=user, course_name=course_name)

        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})

    return render(request, 'enroll.html')

def task(request):
    return render(request,'task.html')
def calendar(request):
    return render(request,'calendar.html')
def admincourse(request):
     return render(request,'admincourse.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser, Enrollment

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
            
            if user.is_student:
                login(request, user)
                return redirect('studenthome')
            elif user.is_teacher:
                login(request, user)
                return redirect('studenthome')

        else:
            error_message = "Invalid credentials. Please try again."


            # You can pass the error message to the template for display
            return render(request, "login.html", {'error_message': error_message, 'username': username})

    # If the request method is GET, just render the login page
    return render(request, "login.html")
from django.shortcuts import render, redirect
from .models import Teacher
from django.http import HttpResponse

def dashboard(request):
    if request.method == 'POST':
        # Get data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        course = request.POST.get('course')

        # Create a new Teacher object and save it to the database
        new_teacher = Teacher(name=name, email=email, password=password, course=course)
        new_teacher.save()

        new_user = CustomUser.objects.create_user(username=email, email=email, password=password)
        new_user.is_student = False 
        new_user.is_teacher = True 
        new_user.save()        
        return redirect('dashboard') 

    # If the request method is not POST, render the dashboard page
    teachers = Teacher.objects.all()
    return render(request, 'dashboard.html', {'teachers': teachers})



def studentlist(request):

    return render(request, 'studentlist.html')
def loggout(request):
    LOGOUT(request)
    return redirect("index")