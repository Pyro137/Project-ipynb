import pytest
from IPYNBrenderer import get_time
from IPYNBrenderer.custom_exception import InvalidUrlException

good_URL_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2s", 0),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", 42),
]


URL_id_bad_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
    ("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s")
]


@pytest.mark.parametrize("URL, response", good_URL_data)
def test_get_time_info(URL, response):
    assert get_time(URL) == response

@pytest.mark.parametrize("URL", URL_id_bad_data)
def test_get_time_info_failed(URL):
    with pytest.raises(InvalidUrlException):
        get_time(URL)