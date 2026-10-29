from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.attendance.models import AttendanceModel
from apps.attendance.api.serializers import AttendanceSerializer


class AttendanceView(GenericAPIView):
    queryset = AttendanceModel
    serializer_class = AttendanceSerializer

    def get(self, request, *args, **kwargs):
        data = AttendanceModel.objects.all()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Attendance has been created successfully"
            }, status=status.HTTP_201_CREATED)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UpdateAttendanceView(GenericAPIView):
    queryset = AttendanceModel
    serializer_class = AttendanceSerializer

    def get(self, request, id):
        data = get_object_or_404(AttendanceModel, id=id)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self, request, id):
        data = get_object_or_404(AttendanceModel, id=id)
        serializer = self.get_serializer(data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Attendance updated successfully"
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        data = get_object_or_404(AttendanceModel, id=id)
        data.delete()

        return Response(
            {"message": "Attendance deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )