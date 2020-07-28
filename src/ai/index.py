"""Main Entry Point"""
from src.ai.consumer.url_checker import consume_event
from src.service.database import connect
from src.service.kafka import start
from src.service.scheduler import schedule_tasks

start()
connect()


def consumer(args=None):
    """Start Service with scheduling"""
    print('Starting service...')
    consume_event()
    return 0


def scheduler(args=None):
    """Start Service with scheduling"""
    print('Starting service...')
    schedule_tasks()
    return 0
