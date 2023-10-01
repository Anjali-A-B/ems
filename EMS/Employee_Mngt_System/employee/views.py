
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib import messages 
from django.contrib.auth.models import User
from .models import Event
from .forms import EventForm
from django.core.mail import EmailMessage
from django.contrib import messages
from employee.models import *
from django.http import JsonResponse
from .models import LeaveRequest
from .forms import EventForm
from .models import Event



def index(request):
    return render(request, 'index.html')


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            auth.login(request, user)
            return redirect('admin_dashboard')
        else:
            # Authentication failed, add an error message
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'admin_login.html')



def admin_dashboard(request):
    # Add your admin dashboard logic here
    leave = leave_request.objects.all()
    return render(request, 'admin_dashboard.html',leave)


def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and not user.is_staff:
            auth.login(request, user)
            return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, 'employee_login.html')

def employee_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            # Check if the username or email already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.error(request, 'Username or email already exists. Please choose another.')
            else:
                # Create a new user and save it to the database
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registered successfully. You can now log in.')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, 'employee_registration.html')

'''def sendemail(request):
    useremail = request.POST['email']
    email = EmailMessage('Subject', 'Body', to=useremail)
    email.send()  
    return render(request, 'password_reset_sent.html')'''

from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from django.shortcuts import render, redirect

def sendemail(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email="EmployeeManagementSystem@yahoo.com",  # Replace with your Yahoo email
                email_template_name='password_reset_email.html',
                subject_template_name='password_reset_subject.txt',
            )
            messages.success(request, 'Password reset email sent.')
            return redirect('password_reset_done')

    else:
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form})


def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')


#Events
def employee_events(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'employee_events.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Set a success message
            message = "Event added successfully!"
            return render(request, 'add_event.html', {'form': form, 'message': message})
    else:
        form = EventForm()
    
    return render(request, 'add_event.html', {'form': form})


def upload_event_certificate(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            # Handle successful upload
            return redirect('success_page')  # Redirect to a success page
    else:
        form = EventForm()
    return render(request, 'upload_event_certificate.html', {'form': form})



def edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            # Add a success message
            messages.success(request, 'Changes made successfully.')
    else:
        form = EventForm(instance=event)

    return render(request, 'edit_event.html', {'form': form, 'event': event})

def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    # Get the ID of the next event, if available
    next_event_id = Event.objects.filter(id__gt=event_id).order_by('id').first()
    
    if request.method == 'POST':
        event.delete()
        
        # Redirect to the next event if available, otherwise, redirect to the event list
        if next_event_id:
            return redirect('edit_event', event_id=next_event_id.id)
        else:
            return redirect('employee_events')
    
    return render(request, 'event_delete_confirm.html', {'event': event})


# Profile

# views.py

'''from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm

def employee_form(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or another view
            return redirect('success_page')  
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})
'''


#Leave
'''def leave_request(request):
    if request.method == 'POST':
        # Process the leave request and save it to the database
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        leave_type = request.POST['leave_type']
        reason = request.POST['reason']
        employee = request.user  # Assuming you have employee authentication in place

        leave_request = LeaveRequest.objects.create(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
            leave_type=leave_type,
            reason=reason
        )
        leave_request.save()

        # Notify administrators or managers via email
        subject = 'New Leave Request'
        message = f'A new leave request has been submitted by {employee.username}. Please review it in the admin panel.'
        # from_email = 'anjalianjuzz007@gmail.com'  # Your email address
        # recipient_list = ['admin1@example.com', 'admin2@example.com']  # List of admin email addresses

        # email = EmailMessage(subject, message, from_email, recipient_list)
        # email.send()

        # Save the response in the LeaveResponse model
        response_message = 'Leave request sent. Please wait for admin\'s response.'
        return JsonResponse({'message': response_message})

    return render(request, 'leave.html')'''


# leave_app/views.py

# leave_management_app/views.py
from django.shortcuts import render, redirect
from .models import LeaveRequest
from .forms import LeaveRequestForm
from django.contrib import messages

def apply_leave(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)

        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user.employeeprofile
            leave_request.save()
            messages.success(request, 'Leave request submitted successfully')
            return redirect('apply_leave')
    else:
        form = LeaveRequestForm()

    return render(request, 'apply_leave.html', {'form': form})

def all_leaves(request):
    if request.user.is_staff:
        leaves = LeaveRequest.objects.all()
    else:
        leaves = LeaveRequest.objects.filter(employee=request.user.employeeprofile)

    return render(request, 'all_leaves.html', {'leaves': leaves})


# profile

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If UserProfile doesn't exist, create a new one
        user_profile = UserProfile.objects.create(
            user=request.user,
            employee_id='',
            first_name='',
            last_name='',
            email='',
            phone_number='',
            aadhar_number='',
            department='',
            gender='',
            date_of_birth='2023-03-21',
            date_of_joining='2023-09-23',
            current_address='',
            residential_address='',
            status='',
            salary='0.00',
            cv=''
        )

    return render(request, 'profile.html', {'user_profile': user_profile})

@login_required
def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'edit_profile.html', {'form': form})
