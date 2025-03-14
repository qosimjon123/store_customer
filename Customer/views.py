from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminUser
from rest_framework.permissions import IsAuthenticated

from .models import Client, ClientAddress
from .serializers import ClientSerializer, ClientAddressSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'user_id'
    # permission_classes = (IsAuthenticated, IsAdminUser )


class ClientAddressViewSet(viewsets.ModelViewSet):
    queryset = ClientAddress.objects.select_related('client').all()
    serializer_class = ClientAddressSerializer



