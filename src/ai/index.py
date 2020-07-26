"""Main Entry Point"""
import sys

from src.ai.consumer.url_checker import consume_event
from src.service.scheduler import schedule_tasks


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


if __name__ == "__main__":
    sys.exit(consumer())  # pragma: no cover
