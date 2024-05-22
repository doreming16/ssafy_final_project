from .models import Review, Movie
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'