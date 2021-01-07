from rest_framework import serializers
from .models import Attendance


class AttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class AttendanceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

    def create(self, validated_data):
        attendance, created = Attendance.objects.update_or_create(
            name=validated_data.get("name", None),
            branch=validated_data.get("branch", None),
            subject=validated_data.get("subject", None),
            attendedClasses=validated_data.get("attendedClasses", 0),
            totalClasses=validated_data.get("totalClasses", 0),
        )
        return attendance