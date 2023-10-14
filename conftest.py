import pytest
from endpoints.create_url_endpoint import CreateUrlEndpoint
from endpoints.get_url_endpoint import GetUrlEndpoint
import random
import string


@pytest.fixture()
def url_creator_endp():
    return CreateUrlEndpoint()


@pytest.fixture()
def url_getter_endp():
    return GetUrlEndpoint()


@pytest.fixture()
def random_string():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(10))


@pytest.fixture()
def create_tiny(url_creator_endp, random_string):
    long_url = f'http://{random_string}.com'
    url_creator_endp.create_short_url_for_long_url(long_url)
    return url_creator_endp.code, long_url
