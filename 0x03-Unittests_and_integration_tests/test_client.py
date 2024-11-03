#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit tests for GithubOrgClient in client.py."""

import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
import requests
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient."""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, expected_result: dict,
                 mock_get_json: Mock) -> None:
        """Test that GithubOrgClient.org returns the correct value."""
        # Arrange: Set the mock to return the expected result
        mock_get_json.return_value = expected_result

        # Act: Create a GithubOrgClient instance and call the org method
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert: Check that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        # Assert: Check that the org method returns the expected result
        self.assertEqual(result, expected_result)

    def test_public_repos_url(self) -> None:
        """
        Test that GithubOrgClient._public_repos_url returns the expected URL.
        """

        # Define the mock payload with a repos_url
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Patch GithubOrgClient.org to return the mock payload
        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock,
                          return_value=mock_payload):
            client = GithubOrgClient("test_org")

            # Call _public_repos_url; check if it returns the correct repos_url
            result = client._public_repos_url
            self.assertEqual(result, mock_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json) -> None:
        """
        Test that GithubOrgClient.public_repos returns the expected list of
        repos.
        """

        # Define a mock payload for get_json
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl-3.0"}}
        ]
        # Set the return value for get_json
        mock_get_json.return_value = mock_repos_payload

        # Mock the _public_repos_url property to return a fixed URL
        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=PropertyMock) as mock_public_repos_url:
            url = "https://api.github.com/orgs/test_org/repos"
            mock_public_repos_url.return_value = url

            # Create an instance of GithubOrgClient and call public_repos
            client = GithubOrgClient("test_org")
            result = client.public_repos()

            # Verify the returned list of repo names
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            # Ensure _public_repos_url and get_json were each called once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test_org/repos")


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """Set up the class for testing"""
        cls._org_name = "test_org"
        cls.ORG_URL = "https://api.github.com/orgs/{org}"
        
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side effects for the mock
        cls.mock_get.side_effect = lambda url: cls._mock_requests(url)

    @classmethod
    def tearDownClass(cls):
        """Tear down the class after testing"""
        cls.get_patcher.stop()

    @classmethod
    def _mock_requests(cls, url):
        """Mock response based on the requested URL"""
        if url == cls.ORG_URL.format(org="test_org"):
            return MockResponse(cls.org_payload)
        if url == cls.org_payload['repos_url']:
            return MockResponse(cls.repos_payload)
        return MockResponse({})

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filtering"""
        client = GithubOrgClient("google")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


class MockResponse:
    """A mock response class to simulate requests.get().json()"""

    def __init__(self, json_data):
        self._json_data = json_data

    def json(self):
        """Return the mock JSON data"""
        return self._json_data


if __name__ == "__main__":
    unittest.main()
