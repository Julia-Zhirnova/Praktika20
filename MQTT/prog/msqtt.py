import paho.mqtt.client as mqtt
from .publisher import PublisherClass, Var

# https://pypi.org/project/paho-mqtt/
MQTT_ADDR = 'mosquitto'
MQTT_PORT = 1883


def listener_func(pub: PublisherClass, name: str, sub: str):

    def on_connect(client, userdata, flags, rc):
        client.subscribe(sub + '/' + name)

    def on_message(client, userdata, msg):
        a = Var(float(msg.payload.decode()), 0, False)
        pub.add_field(name, a)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_ADDR, MQTT_PORT)
    client.loop_forever()
