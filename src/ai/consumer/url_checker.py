import json

import requests

from src.ai.helpers.serializers import fail_status_request, succeed_status_request
from src.ai.producer.generic import create_event

from .generic import consume_event


# TODO: Add a payload Validator
def check_url(_payload: str):
    payload = json.loads(_payload)
    link = payload.get('link')
    pattern = payload.get('pattern')
    try:
        response = requests.get(link)
        code_return = response.status_code
        response_time = response.elapsed.microseconds
        content = response.content.decode("utf-8")

        if code_return == requests.codes.OK:
            event_payload = succeed_status_request(link, response_time, code_return, content, pattern)
            create_event('status_request_succeeded', event_payload)
        else:
            event_payload = fail_status_request(link, response_time, code_return, content, pattern)
            create_event('status_request_failed', event_payload)
    except requests.ConnectionError:
        event_payload = fail_status_request(link, 0, 0)
        create_event('status_request_failed', event_payload)


def url_checker_consumer():
    topic = 'status_request_created'
    consume_event(topic, check_url)
