from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Users
from services.views import send_verification_link,reset_password_mail_validation


   

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['Password']
        try:
            user=Users.objects.get(email=email,password=password)
            if user.mail_validate==0:
                token=send_verification_link(user)
                return HttpResponse('Please check your mail to conform your email')
            else:
                request.session['user']=user.user
                request.session['uid']=user.id
                return redirect('/')
        except:
            return HttpResponse('Please check your credentials')

    

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
             return HttpResponse('Username only contain alphaNumeric value')       

        # password1 and password2 checker     
        if pass1 != pass2 :
            messages.error(request,'Passwords do not match')
            return HttpResponse('Passwords do not match')
        # creating user
        try:
            myuser=Users.objects.get(user=username)
            myuser2=Users.objects.get(email=email)
            messages.error(request,'The username you entered has already been taken. Please try another username.')
            return HttpResponse('The username/email you entered has already been taken. Please try another username/email')
        except:
            myuser = Users(user=username,email=email,password=pass1,phone=phone)
            myuser.save()
            send_verification_link(myuser)
            return HttpResponse('Account created successfully  Please check your mail to conform your email')      
    else:
        return redirect('')

def logout(request):
    request.session.flush()
    return redirect('/')


def reset_password(request):
    if request.method=='POST':
        email=request.POST['email']
        user=Users.objects.get(email=email)
        print('user===',user.email)
        print('user===',user.last_login)
        token=reset_password_mail_validation(user)
        return HttpResponse('reset password ',token)
       
      