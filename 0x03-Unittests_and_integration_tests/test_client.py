#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit tests for GithubOrgClient in client.py."""

import unittest
from unittest.mock import patch, Mock
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


if __name__ == "__main__":
    unittest.main()
