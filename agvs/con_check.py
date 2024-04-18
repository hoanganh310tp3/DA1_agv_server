# from django.utils import timezone
# import datetime
# import time

# from .models import Agv_identify, Agv_data

# def is_agv_active(ID):
#     AgvIsActive = Agv_identify.objects.filter(verhicle_id = ID, is_active = True, is_connected = True).exists()
#     return AgvIsActive

# def list_of_ActiveAgv():
#     ListOfActive =[]
#     AgvisActive = Agv_identify.objects.all().filter(is_active = True, is_connected = True).order_by('verhicle_id')
#     for eachQuery in AgvisActive:
#         ListOfActive.append([eachQuery.verhicle_id])
#     return   ListOfActive

# def check_connect():
#     now = time.mktime(datetime.datetime.now().timetuple)
    
#     ListOfActive = list_of_ActiveAgv()
#     for eachCar in ListOfActive:
#         query = Agv_data.objects.all().filter(car_id = eachCar[0]).last()
#         dataTime = time.mktime(query.time_stamp.timetuple())
#         if (now - dataTime) > 300:
#             Agv_data.objects.filter(verhicle_id = eachCar[0]).update(is_connected =False)
        