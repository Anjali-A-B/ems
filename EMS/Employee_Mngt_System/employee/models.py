
from django.db import models
from django.contrib.auth.models import User 
from django.db import models
from django.utils.translation import gettext as _


'''class Event(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    description = models.TextField()
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Events"'''
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=100)
    description = models.TextField()
    certificate = models.FileField(upload_to='certificates/', null=True, blank=True)

    def __str__(self):
        return self.event_name

"""class Employee(models.Model):

    employee_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    DEPARTMENT_CHOICES = (
        ('Physics', 'Physics'),
        ('Mathematics', 'Mathemathics'),
        ('Computer Science', 'Computer Science'),
        ('Chemistry', 'Chemistry'),
        ('Economics', 'Economics'),
        ('History', 'History'),
        ('Politics', 'Politics'),
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Malayalam', 'Malayalam'),
        ('Sanskrit', 'Sanskrit'),
        ('Botany', 'Botany'),
        ('Statistics', 'Statistics'),
        ('Zoology', 'Zoology'),
        ('Commerce', 'Commerce'),
        ('Physical Education', 'Physical Education'),
    )
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    adhar_number = models.CharField(max_length=12)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    current_address = models.TextField()
    residential_address = models.TextField()
    date_of_joining = models.DateField()
    salary=models.CharField(max_length=10)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)

    def __str__(self):
        return self.first_name"""

class LeaveRequest(models.Model):
    #employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='Pending')


# Profile

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    aadhar_number = models.CharField(max_length=12)
    DEPARTMENT_CHOICES = [
        ('Physics', 'Physics'),
        ('Mathematics', 'Mathemathics'),
        ('Computer Science', 'Computer Science'),
        ('Chemistry', 'Chemistry'),
        ('Economics', 'Economics'),
        ('History', 'History'),
        ('Politics', 'Politics'),
        ('English', 'English'),
        ('Hindi', 'Hindi'),
        ('Malayalam', 'Malayalam'),
        ('Sanskrit', 'Sanskrit'),
        ('Botany', 'Botany'),
        ('Statistics', 'Statistics'),
        ('Zoology', 'Zoology'),
        ('Commerce', 'Commerce'),
        ('Physical Education', 'Physical Education'),
    ]
    department = models.CharField(max_length=30, choices=DEPARTMENT_CHOICES,null=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,null=True)
    date_of_birth = models.DateField()
    date_of_joining = models.DateField()
    current_address = models.TextField()
    residential_address = models.TextField()
    status_choices = [
        ('working', 'Working'),
        ('retired', 'Retired'),
        ('leave', 'On Leave'),
        ('transfer', 'Transferred'),
    ]
    status = models.CharField(max_length=10, choices=status_choices)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    cv = models.FileField(upload_to='cv/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}"
