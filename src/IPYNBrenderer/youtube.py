from IPython.display import display, IFrame, HTML

from ensure import ensure_annotations
from IPYNBrenderer.custom_exception import InvalidUrlException
from IPYNBrenderer.logger import logger
from py_youtube import Data


@ensure_annotations
def get_time(URL: str) -> int:
    def _verify_vid_id_len(vid_id: str, __expected_len: int = 11) -> None:  # Adding type annotations
        len_of_vid_id = len(vid_id)
        if len_of_vid_id != __expected_len:
            raise InvalidUrlException(
                f"Invalid video id with length: {len_of_vid_id}, expected: {__expected_len}"
            )

    try:
        split_val = URL.split("=")
        if len(split_val) > 3:
            raise InvalidUrlException
        if "watch" in URL:
            if "&t" in URL:
                vid_id, time = split_val[-2][:-2], int(split_val[-1][:-1])
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = split_val[-1], 0
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
        else:
            if "=" in URL and "?t" in URL:
                vid_id, time = split_val[0].split("/")[-1][:-2], int(split_val[-1])
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
            else:
                vid_id, time = URL.split("/")[-1], 0
                _verify_vid_id_len(vid_id)
                logger.info(f"video starts at: {time}")
                return time
    except Exception:
        raise InvalidUrlException


@ensure_annotations
def render_and_display_video(URL: str, width: int = 854, height: int = 480) -> str:
    try:
        
        if URL is None:
            raise InvalidUrlException("Invalid URL")
        
        # Fetch data from YouTube Data API
        data = Data(URL).data()
        
        # Check if the video exists by checking the publish date
        if data["publishdate"] is not None:
            # Get the time from the URL
            time = get_time(URL)
            vid_ID = data["id"]
            embed_url = f"https://www.youtube.com/embed/{vid_ID}?start={time}"
            logger.info(f"Embed URL: {embed_url}")

            # Create iframe HTML to embed the video
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

            # Return success message
            return "success"
        else:
            # Raise exception if no publish date is found (invalid video)
            raise InvalidUrlException

    except Exception as e:
        logger.error(f"Error in render_and_display_video: {e}")
        raise InvalidUrlException
