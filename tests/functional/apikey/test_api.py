import os

os.environ["BACKEND_URL"] = "https://dev-platform-api.aixplain.com"
os.environ["BENCHMARKS_BACKEND_URL"] = "https://dev-platform-api.aixplain.com"
os.environ["MODELS_RUN_URL"] = "https://dev-models.aixplain.com/api/v1/execute"
os.environ["TEAM_API_KEY"] = ""

from aixplain.factories.api_key_factory import APIKeyFactory
from aixplain.modules import APIKey, APIKeyGlobalLimits
from datetime import datetime
import json
import pytest


def test_create_api_key_from_json():
    api_key_json = "tests/functional/apikey/apikey.json"

    with open(api_key_json, "r") as file:
        api_key_data = json.load(file)

    expires_at = datetime.strptime(api_key_data["expires_at"], "%Y-%m-%dT%H:%M:%SZ")

    api_key = APIKeyFactory.create(
        name=api_key_data["name"],
        asset_limits=[
            APIKeyGlobalLimits(
                model=api_key_data["asset_limits"][0]["model"],
                token_per_minute=api_key_data["asset_limits"][0]["token_per_minute"],
                token_per_day=api_key_data["asset_limits"][0]["token_per_day"],
                request_per_day=api_key_data["asset_limits"][0]["request_per_day"],
                request_per_minute=api_key_data["asset_limits"][0]["request_per_minute"],
            )
        ],
        global_limits=APIKeyGlobalLimits(
            token_per_minute=api_key_data["global_limits"]["token_per_minute"],
            token_per_day=api_key_data["global_limits"]["token_per_day"],
            request_per_day=api_key_data["global_limits"]["request_per_day"],
            request_per_minute=api_key_data["global_limits"]["request_per_minute"],
        ),
        budget=api_key_data["budget"],
        expires_at=expires_at,
    )

    assert isinstance(api_key, APIKey)
    assert api_key.id != ""
    assert api_key.name == api_key_data["name"]

    api_key.delete()


def test_create_api_key_from_dict():
    api_key_dict = {
        "asset_limits": [
            {
                "model": "640b517694bf816d35a59125",
                "token_per_minute": 100,
                "token_per_day": 1000,
                "request_per_day": 1000,
                "request_per_minute": 100,
            }
        ],
        "global_limits": {"token_per_minute": 100, "token_per_day": 1000, "request_per_day": 1000, "request_per_minute": 100},
        "budget": 1000,
        "expires_at": "2024-12-12T00:00:00Z",
    }

    api_key_name = "Test API Key"
    api_key = APIKeyFactory.create(
        name=api_key_name,
        asset_limits=[APIKeyGlobalLimits(**limit) for limit in api_key_dict["asset_limits"]],
        global_limits=APIKeyGlobalLimits(**api_key_dict["global_limits"]),
        budget=api_key_dict["budget"],
        expires_at=datetime.strptime(api_key_dict["expires_at"], "%Y-%m-%dT%H:%M:%SZ"),
    )

    assert isinstance(api_key, APIKey)
    assert api_key.id != ""
    assert api_key.name == api_key_name

    api_key.delete()


def test_list_api_keys():
    api_keys = APIKeyFactory.list()
    assert isinstance(api_keys, list)

    for api_key in api_keys:
        assert isinstance(api_key, APIKey)
        assert api_key.id != ""


def test_create_api_key_wrong_input():
    api_key_name = "Test API Key"

    with pytest.raises(Exception):
        APIKeyFactory.create(
            name=api_key_name,
            asset_limits="invalid_limits",
            global_limits="invalid_limits",
            budget=-1000,
            expires_at="invalid_date",
        )