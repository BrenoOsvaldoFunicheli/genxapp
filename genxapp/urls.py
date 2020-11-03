"""genxapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

# rest_framework imports
from rest_framework import routers

# my imports
from .views import index

from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

#   jwt imports
from rest_framework_simplejwt import views as jwt_views
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


# swager
from rest_framework_swagger.views import get_swagger_view

app_name = "genxapp"

urlpatterns = [
    # admin roots
    path('admin/', admin.site.urls),

    # my resources
    path('', index, name="index"),
    path('', include('users.urls')),
    path('', include('mirna_db.urls')),

    # authentication
    path('api/v1/login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/login/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    # path('api/v1/login/', obtain_jwt_token,name='token_obtain_pair'),
    # path('api/v1/login/refresh/', refresh_jwt_token,name='token_refresh'),
]
