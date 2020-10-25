#   import models of the auth django's package
from django.contrib.auth.models import User, Group

#   rest frameworks's response
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import  action
from rest_framework.response import Response
from rest_framework.views import APIView


#   my serializers classes
from users.api.serializers import UserSerializer


unavailable_resource = Response(
    {"result": "this resource isn't available"}, status=status.HTTP_404_NOT_FOUND)


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

        user, created = User.objects.get_or_create(
            username=data['username'], email=data['email'], first_name=data['first_name'], last_name=data['last_name'])

        if created:
            user.set_password(data['password'])
            user.save()
            return Response({"results": "User Created"}, status.HTTP_201_CREATED)
        else:
            return Response({"results": "Error There is error on request"}, status.HTTP_400_BAD_REQUEST)

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


class UserAuth(APIView):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    delete:
        Remove an existing user.

    update:
        Update a user.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
 
    def get(self, request):
        try:
            user = request.user
            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception:
            return Response({"results": "Error There is error on request"}, status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            user = request.user
            user.delete()
            return Response({"results":"Use deleted"}, status.HTTP_200_OK)
        except Exception:
            return Response({"results": "Error There is error on request"}, status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        data = request.data

        user = request.user
        
        user.last_name=data['last_name']
        user.first_name=data['last_name']
        user.username=data['username']
        user.set_password(data['password'])
        user.email=data['email']

        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
        
