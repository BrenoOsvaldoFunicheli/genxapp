from django.urls import path, include
from django.conf.urls import url

# rest_framework imports
from rest_framework import routers

#   my serializers class
from mirna_db.api.viewsets import *

# it's defining the routers to api access
m_router = routers.DefaultRouter()
m_router.register(r'tgscan', TGScanViewSet, 'tgscan')
m_router.register(r'mirdb', miRDBViewSet, 'mirdb')
m_router.register(r'tarbase', TarbaseViewSet, 'tarbase')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(m_router.urls)),
]
