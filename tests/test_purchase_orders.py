import pytest
from unittest.mock import patch, MagicMock
from m8 import M8, BadRequestException
from m8.purchase_order import PurchaseOrder, PurchaseOrderItem, PurchaseOrderInstallment
from .conftest import make_response, make_error_response


def make_po() -> PurchaseOrder:
    item = PurchaseOrderItem(
        produtoId=10, unidadeId=1, quantidade=2.0, quantidadeComprada=2.0,
        valorUnitario=50.0, centroCustoId=3, operacaoFiscalId=4
    )
    installment = PurchaseOrderInstallment(vencimento="2024-03-01", valor=100.0)
    return PurchaseOrder(
        empresaId=1, status="Aberto", emissao="2024-01-01", fornecedorId=5,
        funcionarioId=6, freteId=0, condicaoPagamentoId=1, observacao="test",
        items=[item], installments=[installment],
        tipoOrdemCompraId=1, tipoOC="Normal"
    )


PO_CREATED = {"data": {"id": 99}}
ITEM_CREATED = {"data": {"id": 201}}
INSTALLMENT_CREATED = {"data": {"id": 301}}


class TestGetPurchaseOrders:
    def test_get_purchase_orders_returns_data(self, authenticated_m8):
        payload = {"data": [{"id": 1}, {"id": 2}]}
        with patch("m8.m8.requests.get", return_value=make_response(200, payload)):
            result = authenticated_m8.get_purchase_orders({"status": "Aberto"})

        assert result == payload["data"]

    def test_get_purchase_order_items_returns_data(self, authenticated_m8):
        payload = {"data": [{"id": 10}]}
        with patch("m8.m8.requests.get", return_value=make_response(200, payload)) as mock_get:
            result = authenticated_m8.get_purchase_order_items(99, {})

        assert result == payload["data"]
        url = mock_get.call_args.kwargs["url"]
        assert "99" in url
        assert "item" in url


class TestCreatePurchaseOrder:
    def test_create_purchase_order_returns_id(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_response(200, PO_CREATED)):
            po_id = authenticated_m8.create_purchase_order(make_po())

        assert po_id == 99

    def test_create_purchase_order_raises_on_error(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_error_response(400, "invalid PO")):
            with pytest.raises(BadRequestException, match="invalid PO"):
                authenticated_m8.create_purchase_order(make_po())

    def test_create_purchase_order_not_full_only_calls_po_endpoint(self, authenticated_m8):
        with patch("m8.m8.requests.post", return_value=make_response(200, PO_CREATED)) as mock_post:
            authenticated_m8.create_purchase_order(make_po(), full=False)

        assert mock_post.call_count == 1
        url = mock_post.call_args.args[0]
        assert "item" not in url
        assert "parcela" not in url

    def test_create_purchase_order_full_creates_items_and_installments(self, authenticated_m8):
        responses = [
            make_response(200, PO_CREATED),
            make_response(200, ITEM_CREATED),
            make_response(200, INSTALLMENT_CREATED),
        ]
        with patch("m8.m8.requests.post", side_effect=responses) as mock_post:
            authenticated_m8.create_purchase_order(make_po(), full=True)

        assert mock_post.call_count == 3
        urls = [c.args[0] for c in mock_post.call_args_list]
        assert any("item" in u for u in urls)
        assert any("parcela" in u for u in urls)


class TestCreatePurchaseOrderItem:
    def test_create_purchase_order_item_returns_id(self, authenticated_m8):
        item = PurchaseOrderItem(
            produtoId=10, unidadeId=1, quantidade=2.0, quantidadeComprada=2.0,
            valorUnitario=50.0, centroCustoId=3, operacaoFiscalId=4
        )
        with patch("m8.m8.requests.post", return_value=make_response(200, ITEM_CREATED)):
            item_id = authenticated_m8.create_purchase_order_item(99, item)

        assert item_id == 201

    def test_create_purchase_order_item_raises_on_error(self, authenticated_m8):
        item = PurchaseOrderItem(
            produtoId=10, unidadeId=1, quantidade=2.0, quantidadeComprada=2.0,
            valorUnitario=50.0, centroCustoId=3, operacaoFiscalId=4
        )
        with patch("m8.m8.requests.post", return_value=make_error_response(400, "bad item")):
            with pytest.raises(BadRequestException, match="bad item"):
                authenticated_m8.create_purchase_order_item(99, item)


class TestCreatePurchaseOrderInstallment:
    def test_create_purchase_order_installment_returns_id(self, authenticated_m8):
        installment = PurchaseOrderInstallment(vencimento="2024-03-01", valor=100.0)
        with patch("m8.m8.requests.post", return_value=make_response(200, INSTALLMENT_CREATED)):
            inst_id = authenticated_m8.create_purchase_order_installment(99, installment)

        assert inst_id == 301

    def test_create_purchase_order_installment_raises_on_error(self, authenticated_m8):
        installment = PurchaseOrderInstallment(vencimento="2024-03-01", valor=100.0)
        with patch("m8.m8.requests.post", return_value=make_error_response(400, "bad installment")):
            with pytest.raises(BadRequestException, match="bad installment"):
                authenticated_m8.create_purchase_order_installment(99, installment)
