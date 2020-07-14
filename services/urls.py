from django.urls import path
from .import views

urlpatterns = [
    path('validate_mail/',views.validate_mail_id,name='validate_mail_id'),
    path('validate_reset_password/',views.validate_reset_password,name='validate_reset_password')
]
