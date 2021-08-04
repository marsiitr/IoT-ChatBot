from random import choice
import paho.mqtt.client as mqtt
import time
#  function


def connect_msg():
    print('Connected to Broker')


randlist = [i for i in range(0, 100)]
client = mqtt.Client(client_id='Humidity Sensor')


client.connect("127.0.0.1", 1883)
client.on_connect = connect_msg

while True:
    randData = choice(randlist)
    hum = 100 + 0.01*randData
    client.publish("house/hum", hum)
    print("Just published " + str(hum))
    time.sleep(5)
