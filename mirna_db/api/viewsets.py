


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
    model = Tarbase
    serializer_class = TarbaseSerializer
    #permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        queryset = Tarbase.objects.all()

        mirna = self.request.query_params.get('mirna')
        gene= self.request.query_params.get('gene')

        if mirna:     
            queryset = queryset.filter(mirna__icontains=mirna)   

        if gene:
            queryset = queryset.filter(geneName__icontains=gene)   
            

        return queryset
    
class miRDBViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    model = miRDB
    serializer_class = miRDBSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = miRDB.objects.all()

        mirna = self.request.query_params.get('mirna')
        gene= self.request.query_params.get('gene')

        if mirna:     
            queryset = queryset.filter(mirna__icontains=mirna)   

        if gene:
            queryset = queryset.filter(geneName__icontains=gene)   
            

        return queryset

class TGScanViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    model=TGScan
    # queryset = TGScan.objects.all()
    serializer_class = TGScanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = TGScan.objects.all()

        mirna = self.request.query_params.get('mirna')
        gene= self.request.query_params.get('gene')

        if mirna:     
            queryset = queryset.filter(mirna__icontains=mirna)   

        if gene:
            queryset = queryset.filter(gene_name__icontains=gene)   
            

        return queryset