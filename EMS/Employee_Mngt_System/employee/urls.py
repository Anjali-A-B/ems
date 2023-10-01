from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
#from .views import profile, edit_profile

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee_login/', views.employee_login, name='employee_login'),
    path('employee_registration/', views.employee_registration, name='employee_registration'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
   
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_done.html"), name='password_reset_complete'),
   
    path('add-event/', views.add_event, name='add-event'),
    path('edit-event/<int:event_id>/', views.edit_event, name='edit-event'),
    path('employee-events/', views.employee_events, name='employee_events'),
    path('delete/<int:event_id>/', views.event_delete, name='event_delete'),

    #path('employee_form', views.employee_form, name='employee_form'),
    #path('profile/', views.employee_profile, name='employee_profile'),
    #path('admin/employee/', views.admin_employee_list, name='admin_profile'),
 
    #path('leave/', views.leave_request, name='leave_request'),

    #path('employee_profile/', views.employee_profile, name='employee_profile'),
    #path('profile_success/', views.profile_success, name='profile_success'),




    #Leave
    path('apply-leave/', views.apply_leave, name='apply_leave'),
    path('all-leaves/', views.all_leaves, name='all_leaves'),


    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),


]
