from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Users
from myapp.models import UserPurchagedCourse,CourseCategary
from services.views import send_verification_link,reset_password_mail_validation

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['Password']
        try:
            user=Users.objects.get(email=email,password=password)
            if user.mail_validate==0:
                token=send_verification_link(user)
                messages.warning(request,'Please check your mail to conform your email')
                return redirect('/')
            else:
                request.session['user']=user.user
                request.session['uid']=user.id
                messages.success(request,'Login Successfullly')
                return redirect('/')
        except:
            messages.error(request,'invalid credencials')
            return redirect('/')

    

def signup(request):
    if request.method=='POST':
        username=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # checkpoints 
        #username length checker
        

        # username charkters checker
        if not username.isalnum() :
             messages.error(request,'Username only contain alphaNumeric value')
             return redirect('/')    

        # password1 and password2 checker     
        if pass1 != pass2 :
            messages.error(request,'Passwords do not match')
            return redirect('/')
        # creating user
        try:
            myuser=Users.objects.get(user=username)
            myuser2=Users.objects.get(email=email)
            messages.error(request,'The username/email you entered has already been taken. Please try another username/email')
            return redirect('/') 
        except:
            myuser = Users(user=username,email=email,password=pass1,phone=phone)
            myuser.save()
            send_verification_link(myuser)
            messages.success(request,'Account created successfully  Please check your mail to conform your email')
            return redirect('/') 
    else:
        return redirect('')

def logout(request):
    request.session.flush()
    messages.success(request,'Logout Sucessfully')
    return redirect('/')


def reset_password(request):
    if request.method=='POST':
        email=request.POST['email']
        user=Users.objects.get(email=email)
        token=reset_password_mail_validation(user)
        return redirect('/')
      
def profile(request,user):
    user=Users.objects.get(user=user)
    courses=UserPurchagedCourse.objects.filter(uid=user.id)
    courses=[CourseCategary.objects.get(id=i.cid) for i in courses]
    print("user====",user,"\nCourses===",courses)
    return render(request,"myapp/userProfile.html",{"user":user,"courses":courses})