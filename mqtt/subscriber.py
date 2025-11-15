import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client("pasta_subscriber")
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("storage/fresh/A")

client.loop_forever()
