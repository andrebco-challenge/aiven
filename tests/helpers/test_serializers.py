import unittest
from datetime import datetime

from freezegun import freeze_time

from src.ai.helpers.serializers import (
    create_message,
    create_status_request,
    create_status_request_response,
    fail_status_request,
    succeed_status_request,
)


class TestSerializers(unittest.TestCase):
    @freeze_time("2012-01-01")
    def test_create_message_should_return_and_add_timestamp(self):
        event_name = 'event_name'
        metadata = {'any_key': 'any_value'}

        message_expected = {
            'event_name': 'event_name',
            'timestamp': '2012-01-01T00:00:00',
            'any_key': 'any_value',
        }

        message_create = create_message(event_name, metadata, timestamp=datetime.now().isoformat())

        assert message_create == message_expected

    @freeze_time("2012-01-01")
    def test_create_status_request_should_return_without_pattern(self):
        link = 'http://aiven.io'

        message_expected = {
            'event_name': 'status_request_created',
            'timestamp': '2012-01-01T00:00:00',
            'link': link,
        }

        message_create = create_status_request(link, timestamp=datetime.now().isoformat())

        assert message_create == message_expected

    @freeze_time("2012-01-01")
    def test_create_status_request_should_return_with_pattern(self):
        link = 'http://aiven.io'
        pattern = '.*'

        message_expected = {
            'event_name': 'status_request_created',
            'timestamp': '2012-01-01T00:00:00',
            'link': link,
            'pattern': pattern,
        }

        message_create = create_status_request(link, pattern, timestamp=datetime.now().isoformat())

        assert message_create == message_expected

    @freeze_time("2012-01-01")
    def test_create_status_response_should_return_and_add_timestamp(self):
        link = 'http://aiven.io'
        event_name = 'status_request_created'
        http_response_time = 1000
        code_return = 200

        message_expected = {
            'event_name': event_name,
            'timestamp': '2012-01-01T00:00:00',
            'link': link,
            'http_response_time': http_response_time,
            'code_return': code_return,
        }

        message_create = create_status_request_response(
            link, http_response_time, code_return, timestamp=datetime.now().isoformat()
        )

        assert message_create == message_expected

    @freeze_time("2012-01-01")
    def test_succeed_status_response_should_return_with_timestamp(self):
        link = 'http://aiven.io'
        http_response_time = 1000
        code_return = 200

        message_expected = {
            'event_name': 'status_request_succeeded',
            'timestamp': '2012-01-01T00:00:00',
            'link': link,
            'http_response_time': http_response_time,
            'code_return': code_return,
        }

        message_create = succeed_status_request(
            link, http_response_time, code_return, timestamp=datetime.now().isoformat()
        )

        assert message_create == message_expected

    @freeze_time("2012-01-01")
    def test_fail_status_response_should_return_with_timestamp(self):
        link = 'http://aiven.io'
        http_response_time = 1000
        code_return = 500

        message_expected = {
            'event_name': 'status_request_failed',
            'timestamp': '2012-01-01T00:00:00',
            'link': link,
            'http_response_time': http_response_time,
            'code_return': code_return,
        }

        message_create = fail_status_request(
            link, http_response_time, code_return, timestamp=datetime.now().isoformat()
        )

        assert message_create == message_expected
