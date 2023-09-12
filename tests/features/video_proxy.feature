Feature: Video Streaming with Proxy
  As a user
  I want to watch videos using a proxy to reduce loading times
  So that videos are loaded quickly from the cache

  @automation
  Scenario: Use real video service
    Given I have a real video service
    When I request video content with id "1"
    Then the real service video content should be downloaded

  @automation
  Scenario: Use cached video service
    Given I have a cached video service
    When I request video content with id "2"
    Then the cached video content should be returned

  @automation
  Scenario: Test caching functionality of cached video service
    Given I have a cached video service
    When I request video content with different ids
    Then the cached video content should be returned for each id