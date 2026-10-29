from rest_framework import serializers
from apps.attendance.models import AttendanceModel

class AttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendanceModel
        fields = '__all__'