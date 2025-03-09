
from rest_framework_nested import routers
from Customer.views import ClientViewSet, ClientAddressViewSet

router = routers.SimpleRouter()
router.register(r'', ClientViewSet, basename='client')

address_router = routers.NestedSimpleRouter(router, r'', lookup='user')
address_router.register(r'address', ClientAddressViewSet, basename='client-address')


urlpatterns = router.urls + address_router.urls