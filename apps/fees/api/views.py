from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from apps.fees.models import FeesModel
from apps.fees.api.serializers import FeeSerializer
from apps.accounts.api.permissions import IsAdmin, IsAdminOrTeacher

class FeeView(GenericAPIView):
    queryset = FeesModel
    serializer_class = FeeSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAdminOrTeacher()]

        return [IsAdmin()]

    def get(self, request, *args, **kwargs):
        data = FeesModel.objects.all()
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Fee has been created successfully"
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UpdateFeeView(GenericAPIView):
    queryset = FeesModel
    serializer_class = FeeSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAdminOrTeacher()]

        return [IsAdmin()]

    def get(self, request, id):
        data = get_object_or_404(FeesModel, id=id)
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def put(self, request, id):
        data = get_object_or_404(FeesModel, id=id)
        serializer = self.get_serializer(data, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Fee updated successfully"
            })

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        data = get_object_or_404(FeesModel, id=id)
        data.delete()

        return Response(
            {"message": "Fee deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
