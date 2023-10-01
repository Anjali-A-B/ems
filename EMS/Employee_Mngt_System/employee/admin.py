from django.contrib import admin
from .models import Event
from .models import UserProfile
from .models import LeaveRequest

admin.site.register(Event)

admin.site.register(UserProfile)

admin.site.register(LeaveRequest)