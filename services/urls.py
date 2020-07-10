from django.urls import path
from .import views

urlpatterns = [
    path('validate_mail/',views.validate_mail_id,name='validate_mail_id')
]
