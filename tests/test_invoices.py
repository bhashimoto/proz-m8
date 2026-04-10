import pytest
from unittest.mock import patch, call
from m8 import M8, UnauthorizedException, BadRequestException
from .conftest import make_response, make_error_response


INVOICE_LIST = {"data": [{"id": 1, "status": "Pendente"}, {"id": 2, "status": "Pendente"}]}


class TestGetInvoices:
    def test_get_invoices_returns_data(self, authenticated_m8):
        with patch("m8.m8.requests.get", return_value=make_response(200, INVOICE_LIST)):
            result = authenticated_m8.get_invoices({"Status": "Pendente"})

        assert result == INVOICE_LIST["data"]

    def test_get_invoices_raises_on_error(self, authenticated_m8):
        with patch("m8.m8.requests.get", return_value=make_error_response(500, "server error")):
            with pytest.raises(BadRequestException, match="server error"):
                authenticated_m8.get_invoices({})

    def test_get_invoices_builds_query_string(self, authenticated_m8):
        with patch("m8.m8.requests.get", return_value=make_response(200, {"data": []})) as mock_get:
            authenticated_m8.get_invoices({"Status": "Pendente", "Empresa": "1"})

        url = mock_get.call_args.kwargs["url"]
        assert "Status=Pendente" in url
        assert "Empresa=1" in url

    def test_get_unsent_invoices_uses_pendente_status(self, authenticated_m8):
        with patch("m8.m8.requests.get", return_value=make_response(200, {"data": []})) as mock_get:
            authenticated_m8.get_unsent_invoices()

        url = mock_get.call_args.kwargs["url"]
        assert "Status=Pendente" in url


class TestSendInvoice:
    def test_send_invoice_success(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_response(200, {})):
            authenticated_m8.send_invoice(42)  # should not raise

    def test_send_invoice_raises_on_error(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_error_response(400, "cannot send")):
            with pytest.raises(BadRequestException, match="cannot send"):
                authenticated_m8.send_invoice(42)

    def test_send_invoice_posts_to_correct_url(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_response(200, {})) as mock_post:
            authenticated_m8.send_invoice(42)

        url = mock_post.call_args.kwargs["url"]
        assert "42" in url
        assert "faturar" in url


class TestCancelInvoice:
    def test_cancel_invoice_success(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_response(200, {})) as mock_post:
            authenticated_m8.cancel_invoice(42, "Wrong order")

        url = mock_post.call_args.args[0]
        body = mock_post.call_args.kwargs["json"]
        assert "42" in url
        assert "cancelar" in url
        assert body["motivo"] == "Wrong order"

    def test_cancel_invoice_401_raises_unauthorized(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_response(401)):
            with pytest.raises(UnauthorizedException):
                authenticated_m8.cancel_invoice(42, "reason")

    def test_cancel_invoice_error_raises_bad_request(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_error_response(400, "cannot cancel")):
            with pytest.raises(BadRequestException, match="cannot cancel"):
                authenticated_m8.cancel_invoice(42, "reason")


class TestUpdateInvoice:
    def test_update_invoice_success(self, authenticated_m8):
        with patch("m8.m8.requests.patch", return_value=make_response(200, {})):
            authenticated_m8.update_invoice(42, {"emissao": "2024-01-01"})  # should not raise

    def test_update_invoice_none_context_sends_empty_dict(self, authenticated_m8):
        with patch("m8.m8.requests.patch", return_value=make_response(200, {})) as mock_patch:
            authenticated_m8.update_invoice(42)

        sent_json = mock_patch.call_args.kwargs["json"]
        assert sent_json == {}

    def test_update_invoice_mutable_default_not_shared(self, authenticated_m8):
        """Two calls with no context must not share the same dict object."""
        with patch("m8.m8.requests.patch", return_value=make_response(200, {})) as mock_patch:
            authenticated_m8.update_invoice(1)
            authenticated_m8.update_invoice(2)

        calls = mock_patch.call_args_list
        assert calls[0].kwargs["json"] is not calls[1].kwargs["json"]

    def test_update_invoice_raises_on_error(self, authenticated_m8):
        with patch("m8.m8.requests.patch", return_value=make_error_response(400, "bad update")):
            with pytest.raises(BadRequestException, match="bad update"):
                authenticated_m8.update_invoice(42, {"emissao": "2024-01-01"})


class TestSendInvoiceWithCustomDate:
    def test_send_invoice_with_custom_date_calls_update_then_send(self, authenticated_m8):
        patch_mock = make_response(200, {})
        post_mock = make_response(200, {})

        with patch("m8.m8.requests.patch", return_value=patch_mock) as mock_patch, \
             patch("m8.m8.requests.post", return_value=post_mock) as mock_post:
            authenticated_m8.send_invoice_with_custom_date(42, "2024-03-01")

        # PATCH was called for update_invoice
        patch_url = mock_patch.call_args.kwargs["url"]
        assert "42" in patch_url
        assert mock_patch.call_args.kwargs["json"] == {"emissao": "2024-03-01"}

        # POST was called for send_invoice
        post_url = mock_post.call_args.kwargs["url"]
        assert "42" in post_url
        assert "faturar" in post_url


class TestPatchWithRetries:
    def test_patch_with_retries_succeeds_first_try(self, authenticated_m8):
        ok = make_response(200, {})
        with patch("m8.m8.requests.patch", return_value=ok) as mock_patch:
            result = authenticated_m8.patch_with_retries(max_retries=3, url="http://x", json={})

        assert result.status_code == 200
        assert mock_patch.call_count == 1

    def test_patch_with_retries_retries_on_connection_error(self, authenticated_m8):
        ok = make_response(200, {})
        with patch("m8.m8.requests.patch", side_effect=[ConnectionError(), ok]) as mock_patch, \
             patch("m8.m8.time.sleep"):
            result = authenticated_m8.patch_with_retries(max_retries=3, url="http://x", json={})

        assert result.status_code == 200
        assert mock_patch.call_count == 2

    def test_patch_with_retries_raises_after_max_retries(self, authenticated_m8):
        with patch("m8.m8.requests.patch", side_effect=ConnectionError()), \
             patch("m8.m8.time.sleep"):
            with pytest.raises(ConnectionError):
                authenticated_m8.patch_with_retries(max_retries=2, url="http://x", json={})
