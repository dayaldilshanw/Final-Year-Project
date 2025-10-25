import paho.mqtt.client as mqtt

brokerAddress = "df3104c9978f4e3c97934a7f0ac9749f.s1.eu.hivemq.cloud"
userName = "wildfire"
passWord = "WILDfire1"

topic = "Sensor/DHT/Temperature"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
       print("Connected successfully")
    else:
       print("Connect returned result code: " + str(rc))
def on_message(client, userdata, msg):
    print("Received message: " + msg.topic + " -> " + msg.payload.decode("utf-8"))

# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set(userName, passWord)
client.connect(brokerAddress, 8883)

client.subscribe(topic)

client.loop_forever()