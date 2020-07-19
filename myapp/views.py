from django.shortcuts import render,HttpResponse,redirect
from .models import (
    CourseCategary,
    CourseLesson,
    Videos,
    UserPurchagedCourse)
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

def buy_course(request,cid):
    if request.method=='POST':
        course_id=request.POST['cid']
        uid=request.session['uid']
        price=request.POST['price']
        UserPurchagedCourse(cid=course_id,uid=uid,price=price).save()
        return redirect('/')
    if request.method=='GET':
        course=CourseCategary.objects.get(id=cid)
        return render(request,'myapp/buy_course.html',{'course':course})
        
