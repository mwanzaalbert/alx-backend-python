#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit tests for GithubOrgClient in client.py."""

import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


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


if __name__ == "__main__":
    unittest.main()
