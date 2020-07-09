from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Users



def login(request):
    return HttpResponse('this is login')

def signup(request):
    if request.method=='POST':
        username=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        print(username,pass1,email)
        # checkpoints 
        #username length checker
        if len(username) > 12 :
            messages.error(request,'Username must have maximum 12 Charcters')
            return redirect('/')

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
            myuser=Users.objects.get(username=username)
            messages.error(request,'The username you entered has already been taken. Please try another username.')
            return redirect('/')
        except:
            myuser = Users(username=username,email=email,password=pass1,phone=phone)
            myuser.save()
            messages.success(request,'Your account created succesfully')
            return redirect('/')      
    else:
        return redirect('/')

def logout(request):
    return HttpResponse('this is logout')
