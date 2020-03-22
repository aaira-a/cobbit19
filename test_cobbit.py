import json

import unittest
import responses

from cobbit import (
    RequestClient,
    ResponseParser,
)


class RequestTests(unittest.TestCase):

    def setUp(self):
        self.url = "https://thedomain/thepath"
        self.response_body = "<html><h1>header1</h1><body>body1</body></html>"
        self.client = RequestClient(self.url)

    @responses.activate
    def test_make_request_with_url_from_constructor(self):
        responses.add(responses.GET, self.url)

        self.client.make_request()
        actual_url = responses.calls[0].request.url

        self.assertEqual(self.url, actual_url)

    @responses.activate
    def test_make_request_returns_html_text(self):
        responses.add(
            method=responses.GET,
            url=self.url,
            body=self.response_body,
        )

        res = self.client.make_request()

        self.assertEqual(self.response_body, res)


class ResponseParserTests(unittest.TestCase):

    def setUp(self):
        self.test_file = open("fixture_20200322.html")
        self.mock_response = self.test_file.read()

        self.parser = ResponseParser()
        self.result = self.parser.parse_html(self.mock_response)

    def tearDown(self):
        self.test_file.close()

    def test_parse_html_returns_json_string(self):
        actual = json.loads(self.parser.parse_html(self.mock_response))

        # valid json should be able to be loaded into dict by json.loads()
        self.assertIsInstance(actual, dict)
