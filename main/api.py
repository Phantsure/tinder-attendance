from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response

from .serializers import EnrolledSerializer, SubjectSerializer
from .models import Enrolled, Subject


class EnrolledList(generics.ListAPIView):
    queryset = Enrolled.objects.all()
    serializer_class = EnrolledSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        enroll = serializer.save()
        print(2)
        return Response(
            {
                "Enrollment": EnrolledSerializer(
                    enroll, context=self.get_serializer_context()
                ).data,
            }
        )

    # def get_queryset(self):
    #     queryset = Enrolled.objects.all()

    #     return queryset


class SubjectList(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.save()
        return Response(
            {
                "subject": SubjectSerializer(
                    subject, context=self.get_serializer_context()
                ).data,
            }
        )