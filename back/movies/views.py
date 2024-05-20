from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie

# Create your views here.
def index(request):
    pass

def detail(request):
    pass

def rate(request):
    pass

class ImagePathView(APIView):
    def get(self, request):
        image_data = Movie.objects.values('image_path')
        return Response(list(image_data))