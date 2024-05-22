from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import JsonResponse

from .serializers import ReviewSerializer
from .models import Movie, Review

import json

# Create your views here.
@api_view(['GET', 'POST'])
def review_list(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(pk=movie_pk)
        reviews = Review.objects.all(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # movie = Movie.objects.get(pk=movie_pk)
        # serializer = ReviewSerializer(data=request.data)
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save(movie=movie)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        data = json.loads(request.body)
        form_data = Review(
            movie=data.get('movie'),
            user=data.get('user'),
            rating=data.get('rating'),
            content=data.get('content'),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )
        form_data.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def review_detail(request, review_pk, movie_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
class ImagePathView(APIView):
    def get(self, request):
        image_data = Movie.objects.values('image_path')
        return Response(list(image_data))