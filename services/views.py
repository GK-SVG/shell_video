from django.shortcuts import render,HttpResponse
from django.contrib.auth.tokens import default_token_generator
from .models import StoreMailVarificatioLink
# Create your views here.
def send_verification_link(user):
    token=default_token_generator.make_token(user)
    user_data=StoreMailVarificatioLink(token=token,email=user.email,uid=user.id)
    user_data.save()
    return token

def validate_mail_id(request):
    token=request.GET['token']
    mail=request.GET['mail']
    uid=request.GET['uid']
    print('tken===',token,'mail====',mail,'uid===',uid)
    try:
        validate=StoreMailVarificatioLink.objects.get(token=token,email=mail,uid=uid)
        return HttpResponse('your mail validated ' + token +' ' + mail  + ' '+ str(uid))
    except:
        return HttpResponse('mail validation failed')