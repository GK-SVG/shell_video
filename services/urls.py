from django.urls import path
from .import views

urlpatterns = [
    path('validate_mail/',views.validate_mail_id,name='validate_mail_id'),
    path('validate_email_reset_password/',views.validate_email_reset_password,name='validate_email_reset_password'),
    path('reset_password/<int:uid>/',views.reset_password,name='reset_password')
]
