from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('courses',views.allcourse,name='allcourse'),
    path('course_detail',views.course_detail,name='Course_Detail'),
    path('about/',views.about,name='About'),
]
