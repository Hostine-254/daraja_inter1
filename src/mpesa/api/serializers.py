from rest_framework import serializers

from mpesa.models import LNMOnline,netview,C2BPayments

class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = 'id'

class NetPostSerializer(serializers.ModelSerializer):
        class Meta: 
             model = netview
             fields ="__all__"

class C2BPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = C2BPayments
        fields = 'id'