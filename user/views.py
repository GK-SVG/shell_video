from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Users
from services.views import send_verification_link


   

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
                return HttpResponse('You are a validated user')
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
            messages.error(request,'The username you entered has already been taken. Please try another username.')
            return HttpResponse('The username you entered has already been taken. Please try another username')
        except:
            myuser = Users(user=username,email=email,password=pass1,phone=phone)
            myuser.save()
            token=send_verification_link(myuser)
            return HttpResponse('Account created successfully  Please check your mail to conform your email')      
    else:
        return redirect('')

def logout(request):
    return HttpResponse('this is logout')
