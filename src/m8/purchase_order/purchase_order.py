from dataclasses import dataclass


@dataclass
class PurchaseOrderItem:
    produtoId: int
    unidadeId: int
    quantidade: float
    quantidadeComprada: float
    valorUnitario: float
    centroCustoId: int
    operacaoFiscalId: int

    def to_dict(self) -> dict:
        return {
            "produtoId": int(self.produtoId),
            "unidadeId": int(self.unidadeId),
            "quantidade": float(self.quantidade),
            "quantidadeComprada": float(self.quantidadeComprada),
            "valorUnitario": float(self.valorUnitario),
            "centroCustoId": int(self.centroCustoId),
            "operacaoFiscalId": int(self.operacaoFiscalId),
        }


@dataclass
class PurchaseOrderInstallment:
    vencimento: str
    valor: float

    def to_dict(self) -> dict:
        return {
            "vencimento": self.vencimento,
            "valor": self.valor
        }


@dataclass
class PurchaseOrder:
    empresaId: int
    status: str
    emissao: str
    fornecedorId: int
    funcionarioId: int
    freteId: int
    condicaoPagamentoId: int
    observacao: str
    items: list[PurchaseOrderItem]
    installments: list[PurchaseOrderInstallment]
    tipoOrdemCompraId: int
    tipoOC: str

    def to_dict(self, full: bool = False) -> dict:
        ret = {
            "empresaId": self.empresaId,
            "status": self.status,
            "emissao": self.emissao,
            "fornecedorId": self.fornecedorId,
            "funcionarioId": self.funcionarioId,
            "freteId": self.freteId,
            "condicaoPagamentoId": self.condicaoPagamentoId,
            "observacao": self.observacao,
            "tipoOrdemCompraId": self.tipoOrdemCompraId,
            "tipoOC": self.tipoOC,
        }

        if full:
            ret["items"] = [item.to_dict() for item in self.items]
            ret["installments"] = [installment.to_dict()
                                   for installment in self.installments]

        return ret
