from confluent_kafka import Consumer

from src.ai.helpers.url_checker import check_url

conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "status_created",
    'session.timeout.ms': 6000,
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf, debug='fetch')


def consume_event():
    topic = 'status_request_created'
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise Exception(msg.error())
            else:
                # Proper message
                print(
                    '%% %s [%d] at offset %d with key %s' % (msg.topic(), msg.partition(), msg.offset(), str(msg.key()))
                )
                check_url(msg.value())
                print(msg.value())

    except KeyboardInterrupt:
        print('%% Aborted by user\n')

    finally:
        consumer.close()
