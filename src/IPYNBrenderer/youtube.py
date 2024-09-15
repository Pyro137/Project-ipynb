from IPython.display import display, IFrame, HTML

from ensure import ensure_annotations
from IPYNBrenderer.custom_exception import InvalidUrlException
from IPYNBrenderer.logger import logger
from py_youtube import Data

def get_time(URL: str) -> int:
    def verify_id(vid_id, expected_len=11):
        len_of_video_id = len(vid_id)
        if len_of_video_id != expected_len:
            raise InvalidUrlException(f"Invalid video ID. Expected {expected_len} characters, got {len_of_video_id}")

    try:
        split_val = URL.split("=")
        if len(split_val) > 3:
            raise InvalidUrlException("Invalid link")
        if "watch" in URL:
            if "&t" in URL:
                vid_id, time = split_val[-2][:-2], int(split_val[2].split("s")[0])
                verify_id(vid_id)
                logger.info(f"video start from {time}")
                return time
            else:
                vid_id, time = split_val[-1], 0
                verify_id(vid_id)
                logger.info(f"video starts at: {time}")
                return time
    except Exception as e:
        raise e


@ensure_annotations
def render_and_display_video(URL: str, width: int = 854, height: int = 480) -> str:
    try:
        if URL is None:
            raise InvalidUrlException("Invalid URL")
        data = Data(URL).data()
        if data["publishdate"] is not None:
            time = get_time(URL)
            vid_ID = data["id"]
            embed_url = f"https://www.youtube.com/embed/{vid_ID}?start={time}"
            logger.info(f"Embed URL: {embed_url}")

            # Create iframe HTML
            iframe = f"""
            <iframe 
            width="{width}" height="{height}" 
            src="{embed_url}" 
            title="YouTube video player" 
            frameborder="0" 
            allow="accelerometer; 
            autoplay; clipboard-write; 
            encrypted-media; 
            gyroscope; picture-in-picture; 
            web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""

            # Display the iframe in the notebook
            display(HTML(iframe))

            # Return the embed URL as a string
            return "successed"
    except Exception as e:
        raise e


if "__main__" == __name__:
    render_and_display_video("https://www.youtube.com/watch?v=rzO0_-axf40&t=1539s")
