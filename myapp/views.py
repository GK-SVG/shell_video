from django.shortcuts import render,HttpResponse,redirect
from .models import (
    CourseCategary,
    CourseLesson,
    Videos,
    UserPurchagedCourse)
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
# Create your views here.
def index(request):
    try:
        uid=request.session['uid']
        purchaged_course=UserPurchagedCourse.objects.filter(uid=uid)
        purchaged_course=[s.cid for s in purchaged_course]
    except:
        purchaged_course=[]
        pass
    courses=CourseCategary.objects.all()
    return render(request,'myapp/index.html',{'courses':courses,'purchaged_course':purchaged_course})


def allcourse(request):
    try:
        uid=request.session['uid']
        purchaged_course=UserPurchagedCourse.objects.filter(uid=uid)
        purchaged_course=[s.cid for s in purchaged_course]
    except:
        purchaged_course=[]
        pass
    courses=CourseCategary.objects.all()
    return render(request,'myapp/allcourse.html',{'courses':courses,'purchaged_course':purchaged_course})
def course_detail(request,id):
    try:
        uid=request.session['uid']
        purchaged_course=UserPurchagedCourse.objects.filter(uid=uid)
        purchaged_course=[s.cid for s in purchaged_course]
    except:
        purchaged_course=[]
        pass
    course=CourseCategary.objects.get(id=id)
    return render(request,'myapp/course_details.html',{'course':course,'purchaged_course':purchaged_course})

def about(request):
    return render(request,'myapp/about.html')

def contact(request):
    if request.method=='POST':
        message=request.POST['message']
        name=request.POST['name']
        email=request.POST['email']
        user_subject=request.POST['subject']
        subject,from_email,to=user_subject,email,'gk32239@gmail.com'
        html_content="Hello, I am "+ name +" "+ " "+message + "<br> FROM "+ email 
        msg = EmailMultiAlternatives(subject, html_content,from_email,[to])
        msg.attach_alternative(html_content,'text/html')
        msg.send()  
        return redirect("/")   
    return render(request,'myapp/contact.html')

def playvideo(request,cid,vid):
    try:
        uid=request.session['uid']
        user_courses=UserPurchagedCourse.objects.filter(uid=uid)
        user_courses=[c.cid for c in user_courses]
        if cid in user_courses:
            course=CourseCategary.objects.get(id=cid)
            videos=Videos.objects.get(id=vid)
            return render(request,'myapp/playvideo.html',{'videos':videos,'course':course})
        else:
            purchaged_course=[]
            course=CourseCategary.objects.get(id=cid)
            return render(request,'myapp/course_details.html',{'course':course,'purchaged_course':purchaged_course})
    except:
        return redirect('/')

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
        
