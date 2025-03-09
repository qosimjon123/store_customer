from rest_framework import viewsets
from .models import Client, ClientAddress
from Customer.serializers import ClientSerializer, ClientAddressSerializer


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'user_id'


class ClientAddressViewSet(viewsets.ModelViewSet):
    queryset = ClientAddress.objects.select_related('client').all()
    serializer_class = ClientAddressSerializer



