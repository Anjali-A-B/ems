from django import forms
from .models import Event
from .models import LeaveRequest

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'date', 'venue', 'description', 'certificate']
        

from .models import LeaveRequest

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['leave_type', 'start_date', 'end_date', 'reason']


from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
