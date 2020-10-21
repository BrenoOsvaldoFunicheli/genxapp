


#   rest frameworks's response
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

#   my classes
from mirna_db.api.serializers import *
from mirna_db.models import *

unavailable_resource = Response({"result": "this resource isn't available"}, status=status.HTTP_404_NOT_FOUND)


class TarbaseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = Tarbase.objects.all()
    serializer_class = TarbaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    
class miRDBViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = miRDB.objects.all()
    serializer_class = miRDBSerializer
    permission_classes = [permissions.IsAuthenticated]

class TGScanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = TGScan.objects.all()
    serializer_class = TGScanSerializer
    permission_classes = [permissions.IsAuthenticated]