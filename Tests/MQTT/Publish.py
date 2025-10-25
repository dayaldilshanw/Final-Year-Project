import paho.mqtt.client as mqtt
import random
import time

brokerAddress = "df3104c9978f4e3c97934a7f0ac9749f.s1.eu.hivemq.cloud"
userName = "wildfire"
passWord = "WILDfire1"

topic = "Sensor/DHT/Temperature"
topic1 = "Sensor/DHT/Humidity"

min = 27
max = 30
min1 = 50
max1 = 52
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully")
    else:
        print("Connect returned result code: " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(userName, passWord)
client.connect(brokerAddress, 8883)

wait = 5
while True:
   data = random.randint(min, max)
   data1 = random.randint(min1, max1)
   print(data,data1)
   #print(data1)
   client.publish(topic, data)
   client.publish(topic1, data1)
   time.sleep(wait)