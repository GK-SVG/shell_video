from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.tokens import default_token_generator
from .models import StoreMailVarificatioLink,ResetPasswordLink
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
# from django.template.loader import get_template 
# from django.template import Context 
# from django.contrib.auth import get_user_model
from user.models import Users 
# Create your views here.
def send_verification_link(user):
    token=default_token_generator.make_token(user)
    StoreMailVarificatioLink(token=token,email=user.email,uid=user.id).save()
    verification_link='http://127.0.0.1:8000/services/validate_mail/?token={token}&email={email}&uid={uid}'.format(token=token,email=user.email,uid=user.id)
    subject,from_email,to='Validate Email','gk32239@gmail.com',user.email
    html_content='Please click on below link to confirm your email \n\n ' + verification_link
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content,'text/html')
    msg.send()  
    return token

def validate_mail_id(request):
    token=request.GET['token']
    email=request.GET['email']
    uid=request.GET['uid']
    try:
        validate=StoreMailVarificatioLink.objects.filter(token=token,email=email,uid=uid)
        if not validate:
            return HttpResponse('mail validation failed')
        user=Users.objects.get(id=uid)
        user.mail_validate=1
        user.save()
        return HttpResponse('your mail validated Succsefully ' + token +' ' + email  + ' '+ str(uid))
    except:
        return HttpResponse('mail validation failed')

def reset_password_mail_validation(user):
    print('login====',user.last_login)
    token=default_token_generator.make_token(user)
    print(token)
    ResetPasswordLink(token=token,email=user.email,uid=user.id).save()
    verification_link='http://127.0.0.1:8000/services/validate_email_reset_password/?token={token}&email={email}&uid={uid}'.format(token=token,email=user.email,uid=user.id)
    subject,from_email,to='Reset Password','gk32239@gmail.com',user.email
    html_content='Please click on below link to reset your password\n\n ' + verification_link
    msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
    return token  
    

def validate_email_reset_password(request):
    if request.method=='GET':
        token=request.GET['token']
        email=request.GET['email']
        uid=request.GET['uid']
        print('email==',email,'uid==',uid)
        return render(request,'myapp/reset_password.html',{'uid':uid})

def reset_password(request,uid):
    if request.method=='POST':
        user=Users.objects.get(id=uid)
        pass1=request.POST['pass1']  
        pass2=request.POST['pass2']
        if pass1 != pass2 :
            messages.error(request,'Passwords do not match')
            return HttpResponse('Passwords do not match')
        user.password=pass1
        user.save()
        return redirect('/')
        