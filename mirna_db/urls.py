from django.urls import path, include
from django.conf.urls import url

# rest_framework imports
from rest_framework import routers

#   my serializers class
from mirna_db.api.viewsets import *

# it's defining the routers to api access
router = routers.DefaultRouter()
router.register(r'tgscan', TGScan, 'tgscan')
router.register(r'mirdb', miRDB, 'mirdb')
router.register(r'tarbase', Tarbase, 'tarbase')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(router.urls)),
  
]
