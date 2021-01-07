from django.urls import path, include
from rest_framework import routers
from .api import EnrolledList, SubjectList

# router = routers.DefaultRouter()
# router.register("api/enrolled", EnrolledList, "enrolled")

# urlpatterns = router.urls

urlpatterns = [
    path("api/enrolled", EnrolledList.as_view()),
    path("api/subjects", SubjectList.as_view()),
]