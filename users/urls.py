from django.urls import path, include
from django.conf.urls import url

# rest_framework imports
from rest_framework import routers

#   my serializers class
from users.api.viewsets import UserViewSet,UseraAuthViewSet

# it's defining the routers to api access
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')

router.register(r'users_auth', UseraAuthViewSet,'users_auth')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(router.urls)),
  
]
