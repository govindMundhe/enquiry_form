from .models import Enquiry
from rest_framework import serializers


class EnquirySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'