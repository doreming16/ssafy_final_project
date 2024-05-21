from django.shortcuts import render
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserInfo, User
# User 갖고와서 form_data에 보내기 ?

from django.contrib.auth import get_user_model
# User 모델 갖고오는거

# @authentication_classes([TokenAuthentication, BasicAuthentication])
# Create your views here.
def login(request):
    pass

def signup(request):
    pass

@csrf_exempt
def submit_form(request):
    # 지금 로그인된 유저
    user = request.user
    # user = get_user_model()
    if request.method == 'POST':
        data = json.loads(request.body)
        form_data = UserInfo(
            # user_id = user.pk,
            gender=data.get('gender', ''),
            era= data.get('era', ''),
            favorite_genre = data.get('favorite_genre', []),
            viewing_environment=data.get('viewing_environment', ''),
            birthday=data.get('birthday', None)
        )
        form_data.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)