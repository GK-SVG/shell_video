from django.urls import path
from .import views

urlpatterns = [
    path('signup/',views.signup,name='singup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('profile/<slug:user>/',views.profile,name='Profile'),
]
