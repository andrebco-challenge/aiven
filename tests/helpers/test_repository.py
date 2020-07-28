import unittest
from datetime import datetime

from ai.helpers import repository


class TestRepository(unittest.TestCase):
    def setUp(self) -> None:
        repository.delete_status_request_succeeded()
        repository.delete_status_request_failed()

    def test_insert_status_request_succeeded(self):
        now = datetime.now()
        timestamp = now.isoformat()
        link = 'https://aiven.io'
        return_code = 200
        return_time = 100
        content_match = True

        repository.insert_status_request_succeeded(timestamp, link, return_code, return_time, content_match)
        result = repository.fetch_status_request_succeeded()

        assert result[1] == now
        assert result[2] == link
        assert result[3] == return_code
        assert result[4] == return_time
        assert result[5] == content_match

    def test_insert_status_request_failed(self):
        now = datetime.now()
        timestamp = now.isoformat()
        link = 'https://aiven.io'
        return_code = 200
        return_time = 100

        repository.insert_status_request_failed(timestamp, link, return_code, return_time)
        result = repository.fetch_status_request_failed()
        assert result[1] == now
        assert result[2] == link
        assert result[3] == return_code
        assert result[4] == return_time
