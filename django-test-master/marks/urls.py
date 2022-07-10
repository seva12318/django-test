#from xml.etree.ElementInclude import include
from django.db import router
from marks.api import SchoolViewSet, StudentViewSet
from marks.views import ChoicesView, LessonView, OneLessonView, OneSchoolView, OneStudentView, OneSubjectView, OneTeacherView, SchoolView, StudentView, SubjectView, TeacherView
from django.urls import include, path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')


urlpatterns = [
    path("students/", StudentView.as_view()),
    path("students/<int:id>/", OneStudentView.as_view()),
    path("school/", SchoolView.as_view()),
    path("school/<int:id>/", OneSchoolView.as_view()),
    path("teachers/", TeacherView.as_view()),
    path("teachers/<int:id>/", OneTeacherView.as_view()),
    path("subjects/", SubjectView.as_view()),
    path("subjects/<int:id>/", OneSubjectView.as_view()),
    path("lessons/", LessonView.as_view()),
    path("lessons/<int:id>/", OneLessonView.as_view()),
    path("choices/", ChoicesView.as_view())
]
