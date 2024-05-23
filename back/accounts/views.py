from django.shortcuts import render, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from .models import UserInfo
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# @authentication_classes([TokenAuthentication, BasicAuthentication])

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)