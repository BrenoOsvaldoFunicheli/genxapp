# rest framework
from rest_framework import serializers

# my classes
from mirna_db.models import *


class TarbaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarbase
        fields = [
            'mirna',
            'geneName',
            'species',
            'method',
            'direct_indirect',
            'up_down'
        ]


class TGScanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TGScan
        fields = [  'mirna','gene_id','gene_name','score','specie']


class miRDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = miRDB
        fields = [
            'mirna',
            'geneName',
            'score',
            'species'
        ]
