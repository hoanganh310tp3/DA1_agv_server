# from .models import Agv_data
 
# from .serializers import AgvDataserializer

# from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
# from djangochannelsrestframework.mixins import ListModelMixin
# from djangochannelsrestframework.observer import model_observer
# from djangochannelsrestframework import permissions

# class AgvDataConsumer(GenericAsyncAPIConsumer):
    
#     queryset = Agv_data.objects.all()
#     permissions_class = (permissions.AllowAny)
    
#     async def connect(self, **kwargs):
#         await self.model_change.subcribe()
#         await super().connect()
    
#     @model_observer(Agv_data)
#     async def model_change(self, message, observer=None, **kwargs):
#         await self.send_json(message)
        
#     @model_change.serialize
#     def model_serialize(self, instance, action, **kwargs):
#       return dict(data=AgvDataserializer(instance=instance).data, action=action.value)
  
  
  