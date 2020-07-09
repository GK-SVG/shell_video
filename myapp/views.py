from django.shortcuts import render
from .models import (
    CourseCategary,
    CourseLesson,
    Videos)
# Create your views here.
def index(request):
    courses=CourseCategary.objects.all()
    return render(request,'myapp/index.html',{'courses':courses})


def allcourse(request):
    courses=CourseCategary.objects.all()
    return render(request,'myapp/allcourse.html',{'courses':courses})
def course_detail(request,id):
    course=CourseCategary.objects.get(id=id)
    return render(request,'myapp/course_details.html',{'course':course})

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def playvideo(request,cid,vid):
    course=CourseCategary.objects.get(id=cid)
    videos=Videos.objects.get(id=vid)
    return render(request,'myapp/playvideo.html',{'videos':videos,'course':course})