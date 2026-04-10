import datetime as dt
import json
import pytest
from unittest.mock import patch, MagicMock, mock_open
from m8 import M8, UnauthorizedException, BadRequestException, load_credentials_from_file
from .conftest import make_response, make_error_response


AUTH_SUCCESS = {
    "data": {
        "token": "test-jwt-token",
        "minutesExpire": 60,
    }
}


class TestAuthenticate:
    def test_authenticate_success(self, m8):
        with patch("m8.m8.requests.post", return_value=make_response(200, AUTH_SUCCESS)):
            m8.authenticate()

        assert m8._auth_token == "test-jwt-token"
        assert m8._headers["Authorization"] == "Bearer test-jwt-token"
        assert m8._auth_token_expiration_dt > dt.datetime.now()

    def test_authenticate_401_raises_unauthorized(self, m8):
        with patch("m8.m8.requests.post", return_value=make_response(401)):
            with pytest.raises(UnauthorizedException):
                m8.authenticate()

    def test_authenticate_error_raises_bad_request(self, m8):
        with patch("m8.m8.requests.post", return_value=make_error_response(400, "Invalid credentials")):
            with pytest.raises(BadRequestException, match="Invalid credentials"):
                m8.authenticate()


class TestAuthDecorator:
    def test_auth_decorator_refreshes_expired_token(self, m8):
        auth_mock = make_response(200, AUTH_SUCCESS)
        get_mock = make_response(200, {"data": []})

        with patch("m8.m8.requests.post", return_value=auth_mock) as mock_post, \
             patch("m8.m8.requests.get", return_value=get_mock):
            m8.get_invoices({})

        mock_post.assert_called_once()  # authenticate() was called

    def test_auth_decorator_skips_if_token_valid(self, authenticated_m8):
        get_mock = make_response(200, {"data": []})

        with patch("m8.m8.requests.post") as mock_post, \
             patch("m8.m8.requests.get", return_value=get_mock):
            authenticated_m8.get_invoices({})

        mock_post.assert_not_called()

    def test_auth_decorator_retries_on_bad_request(self, m8):
        error_resp = make_error_response(400, "bad request")
        auth_success = make_response(200, AUTH_SUCCESS)
        get_mock = make_response(200, {"data": []})

        # First auth attempt fails, second succeeds
        with patch("m8.m8.requests.post", side_effect=[error_resp, auth_success]), \
             patch("m8.m8.requests.get", return_value=get_mock), \
             patch("m8.m8.time.sleep"):
            m8.get_invoices({})  # should not raise

    def test_auth_decorator_raises_after_max_retries(self, m8):
        error_resp = make_error_response(400, "bad request")

        with patch("m8.m8.requests.post", return_value=error_resp), \
             patch("m8.m8.time.sleep"):
            with pytest.raises(BadRequestException):
                m8.get_invoices({})


class TestSwitchCompany:
    def test_switch_company_reauthenticates(self, authenticated_m8):
        auth_mock = make_response(200, AUTH_SUCCESS)

        with patch("m8.m8.requests.post", return_value=auth_mock) as mock_post:
            authenticated_m8.switch_company(99)

        assert authenticated_m8._company == 99
        mock_post.assert_called_once()

    def test_switch_company_noop_same_id(self, authenticated_m8):
        with patch("m8.m8.requests.post") as mock_post:
            authenticated_m8.switch_company(1)  # same as fixture company_id

        mock_post.assert_not_called()


class TestLoadCredentials:
    def test_load_credentials_from_file(self):
        data = json.dumps({"username": "myuser", "password": "mypass"})
        with patch("builtins.open", mock_open(read_data=data)):
            username, password = load_credentials_from_file("creds.json")

        assert username == "myuser"
        assert password == "mypass"
