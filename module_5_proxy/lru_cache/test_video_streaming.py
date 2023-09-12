import unittest
from module_5_proxy.lru_cache.video_streaming_cache import RealVideoService

class TestProxyPatternWithCache(unittest.TestCase):
    def test_real_subject_functionality(self):
        """Test the functionality of the Real Video Service."""
        video_service = RealVideoService()
        self.assertIn("Downloading video content for video ID: 1", video_service.get_video_content(1))

    def test_real_subject_functionality_with_cache(self):
        """Test the caching functionality of the Real Video Service using functools.lru_cache."""
        video_service = RealVideoService()

        # First time call, content is downloaded
        video_1 = video_service.get_video_content(1)

        # Second time call, content is cached
        video_2 = video_service.get_video_content(1)

        self.assertEqual(video_1, video_2)

    def test_a_lot_of_downloads(self):
        """Test the caching functionality of the Real Video Service using functools.lru_cache."""
        number_of_downloads = 1000
        video_service = RealVideoService()

        # Download a lot of videos
        videos = [video_service.get_video_content("video_id") for i in range(number_of_downloads)]

        # Assert that all videos is the same (cached)
        self.assertEqual(len(set(videos)), 1)



if __name__ == "__main__":
    unittest.main()