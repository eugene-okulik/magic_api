import requests
from endpoints.endpoints_handler import Endpoint


class CreateUrlEndpoint(Endpoint):
    long = None
    code = None
    sent_url = None
    sent_code = None

    def create_short_url_for_long_url(self, long_url, code=None):
        if code:
            response = requests.post(
                'https://gotiny.cc/api',
                headers={'Content-Type': 'application/json'},
                json={'long': long_url, 'custom': code}
            )
        else:
            response = requests.post(
                'https://gotiny.cc/api',
                headers={'Content-Type': 'application/json'},
                json={'input': long_url}
            )
        self.sent_code = code if code else None
        self.sent_url = long_url
        self.status = response.status_code
        self.long = response.json()[0]['long']
        self.code = response.json()[0]['code']
        return response

    def check_long_url_same_as_sent(self):
        assert self.sent_url == self.long

    def check_code_is_not_empty(self):
        assert len(self.code) > 0

    def check_short_code_same_as_sent(self):
        assert self.sent_code == self.code
