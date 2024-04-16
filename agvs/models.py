from django.db import models

class Agv(models.Model):
    verhicle_id = models.AutoField(primary_key=True )  
    verhicle_model = models.IntegerField(default=" ")
    guidance = models.CharField(max_length=100, default=" ")  
    is_active = models.BooleanField(default=False)  
    is_connected = models.BooleanField(default=False)

    def __str__(self):
        return self.verhicle_id
