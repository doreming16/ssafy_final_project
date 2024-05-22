from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404, get_list_or_404

from .serializers import ReviewSerializer
from .models import Movie, Review

# Create your views here.
@api_view(['GET', 'POST'])
def review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        reviews = get_list_or_404(Review, movie_id=movie_pk)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ImagePathView(APIView):
    def get(self, request):
        image_data = Movie.objects.values('image_path')
        return Response(list(image_data))