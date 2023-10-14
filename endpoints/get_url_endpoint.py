import requests
from endpoints.endpoints_handler import Endpoint


class GetUrlEndpoint(Endpoint):
    text = None

    def get_long_using_short(self, code):
        response = requests.get(f'https://gotiny.cc/api/{code}')
        self.status = response.status_code
        self.text = response.text
        return response.text

    def check_stored_url_same_as_sent_url(self, sent_url):
        assert self.text == sent_url

