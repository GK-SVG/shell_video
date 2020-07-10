from django.shortcuts import render
from django.contrib.auth.tokens import default_token_generator
# Create your views here.
def send_verification_link(user):
    token=default_token_generator.make_token(user)
    return token