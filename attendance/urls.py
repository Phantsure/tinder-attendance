from django.urls import path, include
from .api import AttendanceListAPI, AttendanceUpdateAPI

urlpatterns = [
    path("api/attendance/list", AttendanceListAPI.as_view()),
    path("api/attendance/update", AttendanceUpdateAPI.as_view()),
]
