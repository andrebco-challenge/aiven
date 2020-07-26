"""Main Entry Point"""
import sys

from src.service.scheduler import schedule_tasks


def main(args=None):
    """Start Service with scheduling"""
    print('Starting service...')
    schedule_tasks()
    # return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
