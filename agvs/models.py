from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator



class Agv_identify(models.Model):
    verhicle_id = models.AutoField(primary_key=True )  
    verhicle_model = models.IntegerField(default=0)
    guidance = models.CharField(max_length=100, default=" ")  
    is_active = models.BooleanField(default=False)  
    is_connected = models.BooleanField(default=False)

    def __str__(self):
        return f'Vehicle ID: {self.verhicle_id}'

class Agv_data(models.Model):
    data_id = models.BigAutoField(primary_key=True) 
    agv_identify = models.ForeignKey(Agv_identify, on_delete=models.CASCADE)
    Agv_speed = models.FloatField(validators=[MinValueValidator(0.0)])
    trip_distance = models.FloatField(validators=[MinValueValidator(0.0)])
    Agv_battery = models.FloatField(validators=[MinValueValidator(0.0)])
    Agv_distance = models.FloatField(validators=[MinValueValidator(0.0)])
    previous_node = models.IntegerField(validators=[MinValueValidator(0)])
    next_node = models.IntegerField(validators=[MinValueValidator(0)])
    

    def __str__(self):
        return f'Data ID: {self.data_id}'

    
