from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import ListModelMixin
from djangochannelsrestframework.observer import model_observer

from .models import Post
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