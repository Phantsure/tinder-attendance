from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Enrolled, Subject


class EnrolledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrolled
        fields = "__all__"

    def create(self, validated_data):
        answer, created = Enrolled.objects.update_or_create(
            student=User.objects.get(username=validated_data["student"]),
            subject=Subject.objects.get(subject=validated_data.get("subject", None)),
            classesAttended=validated_data.get("classesAttended", 0),
        )
        return answer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

    def create(self, validated_data):
        subject, created = Subject.objects.update_or_create(
            subject=validated_data.get("subject", None),
            branch=validated_data.get("branch", None),
            totalClasses=validated_data.get("totalClasses", 0),
        )
        return subject