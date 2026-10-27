from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.students.api.serializers import StudentSerializer
from apps.students.models import Student
from django.shortcuts import get_object_or_404



class StudentView(GenericAPIView):
    queryset = Student
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        data = Student.objects.all()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Student Created Successfully"
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )




class UpdateStudentView(GenericAPIView):
    queryset = Student
    serializer_class = StudentSerializer

    def get(self, request, id):
        data = get_object_or_404(Student, id=id)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self, request, id):
        data = get_object_or_404(Student, id=id)
        serializer = self.get_serializer(data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Student Updated Successfully"
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id):
        data = get_object_or_404(Student, id=id)
        data.delete()

        return Response(
            {
                "message": "Student Deleted Successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )