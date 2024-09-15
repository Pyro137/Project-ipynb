import pytest
from IPYNBrenderer.youtube import render_and_display_video
from IPYNBrenderer.custom_exception import InvalidUrlException



URL_test_success_data = [
    ("https://youtu.be/roO5VGxOw2s", "success"),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s", "success"),
    ("https://www.youtube.com/watch?v=roO5VGxOw2s&t=42s", "success"),
]

URL_test_bad_data = [
    ("https://www.youtube.com/watch?v=roO5VGxOw2sahesbf"),  # exception
("https://www.youtube.com/watch?v=roO5VGxOw2s&t"),  # exception
("https://www.youtube.com/watch?v=roO5VGxOw2s&t==22s"),  # exception
("https://www.youtube.com/watch?v==roO5VGxOw2s&t=22s"),
]

@pytest.mark.parametrize("URL,response",URL_test_success_data)
def test_render_YT_success(URL,response):
    print("test_input",URL)
    assert render_and_display_video(URL) == response

@pytest.mark.parametrize("URL", URL_test_bad_data)
def test_render_YT_failed( URL):
    with pytest.raises(InvalidUrlException):
        render_and_display_video(URL)