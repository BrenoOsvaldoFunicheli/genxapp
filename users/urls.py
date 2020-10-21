from django.urls import path, include
from django.conf.urls import url

# rest_framework imports
from rest_framework import routers

#   my serializers class
from users.api.viewsets import UserViewSet, UserAuth

# it's defining the routers to api access
router = routers.DefaultRouter()
router.register(r'user', UserViewSet, 'user')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/user_auth/', UserAuth.as_view())
]
