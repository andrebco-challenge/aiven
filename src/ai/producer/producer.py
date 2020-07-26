import json
import socket

from confluent_kafka import Producer

conf = {'bootstrap.servers': "localhost:9092", 'client.id': socket.gethostname()}

producer = Producer(conf)


def delivery_callback(err, msg):
    if err:
        print('%% Message failed delivery: %s\n' % err)
    else:
        print('%% Message delivered to %s [%d] @ %d\n' % (msg.topic(), msg.partition(), msg.offset()))


def create_event(topic, payload):
    producer.produce(topic, key=None, value=json.dumps(payload), callback=delivery_callback)
