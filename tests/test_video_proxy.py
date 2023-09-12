import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from module_5_proxy.general.video_streaming import RealVideoService, CachedVideoService

scenarios("video_proxy.feature")


@given("I have a real video service", target_fixture="video_service")
def create_real_video_service():
    return RealVideoService()


@given("I have a cached video service", target_fixture="video_service")
def create_cached_video_service():
    return CachedVideoService()


@when(parsers.parse('I request video content with id "{video_id}"'), target_fixture="video_content")
def request_video_content(video_id, video_service):
    return video_service.get_video_content(int(video_id))


@when("I request video content with different ids", target_fixture="cached_video_service_with_different_ids")
def request_video_content_with_different_ids(video_service):
    video_service.get_video_content(1)
    video_service.get_video_content(2)
    return video_service


@then("the real service video content should be downloaded")
def check_real_service_video_content(video_content):
    assert "Downloading video content for video ID: 1" in video_content


@then("the cached video content should be returned")
def check_cached_video_content(video_service):
    assert video_service.get_video_content(2) == "Cached video content for video ID: 2"


@then("the cached video content should be returned for each id")
def check_cached_video_content_for_each_id(cached_video_service_with_different_ids):
    assert cached_video_service_with_different_ids.get_video_content(1) == "Cached video content for video ID: 1"
    assert cached_video_service_with_different_ids.get_video_content(2) == "Cached video content for video ID: 2"
