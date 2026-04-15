from dataclasses import dataclass, field


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
            "produtoId": self.produtoId,
            "unidadeId": self.unidadeId,
            "quantidade": self.quantidade,
            "quantidadeComprada": self.quantidadeComprada,
            "valorUnitario": self.valorUnitario,
            "centroCustoId": self.centroCustoId,
            "operacaoFiscalId": self.operacaoFiscalId,
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
    tipoOrdemCompraId: int
    items: list[PurchaseOrderItem] = field(default_factory=list)
    installments: list[PurchaseOrderInstallment] = field(default_factory=list)
    funcionarioId: int | None = None
    freteId: int | None = None
    condicaoPagamentoId: int | None = None
    observacao: str | None = None
    tipoOC: str | None = None

    def to_dict(self, full: bool = False) -> dict:
        ret = {
            "empresaId": self.empresaId,
            "status": self.status,
            "emissao": self.emissao,
            "fornecedorId": self.fornecedorId,
            "tipoOrdemCompraId": self.tipoOrdemCompraId,
        }

        if self.funcionarioId is not None:
            ret["funcionarioId"] = self.funcionarioId
        if self.freteId is not None:
            ret["freteId"] = self.freteId
        if self.condicaoPagamentoId is not None:
            ret["condicaoPagamentoId"] = self.condicaoPagamentoId
        if self.observacao is not None:
            ret["observacao"] = self.observacao
        if self.tipoOC is not None:
            ret["tipoOC"] = self.tipoOC

        if full:
            ret["items"] = [item.to_dict() for item in self.items]
            ret["installments"] = [inst.to_dict() for inst in self.installments]

        return ret
