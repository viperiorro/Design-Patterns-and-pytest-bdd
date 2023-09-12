from functools import lru_cache
import time
import uuid
from abc import ABC, abstractmethod


# Define the Subject interface
class VideoService(ABC):
    @abstractmethod
    def get_video_content(self, video_id):
        pass


# Implement the Real Subject (Video Streaming Service)
class RealVideoService(VideoService):
    @lru_cache(maxsize=None)
    def get_video_content(self, video_id):
        # Simulate downloading the video content (slow operation)
        time.sleep(3)
        random_uuid = uuid.uuid4()
        video = f"Downloading video content for video ID: {video_id}. Content: {random_uuid}"
        print(video)
        return video
