import paho.mqtt.client as mqtt

client = mqtt.Client("pasta_publisher")
client.connect("localhost", 1883)
client.publish("storage/fresh/A", "Storage level at 80%")
client.disconnect()
