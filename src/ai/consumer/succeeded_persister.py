import json

from ai.helpers.consumer_utils import consume_event

from ..helpers.repository import insert_status_request_succeeded


# TODO: Add a payload Validator
def persist_succeeded(_payload: str):
    payload = json.loads(_payload)
    timestamp = payload.get('timestamp')
    link = payload.get('link')
    http_response_time = payload.get('http_response_time')
    code_return = payload.get('code_return')
    content_match = payload.get('content_match')
    try:
        insert_status_request_succeeded(timestamp, link, code_return, http_response_time, content_match)
    except Exception as e:
        print('Error on parsing status_request_succeeded event. Error: {}'.format(e))


def succeeded_consumer():
    topic = 'status_request_succeeded'
    consume_event(topic, persist_succeeded)
