from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.courses.models import Course, Subject
from apps.courses.api.serializers import CourseSerializer, SubjectSerializer
from django.shortcuts import get_object_or_404


class CourseView(GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Course Created Successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class UpdateCourseView(GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course)

        return Response(serializer.data)

    def put(self, request, id):
        course = get_object_or_404(Course, id=id)
        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Course Updated Successfully",
                    "data": serializer.data
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        course = get_object_or_404(Course, id=id)
        course.delete()

        return Response(
            {"message": "Course Deleted Successfully"},
            status=status.HTTP_204_NO_CONTENT
        )




class SubjectView(GenericAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Subject Created Successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )




class UpdateSubjectView(GenericAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def get(self, request, id):
        subject = get_object_or_404(Subject, id=id)
        serializer = SubjectSerializer(subject)

        return Response(serializer.data)

    def put(self, request, id):
        subject = get_object_or_404(Subject, id=id)
        serializer = SubjectSerializer(subject, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message": "Subject Updated Successfully",
                    "data": serializer.data
                }
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        subject = get_object_or_404(Subject, id=id)
        subject.delete()

        return Response(
            {"message": "Subject Deleted Successfully"},
            status=status.HTTP_204_NO_CONTENT
        )