from rest_framework import serializers
from classes.models import Classroom
from rest_framework.generics import CreateAPIView
from .serializers import CreateSerializer

class ClassroomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'teacher']


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name','subject', 'year']