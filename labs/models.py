from django.db import models

# Create your models here.

class UrlLab(models.Model):
    url = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    

LAB_TYPES = (
    ('rdp','RDP'),
    ('ssh','SSH')
)
class RdpLab(models.Model):
    dns_name = models.CharField(max_length=250)
    vm_username = models.CharField(max_length=250)
    vm_password = models.CharField(max_length=50)
    labtype = models.CharField(max_length=6, choices=LAB_TYPES, default='rdp')
    rdp_file = models.FileField(upload_to='labimage/')