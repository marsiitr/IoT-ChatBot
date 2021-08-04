from random import choice
import paho.mqtt.client as mqtt
import time

status = ['off','on']

def on_connect(client, userdata, flags, rc):
    client.subscribe("control/light")


def on_message(client, userdata, msg):
    global data
    data = msg.payload.decode("utf-8")
    print("Message is : "+str(msg.payload.decode("utf-8")))


mqttc = mqtt.Client("Light Sensor")
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("127.0.0.1", 1883)
mqttc.loop_start()
while True:

    light_status = choice(status)
    mqttc.publish("house/light", str(light_status))
    print("publish message " + str(light_status))
    time.sleep(15)
