from IPYNBrenderer.site import render_site
import pytest

URL_example_data=[
    ("https://www.google.com","success"),
    ("https://www.youtube.com","success"),
    ("https://www.github.com","success"),
    ("https://www.linkedin.com","success"),
    ("https://www.facebook.com","success"),
    ("https://www.twitter.com","success"),
    ("https://www.instagram.com","success"),
    ("https://www.pinterest.com","success"),
    ("https://www.reddit.com","success"),
    ("https://www.tumblr.com","success"),

]


@pytest.mark.parametrize("URL,response", URL_example_data)
def test_render_site_success(URL, response):  # Renamed function
    print("test_input", URL)
    assert render_site(URL) == response