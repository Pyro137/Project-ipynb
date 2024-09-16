import pytest
from IPYNBrenderer.site import is_valid_url

URL_test_data = [
    ("http://pytorch.org", True),
    ("https://pytorch.org", True),
    ("http://pytorch", False),
    ("http//pytorch", False),
    ("http:/pytorch", False),
    ("http/pytorch", False),
    ("http/pytorch", False),
    ("pytorch", False),
    ("http://asyef/", False),
]

@pytest.mark.parametrize("URL, response", URL_test_data)
def test_is_valid(URL, response):
    assert is_valid_url(URL) == response

