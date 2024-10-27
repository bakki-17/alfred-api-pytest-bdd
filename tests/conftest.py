import pytest
from utils.APIClient import APIClient

@pytest.fixture(scope="session")
def api_client():
    return APIClient()