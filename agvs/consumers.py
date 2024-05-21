from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer

from .models import Agv_data, Agv_identify
from .serializers import AgvDataserializer


class AgvdataConsumer(ListModelMixin, GenericAsyncAPIConsumer):

    queryset = Agv_data.objects.all()
    serializer_class = AgvDataserializer
    permissions = (permissions.AllowAny,)

    async def connect(self, **kwargs):
        await self.model_change.subscribe()
        await super().connect()

    @model_observer(Agv_data)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serializer
    def model_serialize(self, instance, action, **kwargs):
        return dict(data=AgvDataserializer(instance=instance).data, action=action.value)

    async def receive_json(self, content, **kwargs):
        action = content.get('action')
        if action == 'create':
            agv_data = content.get('data', {})
            agv_identify_id = agv_data.get('agv_identify')

            try:
                agv_identify = await Agv_identify.objects.aget(verhicle_id=agv_identify_id)
                new_agv_data = Agv_data(
                    agv_identify=agv_identify,
                    Agv_speed=agv_data.get('Agv_speed'),
                    trip_distance=agv_data.get('trip_distance'),
                    Agv_battery=agv_data.get('Agv_battery'),
                    Agv_distance=agv_data.get('Agv_distance'),
                    previous_node=agv_data.get('previous_node'),
                    next_node=agv_data.get('next_node')
                )
                await new_agv_data.asave()
                await self.send_json({'status': 'success', 'data': 'Agv data created successfully'})
            except Agv_identify.DoesNotExist:
                await self.send_json({'status': 'error', 'errors': {'agv_identify': ['Invalid agv_identify ID']}})
        else:
            await self.send_json({'status': 'error', 'errors': {'action': ['Invalid action']}})
