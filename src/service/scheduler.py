import sched
import time

from src.ai.helpers.serializers import create_status_request
from src.ai.producer import producer

scheduler = sched.scheduler(time.time, time.sleep)

TOPIC = 'status_request_created'

LINK_LIST = [('https://aiven.io', 'aiven'), ('https://aiven.ix', 'aiven')]


def schedule_link_check():
    for link, pattern in LINK_LIST:
        producer.create_event(TOPIC, create_status_request(link, pattern))
    scheduler.enter(5, 1, schedule_link_check)


def schedule_tasks():
    print("Scheduling tasks...")
    scheduler.enter(5, 1, schedule_link_check)
    scheduler.run()
