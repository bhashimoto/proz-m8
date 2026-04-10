import datetime as dt
import pytest
from unittest.mock import MagicMock
from m8 import M8


def make_response(status_code=200, json_data=None):
    mock = MagicMock()
    mock.status_code = status_code
    mock.json.return_value = json_data if json_data is not None else {}
    return mock


def make_error_response(status_code, message="API error"):
    return make_response(status_code, {"errors": [{"message": message}]})


@pytest.fixture
def m8():
    client = M8()
    client.set_credentials("user", "pass", "tenant1", 1)
    return client


@pytest.fixture
def authenticated_m8(m8):
    """M8 instance with a non-expired token — skips authenticate() in @auth."""
    m8._auth_token_expiration_dt = dt.datetime.now() + dt.timedelta(hours=1)
    m8._auth_token = "fake-token"
    m8._headers["Authorization"] = "Bearer fake-token"
    return m8
