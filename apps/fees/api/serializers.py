from rest_framework import serializers
from apps.fees.models import FeesModel

class FeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeesModel
        fields = '__all__'