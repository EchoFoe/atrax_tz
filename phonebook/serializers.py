from rest_framework import serializers
from .models import PhoneNumberRange


class PhoneNumberRangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumberRange
        fields = ['region_code', 'operator', 'region']