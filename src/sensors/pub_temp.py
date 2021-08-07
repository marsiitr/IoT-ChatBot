from random import choice
import paho.mqtt.client as mqtt
import time
data = 25
randlist = [i for i in range(0, 100)]


def on_connect(client, userdata, flags, rc):
    client.subscribe("control/temp")


def on_message(client, userdata, msg):
    global data
    data = msg.payload.decode("utf-8")
    print("Message is : "+str(msg.payload.decode("utf-8")))


mqttc = mqtt.Client("Temperature Sensor")
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.connect("127.0.0.1", 1883, 60)
mqttc.loop_start()
while True:
    randData = choice(randlist)
    temp = float(data) + 0.01*randData
    mqttc.publish("house/temp", str(temp))
    print("publish message " + str(temp))
    time.sleep(2)
