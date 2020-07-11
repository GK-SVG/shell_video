from django.shortcuts import render,HttpResponse
from django.contrib.auth.tokens import default_token_generator
from .models import StoreMailVarificatioLink
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
    print('tken===',token,'email====',email,'uid===',uid)
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