from django.http import Http404
from rest_framework.views import APIView
from .serializers import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, get_object_or_404


class ListCourses(APIView):
    def get(self, request, format=None):
        course = Course_Models.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)



class ListTeachers(APIView):
    def get(self, request, format=None):
        teacher = Teacher_Model.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,
                                                'username': username,
                                                'password': password}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




#*************For Admin Page ***********
class SubjectListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        subject = Subject_Model.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        return Response(serializer.data)


class SubjectCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetailView(APIView):
    """
    Retrieve, update or delete a transformer instance
    """
    def get_object(self, pk):
        try:
            return Subject_Model.objects.get(pk=pk)
        except Subject_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
            subject = self.get_object(pk)
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)

    def put(self, request, pk, format=None):
            subject = self.get_object(pk)
            serializer = SubjectSerializer(subject, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
            subject = self.get_object(pk)
            serializer = SubjectSerializer(subject,
                                               data=request.data,
                                               partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
            subject = self.get_object(pk)
            subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class CourseListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        course = Course_Models.objects.all()
        serializer = SubjectSerializer(course, many=True)
        return Response(serializer.data)

class CourseCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Course_Models.objects.get(pk=pk)
        except Course_Models.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CourseSerializer(course,
                                       data=request.data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class CertificateListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        certificate = Certificate_Model.objects.all()
        serializer = CertificateSerializer(certificate, many=True)
        return Response(serializer.data)

class CertificateCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificateDetailView(APIView):

    def get_object(self, pk):
        try:
            return Certificate_Model.objects.get(pk=pk)
        except Certificate_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = CertificateSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        certificate = self.get_object(pk)
        serializer = CertificateSerializer(certificate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        certificate = self.get_object(pk)
        serializer = CertificateSerializer(certificate,
                                       data=request.data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        certificate = self.get_object(pk)
        certificate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        teacher = Teacher_Model.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)

class TeacherCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailView(APIView):

    def get_object(self, pk):
        try:
            return Teacher_Model.objects.get(pk=pk)
        except Teacher_Model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher,
                                           data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        certificate = self.get_object(pk)
        certificate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)