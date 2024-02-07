from django.urls import path
from .views import *

urlpatterns = [
    path('ordinary-courses/', ListCourses.as_view()),
    path('ordinary-teachers/',ListTeachers.as_view()),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('subjects/', SubjectListView.as_view(), name='subjects'),
    path("subject-create/", SubjectCreateView.as_view()),
    path('subjects/<pk>/', SubjectDetailView.as_view(), name='subjects'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path("course-create/", CourseCreateView.as_view()),
    path('courses/<pk>/', CourseDetailView.as_view()),
    path('certificates/',CertificateListView.as_view(), name='courses'),
    path("certificate-create/", CertificateCreateView.as_view()),
    path('certificates/<pk>/', CertificateDetailView.as_view()),
    path('teachers/', TeacherListView.as_view(), name='courses'),
    path("teacher-create/", TeacherCreateView.as_view()),
    path('teachers/<pk>/', TeacherDetailView.as_view()),
]