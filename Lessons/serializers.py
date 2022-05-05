from rest_framework import serializers
from .models import Category, Course,VideoLessons ,Direction, User 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class VideoLessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoLessons
        fields = '__all__'
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Direction
        fields = '__all__'
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
