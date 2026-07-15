"""Tests for the public get_secret API."""
from unittest import mock

import pytest

import gcp_notifier
from gcp_notifier import get_secret


def test_get_secret_empty_secret_id_raises() -> None:
    """An empty secret_id is rejected before any network call."""
    with pytest.raises(ValueError):
        get_secret("", project_id="my-project")


def test_get_secret_no_project_raises(monkeypatch) -> None:
    """Missing project_id and no detected project raises ValueError."""
    monkeypatch.setattr(gcp_notifier, "project_id", "")
    with pytest.raises(ValueError):
        get_secret("MY_SECRET")


def test_get_secret_returns_decoded_value() -> None:
    """The payload bytes are decoded to a UTF-8 string."""
    with mock.patch(
        "google.cloud.secretmanager.SecretManagerServiceClient"
    ) as mock_client:
        access = mock_client.return_value.access_secret_version
        access.return_value.payload.data = b"s3cr3t"
        value = get_secret("MY_SECRET", project_id="my-project")
    assert value == "s3cr3t", "payload bytes should decode to str"
    access.assert_called_once_with(
        request={
            "name": "projects/my-project/secrets/MY_SECRET/versions/latest"
        }
    )


def test_get_secret_falls_back_to_detected_project(monkeypatch) -> None:
    """When project_id is omitted, the detected project is used."""
    monkeypatch.setattr(gcp_notifier, "project_id", "detected-project")
    with mock.patch(
        "google.cloud.secretmanager.SecretManagerServiceClient"
    ) as mock_client:
        access = mock_client.return_value.access_secret_version
        access.return_value.payload.data = b"value"
        get_secret("MY_SECRET")
    access.assert_called_once_with(
        request={
            "name": (
                "projects/detected-project/secrets/MY_SECRET/versions/latest"
            )
        }
    )
