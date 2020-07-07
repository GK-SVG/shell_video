from django.shortcuts import render
from .models import (
    CourseCategary,
    CourseLesson)
# Create your views here.
def index(request):
    courses=CourseCategary.objects.all()
    return render(request,'myapp/index.html',{'courses':courses})


def allcourse(request):
    courses=CourseCategary.objects.all()
    return render(request,'myapp/allcourse.html',{'courses':courses})
def course_detail(request,id):
    course=CourseCategary.objects.get(id=id)
    course_lessons=CourseLesson.objects.filter(lessons=course.title)
    return render(request,'myapp/course_details.html',{'course':course,'course_lessons':course_lessons})

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    return render(request,'myapp/contact.html')

def playvideo(request):
    return render(request,'myapp/playvideo.html')