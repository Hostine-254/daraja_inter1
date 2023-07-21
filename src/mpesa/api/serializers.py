from rest_framework import serializers

from mpesa.models import LNMOnline,netview

class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNMOnline
        fields = 'id'

class NetPostSerializer(serializers.ModelSerializer):
        class Meta: 
             model = netview
             fields ="__all__"