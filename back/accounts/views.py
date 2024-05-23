from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import UserInfo
from .serializers import UserInfoSerializer

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
            isSpecial=data.get('isSpecial', None),
            gender=data.get('gender', ''),
            era= data.get('era', ''),
            favorite_genre = data.get('favorite_genre', []),
            viewing_environment=data.get('viewing_environment', ''),
            birthday=data.get('birthday', None)
        )
        form_data.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)


def get_userinfo_list(request):
    userinfo = get_list_or_404(UserInfo)
    data = [
        {
            'isSpecial': info.isSpecial,
            'gender': info.gender,
            'era': info.era,
            'favorite_genre' : info.favorite_genre,
            'viewing_environment' : info.viewing_environment,
            'birthday': info.birthday
        }
        for info in userinfo  # List Comprehension
    ]
    return JsonResponse(data, safe=False)