from rest_framework import serializers
from Customer.models import Client, ClientAddress


class ClientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = '__all__'



class ClientSerializer(serializers.ModelSerializer):
    addresses = ClientAddressSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = '__all__'



