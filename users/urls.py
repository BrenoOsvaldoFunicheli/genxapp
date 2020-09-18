from django.urls import path, include
from django.conf.urls import url

# rest_framework imports
from rest_framework import routers

#   my serializers class
from users.api.viewsets import UserViewSet,UseraAuthViewSet
#   jwt imports
from rest_framework_simplejwt import views as jwt_views



# schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])


# it's defining the routers to api access

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')

router.register(r'users_auth', UseraAuthViewSet,'users_auth')

print(router.urls)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/login/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
