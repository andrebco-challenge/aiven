from confluent_kafka.admin import AdminClient, NewTopic

TOPICS = [
    'status_request_created',
    'status_request_succeeded',
    'status_request_failed',
]


def start():
    admin = AdminClient({'bootstrap.servers': 'localhost:9092'})
    create_topics(admin, TOPICS)


def create_topics(admin, topics):
    """Create topics"""
    new_topics = [NewTopic(topic, num_partitions=1, replication_factor=1) for topic in topics]
    fs = admin.create_topics(new_topics)

    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            print("Topic {} created".format(topic))
        except Exception as e:
            print("Failed to create topic {}: {}".format(topic, e))
