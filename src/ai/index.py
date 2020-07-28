"""Main Entry Point"""
from src.ai.consumer.failed_persister import failed_consumer
from src.ai.consumer.succeeded_persister import succeeded_consumer
from src.ai.consumer.url_checker import url_checker_consumer
from src.service.database import connect
from src.service.kafka import start
from src.service.scheduler import schedule_tasks

start()
connect()


def url_consumer(args=None):
    """Start Service with scheduling"""
    print('Starting service...')
    url_checker_consumer()
    return 0


def succeeded_messages_consumer(args=None):
    """Start Service with scheduling"""
    print('Starting service...')
    succeeded_consumer()
    return 0


def failed_messages_consumer(args=None):
    """Start Service with scheduling"""
    print('Starting service...')
    failed_consumer()
    return 0


def task_scheduler(args=None):
    """Start Service with scheduling"""
    print('Starting service...')
    schedule_tasks()
    return 0
