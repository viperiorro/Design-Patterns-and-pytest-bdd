import unittest

from module_5_proxy.general.video_streaming import RealVideoService, CachedVideoService


class TestProxyPattern(unittest.TestCase):
    def test_real_subject_functionality(self):
        """Test the functionality of the Real Video Service."""
        video_service = RealVideoService()
        self.assertIn("Downloading video content for video ID: 1", video_service.get_video_content(1))

    def test_proxy_subject_functionality(self):
        """Test the functionality of the Cached Video Service (Proxy)."""
        video_service = CachedVideoService()
        self.assertEqual(video_service.get_video_content(1), "Cached video content for video ID: 1")

    def test_cached_video_functionality(self):
        """Test the caching functionality of the Cached Video Service (Proxy)."""
        video_service = CachedVideoService()
        video_service.get_video_content(1)  # Cache video content for video ID 1
        video_service.get_video_content(2)  # Cache video content for video ID 2

        # Assert that video content is cached and returned as expected
        self.assertEqual(video_service.get_video_content(1), "Cached video content for video ID: 1")
        self.assertEqual(video_service.get_video_content(2), "Cached video content for video ID: 2")

    def test_cached_multiple_videos(self):
        """Test the caching functionality of the Cached Video Service (Proxy)."""
        video_service = CachedVideoService()

        number_of_videos = 100

        for _ in range(number_of_videos):
            video_service.get_video_content(1)

        self.assertEqual(video_service.get_video_content(1), "Cached video content for video ID: 1")


if __name__ == "__main__":
    unittest.main()
