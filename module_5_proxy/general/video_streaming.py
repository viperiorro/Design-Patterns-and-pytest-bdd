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
    def get_video_content(self, video_id):
        # Simulate downloading the video content (slow operation)
        time.sleep(3)
        random_uuid = uuid.uuid4()
        video = f"Downloading video content for video ID: {video_id}. Content: {random_uuid}"
        print(video)  # Print the video content
        return video  # Return the video content


# Implement the Proxy class for the video streaming service
class CachedVideoService(VideoService):
    def __init__(self):
        self._video_service = RealVideoService()
        self._cache = dict()

    def get_video_content(self, video_id):
        # Check if video content is cached
        if video_id not in self._cache:
            self._cache[video_id] = self._video_service.get_video_content(video_id)

        video = f"Cached video content for video ID: {video_id}"
        print(video)  # Print the video content
        return video  # Return the video content
