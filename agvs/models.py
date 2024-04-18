from django.contrib.auth.models import User
from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish"),
    (2, "Archive"),
)

class Agv_identify(models.Model):
    verhicle_id = models.AutoField(primary_key=True )  
    verhicle_model = models.IntegerField(default=" ")
    guidance = models.CharField(max_length=100, default=" ")  
    is_active = models.BooleanField(default=False)  
    is_connected = models.BooleanField(default=False)

    def __str__(self):
        return self.verhicle_id

class Agv_data(models.Model):
    Agv_id = models.ForeignKey(Agv_identify, on_delete=models.CASCADE, related_name='Agv_data')
    Agv_speed = models.FloatField()
    trip_distance = models.FloatField()
    Agv_battery = models.FloatField()
    Agv_distance = models.FloatField()
    previous_node = models.IntegerField()
    next_node = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Agv_id


    
