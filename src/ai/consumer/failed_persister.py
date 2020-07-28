import json

from ai.helpers.consumer_utils import consume_event

from ..helpers.repository import insert_status_request_failed


# TODO: Add a payload Validator
def persist_failed(_payload: str):
    payload = json.loads(_payload)
    timestamp = payload.get('timestamp')
    link = payload.get('link')
    http_response_time = payload.get('http_response_time')
    code_return = payload.get('code_return')
    try:
        insert_status_request_failed(timestamp, link, code_return, http_response_time)
    except Exception as e:
        print('Error on parsing status_request_failed event. Error: {}'.format(e))


def failed_consumer():
    topic = 'status_request_failed'
    consume_event(topic, persist_failed)
