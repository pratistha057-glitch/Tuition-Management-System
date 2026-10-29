from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.api.serializers import UserProfileSerializer
from apps.accounts.models import UserProfile
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from apps.accounts.api.permissions import IsAdmin


class UserProfileView(GenericAPIView):
    queryset = UserProfile
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdmin]

    def get(self, request, *args, **kwargs):
        data = UserProfile.objects.all()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User Profile Created Successfully"
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



class UpdateUserProfileView(GenericAPIView):
    queryset = UserProfile
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdmin]

    def get(self, request, id):
        data = get_object_or_404(UserProfile, id=id)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self, request, id):
        data = get_object_or_404(UserProfile, id=id)
        serializer = self.get_serializer(data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User Profile Updated Successfully"
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, id):
        data = get_object_or_404(UserProfile, id=id)
        data.delete()

        return Response(
            {
                "message": "User Profile Deleted Successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )




class MyProfileView(GenericAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = get_object_or_404(
            UserProfile,
            user=request.user
        )
        serializer = self.get_serializer(data)
        return Response(serializer.data)