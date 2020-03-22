from bs4 import BeautifulSoup
import requests

URL = "hxxps://fsjfrenz.com/covid19.php"


class RequestClient(object):

    def __init__(self, url):
        self.url = url

    def make_request(self):
        response = requests.get(self.url)
        return response.text


class ResponseParser(object):

    def __init__(self):
        pass

    def parse_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        return '{}'
