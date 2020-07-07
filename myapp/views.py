from django.shortcuts import render
from .models import (
    CourseCategary)
# Create your views here.
def index(request):
    courses=CourseCategary.objects.all()
    return render(request,'myapp/index.html',{'courses':courses})


def allcourse(request):
    return render(request,'myapp/allcourse.html')

def course_detail(request):
    return render(request,'myapp/course_details.html')

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def playvideo(request):
    return render(request,'myapp/playvideo.html')