from typing import Callable

from confluent_kafka import Consumer


def start_consumer():
    conf = {
        'bootstrap.servers': "localhost:9092",
        'group.id': "status_created",
        'session.timeout.ms': 6000,
        'auto.offset.reset': 'earliest',
    }
    # TODO: Improve debugging instead of >>: consumer = Consumer(conf, debug='fetch')
    return Consumer(conf)


def consume_event(topic: str, callback: Callable):
    consumer = start_consumer()
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise Exception(msg.error())
            else:
                print('%% %s [%d] at offset %d' % (msg.topic(), msg.partition(), msg.offset()))
                callback(msg.value())

    except KeyboardInterrupt:
        print('%% Aborted by user\n')
