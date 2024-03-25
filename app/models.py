from django.db import models

# Create your models here.
class Cdr(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.CharField(max_length = 100)
    operator = models.CharField(max_length = 100)
    partya = models.IntegerField()
    partyb = models.IntegerField()
    call_duration = models.IntegerField()
    usage_type = models.CharField(max_length=20)
    cell_type = models.CharField(max_length=20)
    lac_id = models.IntegerField()
    cell_id = models.IntegerField()
    imei = models.IntegerField()
    imsi = models.IntegerField()
    Address = models.CharField(max_length = 100)
    partyb_original = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    