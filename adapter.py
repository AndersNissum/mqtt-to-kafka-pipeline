import paho.mqtt.client as mqtt
from confluent_kafka import Producer

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print(f"MQTT → Kafka: {payload}")
    producer.produce('pasta', key='A', value=payload, callback=delivery_report)
    producer.flush()

mqtt_client = mqtt.Client("mqtt_to_kafka_adapter")
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883)
mqtt_client.subscribe("storage/fresh/A")

mqtt_client.loop_forever()
