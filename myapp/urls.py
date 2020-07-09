from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('courses/',views.allcourse,name='allcourse'),
    path('course_detail/<int:id>/',views.course_detail,name='Course_Detail'),
    path('about/',views.about,name='About'),
    path('contact/',views.contact,name='Contact'),
    path('playvideo/<int:cid>/<int:vid>/',views.playvideo,name='playvideo'),
]
