import re
from datetime import datetime


def create_message(event_name: str, metadata: dict = {}, timestamp: str = datetime.now().isoformat()):
    message = {'event_name': event_name, 'timestamp': timestamp}
    message.update(metadata)
    return message


def create_status_request(link: str, pattern: str = None, timestamp: str = datetime.now().isoformat()):
    message_response = {
        'link': link,
    }

    if pattern:
        message_response.update({'pattern': pattern})
    return create_message('status_request_created', message_response, timestamp=timestamp)


def create_status_request_response(
    link: str,
    http_response_time: datetime.microsecond,
    code_return: int,
    content: str = None,
    pattern: re = None,
    timestamp: str = datetime.now().isoformat(),
    event_name: str = None,
):
    message_response = {
        'link': link,
        'http_response_time': http_response_time,
        'code_return': code_return,
    }

    if content and pattern:
        regex = re.compile(pattern)
        message_response.update({'content_match': True if re.match(regex, content) else False})

    if event_name:
        return create_message(event_name, message_response, timestamp=timestamp)
    return create_message('status_request_created', message_response, timestamp=timestamp)


def succeed_status_request(
    link: str,
    http_response_time: datetime.microsecond,
    code_return: int,
    content: str = None,
    pattern: re = None,
    timestamp: str = datetime.now().isoformat(),
):
    return create_status_request_response(
        link, http_response_time, code_return, content, pattern, timestamp, event_name='status_request_succeeded'
    )


def fail_status_request(
    link: str, http_response_time: datetime.microsecond, code_return: int, timestamp: str = datetime.now().isoformat()
):
    return create_status_request_response(
        link, http_response_time, code_return, timestamp=timestamp, event_name='status_request_failed'
    )
