from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import *

from django.contrib.auth.models import User
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate_Model
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    certificate = CertificateSerializer(many=True, read_only=True)
    class Meta:
        model = Teacher_Model
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Models
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_Model
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user