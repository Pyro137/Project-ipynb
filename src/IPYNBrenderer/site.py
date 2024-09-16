from IPython import display
from ensure import ensure_annotations
import urllib.request
from IPYNBrenderer.custom_exception import InvalidUrlException


def is_valid_url(URL: str) -> bool:
    try:
        with urllib.request.urlopen(URL, timeout=5) as response:
            return response.status == 200
    except Exception as e:
        raise InvalidUrlException

@ensure_annotations
def render_site(URL: str, width: str = "100%", height: str = "600") -> str:
    try:
        if is_valid_url(URL):
            response = display.IFrame(src=URL, width=width, height=height)
            display.display(response)
            return "success"
        else:
            raise InvalidUrlException
    except Exception as e:
        raise InvalidUrlException
    

if __name__ == "__main__":
    a=render_site("https://www.youtube.com/watch?v=zdt9Qh6XMe0&t=952s")
    print(a)
