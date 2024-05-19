from django.shortcuts import render
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

@authentication_classes([TokenAuthentication, BasicAuthentication])
# Create your views here.
def login(request):
    pass

def signup(request):
    pass

def userinfo(request):
    pass