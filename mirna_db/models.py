from django.db import models

# Create your models here.


class Tarbase(models.Model):

    mirna = models.CharField(max_length=300)
    geneName = models.CharField(max_length=300)
    species = models.CharField(max_length=300)
    method = models.CharField(max_length=300)
    direct_indirect = models.CharField(max_length=300)
    up_down = models.CharField(max_length=300)

    def __str__(self):
        return " miRNA " + self.mirna + " of " + self.geneName + " belong to " + self.species


class miRDB(models.Model):

    mirna = models.CharField(max_length=300)
    geneName = models.CharField(max_length=300)
    score = models.FloatField()
    species = models.CharField(max_length=300)

    def __str__(self):
        return ''

class TGScan(models.Model):

    mirna = models.CharField(max_length=500)
    gene_id = models.CharField(null=True, blank=True, max_length=500)
    gene_name = models.CharField(null=True, blank=True,max_length=500)
    score = models.FloatField(null=True, blank=True)
    specie = models.CharField(null=True, blank=True, max_length=500)
