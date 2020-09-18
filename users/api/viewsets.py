#   import models of the auth django's package
from django.contrib.auth.models import User, Group

#   rest frameworks's response
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

#   my serializers classes
from users.api.serializers import UserSerializer

unavailable_resource = Response({"result": "this resource isn't available"}, status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        data = request.data

        user, created = User.objects.get_or_create(username=data['username'], email=data['email'])

        if created:
            user.set_password(data['password'])
            user.save()
            
        return Response({"User Created":"User Created"})

    def list(self, request, pk=None):
        return unavailable_resource

    def retrieve(self, request, pk=None):
        return unavailable_resource

    def destroy(self, request, *args, **kwargs):
        return unavailable_resource

    def update(self, request, *args, **kwargs):
        return unavailable_resource

    def partial_update(self, request, *args, **kwargs):
        return unavailable_resource


class UseraAuthViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        return unavailable_resource
