from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

from .models import Agv_data, Agv_identify
from .serializers import AgvIdentifySerializer, AgvDataserializer

# For Agv_identify restfulapi
@api_view(['GET', 'POST'])
def agvs_list(request):
    if request.method == 'GET':
        data = Agv_identify.objects.all()

        serializer = AgvIdentifySerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgvIdentifySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def agvs_detail(request, pk):
    try:
        agv = Agv_identify.objects.get(pk=pk)
    except Agv_identify.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer =  AgvIdentifySerializer(agv, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        agv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
# For Agv_data websocket 

class AgvDataViewSet(viewsets.ModelViewSet):
    
    serializer_class = AgvDataserializer
    queryset = Agv_data.objects.all()
    
def index(request):
    return render(request, "agvs/index.html")