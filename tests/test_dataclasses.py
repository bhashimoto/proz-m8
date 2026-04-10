from m8.purchase_order import PurchaseOrder, PurchaseOrderItem, PurchaseOrderInstallment


class TestPurchaseOrderItem:
    def test_to_dict_serializes_all_fields(self):
        item = PurchaseOrderItem(
            produtoId=10, unidadeId=2, quantidade=3.5, quantidadeComprada=3.5,
            valorUnitario=99.99, centroCustoId=7, operacaoFiscalId=8
        )
        d = item.to_dict()

        assert d == {
            "produtoId": 10,
            "unidadeId": 2,
            "quantidade": 3.5,
            "quantidadeComprada": 3.5,
            "valorUnitario": 99.99,
            "centroCustoId": 7,
            "operacaoFiscalId": 8,
        }


class TestPurchaseOrderInstallment:
    def test_to_dict_serializes_all_fields(self):
        inst = PurchaseOrderInstallment(vencimento="2024-03-15", valor=250.0)
        d = inst.to_dict()

        assert d == {"vencimento": "2024-03-15", "valor": 250.0}


class TestPurchaseOrder:
    def _make_po(self):
        item = PurchaseOrderItem(
            produtoId=1, unidadeId=1, quantidade=1.0, quantidadeComprada=1.0,
            valorUnitario=10.0, centroCustoId=1, operacaoFiscalId=1
        )
        installment = PurchaseOrderInstallment(vencimento="2024-04-01", valor=10.0)
        return PurchaseOrder(
            empresaId=1, status="Aberto", emissao="2024-01-01", fornecedorId=2,
            funcionarioId=3, freteId=0, condicaoPagamentoId=1, observacao="obs",
            items=[item], installments=[installment],
            tipoOrdemCompraId=1, tipoOC="Normal"
        )

    def test_to_dict_excludes_items_by_default(self):
        d = self._make_po().to_dict()

        assert "items" not in d
        assert "installments" not in d

    def test_to_dict_includes_required_fields(self):
        d = self._make_po().to_dict()

        assert d["empresaId"] == 1
        assert d["status"] == "Aberto"
        assert d["emissao"] == "2024-01-01"
        assert d["fornecedorId"] == 2
        assert d["tipoOC"] == "Normal"

    def test_to_dict_full_includes_nested_items_and_installments(self):
        d = self._make_po().to_dict(full=True)

        assert "items" in d
        assert "installments" in d
        assert len(d["items"]) == 1
        assert len(d["installments"]) == 1
        assert d["items"][0]["produtoId"] == 1
        assert d["installments"][0]["vencimento"] == "2024-04-01"

    def test_to_dict_full_false_still_excludes_items(self):
        d = self._make_po().to_dict(full=False)

        assert "items" not in d
        assert "installments" not in d
