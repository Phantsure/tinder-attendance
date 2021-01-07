from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from .serializers import AttendanceUpdateSerializer, AttendanceListSerializer
from .models import Attendance


class AttendanceListAPI(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceListSerializer


class AttendanceUpdateAPI(generics.GenericAPIView):
    serializer_class = AttendanceUpdateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        attendance = serializer.save()
        return Response(
            {
                "attendance": AttendanceUpdateSerializer(
                    attendance, context=self.get_serializer_context()
                ).data,
            }
        )