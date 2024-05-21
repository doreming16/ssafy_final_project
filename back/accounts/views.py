from django.shortcuts import render
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserInfo

# @authentication_classes([TokenAuthentication, BasicAuthentication])
# Create your views here.
def login(request):
    pass

def signup(request):
    pass

@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form_data = UserInfo(
            gender=data.get('gender', ''),
            era= data.get('era', ''),
            favorite_gerne = data.get('favorite_gerne', []),
            viewing_environment=data.get('viewing_environment', ''),
            birthday=data.get('birthday', None)
        )
        form_data.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)