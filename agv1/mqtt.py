import paho.mqtt.client as mqtt
from django.conf import settings

def subcribe():
    client.subscribe("AGVData/#")
    client.subscribe("AGVError/#")


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print('Connect to mosquitto broker successfully')
        mqtt_client.subscribe('django/mqtt')
        subcribe()
    else:
        print('Bad connection. Return Code:', rc)


def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Subcribe successfully with mid: {str(mid)} and granted_qos: {str(granted_qos)} ')
 

client = mqtt.Client()
client.on_connect = on_connect
client.on_subcribe = on_subscribe
client.connect(
        host=settings.MQTT_SERVER,
        port=settings.MQTT_PORT,
        keepalive=settings.MQTT_KEEPALIVE
    )