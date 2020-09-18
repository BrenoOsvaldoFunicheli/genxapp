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


from rest_framework.schemas import get_schema_view

from rest_framework.renderers import CoreJSONRenderer
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


# swager
from rest_framework_swagger.views import get_swagger_view

app_name = "genxapp"

schema_view = get_schema_view(
    title='A Different API',
    renderer_classes=[CoreJSONRenderer]
)
# schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url('doc/', schema_view, name="docs"),
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('', include('users.urls')),

]
