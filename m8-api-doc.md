# M8 Integra API — SDK Reference

## Overview

- **Base URL:** `https://api.integra.m8sistemas.com.br`
- **OpenAPI Spec:** `GET /swagger/v1/swagger.json`
- **Version:** 1.0 (OpenAPI 3.0.4)
- **Auth:** Bearer token — obtain via `POST /v1/auth/token`

---

## Authentication

```
POST /v1/auth/token
Content-Type: application/json

# Request body
{ "tenant": string, "username": string, "password": string, "company": int32, "domain": string? }

# Response 200
{ "data": { "token": string, "expiration": datetime }, "errors": null }
```

Include token in all requests:
`Authorization: Bearer <token>`

---

## Response Envelope

All responses follow:
```json
{ "data": <T | T[] | null>, "errors": [{ "message": "string", "field": "string?" }] | null }
```

- **List endpoints** → `{ data: T[], errors: null }`
- **Single object** → `{ data: T, errors: null }`
- **Create/Update** → `{ data: { id: int }, errors: null }`
- **Empty success** → `{ data: null, errors: null }`

**HTTP status codes:** `200` OK · `400` Bad Request · `401` Unauthorized · `500` Internal Error

---

## Pagination

All list endpoints accept: `Page` (integer, default 1) and `PageSize` (integer).

---

## Endpoints

### Autenticação

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/auth/token` | Obter Token | — |

**`POST` Obter Token — body fields:** `tenant`, `username`, `password`, `company`, `domain`

---

### Checklist

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/configuracoes/checklist` | Listar Checklists | EstaExcluido, Id, Nome, Page, PageSize |

---

### Classificação de Pessoas

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/configuracoes/classificacaopessoa` | Listar | Id, Nome, Page, PageSize |

---

### Clientes

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/configuracoes/cliente` | Listar | IndicadorVendaId, IndicadorVendaNome, Id, RazaoSocial, Fantasia, CpfCnpj, DataAtualizacaoInicial, Da |
| `PATCH` | `_see description_` | Editar | `id`(path) |
| `GET` | `/v1/configuracoes/cliente/{id}` | Obter | `id`(path) |
| `GET` | `/v1/configuracoes/cliente/{clienteId}/endereco` | Listar Endereços | `clienteId`(path), TipoEndereco, Cep, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSize |
| `POST` | `/v1/configuracoes/cliente/{clienteId}/endereco` | Cadastrar Endereço | `clienteId`(path) |
| `GET` | `/v1/configuracoes/cliente/{clienteId}/tabelapreco` | Listar Tabelas Preços | `clienteId`(path), Page, PageSize |
| `GET` | `/v1/configuracoes/cliente/{clienteId}/contato` | Listar Contatos | `clienteId`(path), Page, PageSize |
| `POST` | `/v1/configuracoes/cliente/{clienteId}/contato` | Cadastrar Contato | `clienteId`(path) |
| `GET` | `/v1/configuracoes/cliente/{clienteId}/historicolimite` | Listar Histórico de Alterações de Limite | `clienteId`(path), Page, PageSize |
| `POST` | `/v1/configuracoes/cliente/{clienteId}/historicolimite` | Cadastrar Histórico de Alterações de Limite | `clienteId`(path) |
| `GET` | `/v1/configuracoes/cliente/{clienteId}/vendedor` | Listar Vendedores | `clienteId`(path), Page, PageSize |
| `POST` | `/v1/configuracoes/cliente/{clienteId}/vendedor` | Cadastrar Vendedor | `clienteId`(path) |

**`POST` Cadastrar — body fields:** `tipoPessoaId`, `classificacaoId`, `cpfCnpj`, `razaoSocial`, `cep`, `logradouro`, `numero`, `bairroId`, `bairroNome`, `municipioId`, `municipioNome`, `uf`, `municipioIbge`, `fantasia`, `complemento`, `letra`, `apelido`, `tabelaPrecoId`, `tipoContribuinte`, `regimeTributario`

**`PATCH` Editar — body fields:** `tipoPessoaId`, `classificacaoId`, `cpfCnpj`, `razaoSocial`, `cep`, `logradouro`, `numero`, `bairroId`, `bairroNome`, `municipioId`, `municipioNome`, `uf`, `municipioIbge`, `fantasia`, `complemento`, `letra`, `apelido`, `tipoContribuinte`, `regimeTributario`, `operacaoConsumidorNFe`

**`POST` Cadastrar Endereço — body fields:** `tipoEndereco`, `cep`, `logradouro`, `numero`, `municipioIbge`, `municipioId`, `municipioNome`, `uf`, `bairroId`, `bairroNome`, `complemento`, `letra`, `razaoSocialRecebimento`, `cpfCnpjRecebimento`, `inscricaoEstadualRecebimento`, `caixaPostal`, `pontoReferencia`

**`POST` Cadastrar Contato — body fields:** `tipo`, `nome`, `telefone`, `email`, `cargoId`, `telefoneAdicional`, `cpfCnpj`, `observacao`

**`POST` Cadastrar Histórico de Alterações de Limite — body fields:** `valorLimiteAtual`, `jurosPadrao`, `dataValidadeLimiteCredito`

**`POST` Cadastrar Vendedor — body fields:** `vendedorId`, `padrao`

---

### Clientes — Adiantamento

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/financeiro/adiantamentocliente` | Cadastrar | — |
| `GET` | `/v1/financeiro/adiantamentocliente` | Listar | Id, ClienteId, DataEmissaoInicial, DataEmissaoFinal, DataLancamentoInicial, DataLancamentoFinal, Pag |
| `PUT` | `/v1/financeiro/adiantamentocliente/{id}` | Editar | `id`(path) |

**`POST` Cadastrar — body fields:** `empresaId`, `clienteId`, `documento`, `valor`, `meioPagamentoId`, `operacaoFinanceiraId`, `contaOrigemId`, `contaDestinoId`, `historicoContabilId`, `dataLancamento`, `dataEmissao`, `moedaId`, `dataValidade`, `status`, `statusAprovacao`, `tipoAdiantamentoId`, `percentualComissao`, `cotacaoMoeda`, `vendedorId`, `especieId`

**`PUT` Editar — body fields:** `empresaId`, `clienteId`, `documento`, `valor`, `meioPagamentoId`, `operacaoFinanceiraId`, `contaOrigemId`, `contaDestinoId`, `historicoContabilId`, `dataLancamento`, `dataEmissao`, `moedaId`, `dataValidade`, `status`, `statusAprovacao`, `tipoAdiantamentoId`, `percentualComissao`, `cotacaoMoeda`, `vendedorId`, `especieId`

---

### Condições de Pagamento

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/financeiro/condicaopagamento` | Listar | MeioPagamentoId, MeioPagamentoNome, QuantidadeParcelas, QuantidadeParcelasTef, CodigoMarketplace, De |
| `GET` | `/v1/financeiro/condicaopagamento/{id}` | Obter | `id`(path) |

**`POST` Cadastrar — body fields:** `tipoPagamento`, `empresaGrupoId`, `nome`, `abreviatura`, `meioPagamentoId`, `codigoNfe`, `enviarNfe`, `lancamentoPermitido`, `dataGerarParcelas`, `percentualOperadoraCartao`, `vencimentoFimSemana`, `exibirPdv`, `enviarECF`, `imprimirConfissaoDivida`, `condicaoEspecial`, `informarTefPos`, `nomePdv`, `exibeAutorizacaoPagamento`, `exibeAutorizacaoAdiantamento`, `entradaAntecipada`

---

### Contas à Pagar

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/financeiro/contapagar` | Listar | Id, FornecedorId, Documento, DataEmissaoInicial, DataEmissaoFinal, Page, PageSize |
| `PUT` | `_see description_` | Editar | `id`(path) |
| `GET` | `/v1/financeiro/contapagar/consulta` | Consultar | Id, FornecedorId, Documento, VencimentoInicial, VencimentoFinal |
| `GET` | `/v1/financeiro/contapagar/{tituloId}/parcela` | Listar Parcelas | `tituloId`(path), Page, PageSize |
| `GET` | `/v1/financeiro/contapagar/{tituloId}/baixa` | Listar Baixas | `tituloId`(path), Page, PageSize |

**`POST` Cadastrar — body fields:** `empresaId`, `fornecedorId`, `documento`, `dataEmissao`, `dataEntrada`, `condicaoPagamentoId`, `operacaoFinanceiraId`, `moedaId`, `valor`, `dataCompetencia`, `pessoaCompraId`, `especieId`, `contaContabilCreditoId`, `historicoId`, `contaContabilDespesaId`, `historicoDespesaId`, `centroCustoId`, `projetoExecucaoTarefaItemId`, `statusAprovacao`, `status`

**`PUT` Editar — body fields:** `empresaId`, `fornecedorId`, `documento`, `dataEmissao`, `dataEntrada`, `condicaoPagamentoId`, `operacaoFinanceiraId`, `moedaId`, `valor`, `dataCompetencia`, `pessoaCompraId`, `especieId`, `contaContabilCreditoId`, `historicoId`, `contaContabilDespesaId`, `historicoDespesaId`, `centroCustoId`, `projetoExecucaoTarefaItemId`, `statusAprovacao`, `status`

---

### Contas à Receber

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/financeiro/contareceber` | Listar | Id, ClienteId, Documento, CodigoImportacao, DataEmissaoInicial, DataEmissaoFinal, Page, PageSize |
| `PUT` | `_see description_` | Editar | `id`(path) |
| `POST` | `/v1/financeiro/contareceber/{tituloId}/parcela` | Cadastrar Parcela | `tituloId`(path) |
| `GET` | `/v1/financeiro/contareceber/{tituloId}/parcela` | Listar Parcelas | `tituloId`(path), Page, PageSize |
| `POST` | `/v1/financeiro/contareceber/importacao/{tituloCodigoImportacao}/parcela` | Cadastrar Parcela (Cód. Importação) | `tituloCodigoImportacao`(path) |
| `GET` | `/v1/financeiro/contareceber/importacao/{tituloCodigoImportacao}/parcela` | Listar Parcelas (Cód. Importação) | `tituloCodigoImportacao`(path), Page, PageSize |
| `PATCH` | `/v1/financeiro/contareceber/{tituloId}/parcela/{id}` | Editar Parcela | `tituloId`(path), `id`(path) |
| `GET` | `/v1/financeiro/contareceber/{tituloId}/baixa` | Listar Baixas | `tituloId`(path), Page, PageSize |
| `POST` | `/v1/financeiro/contareceber/{tituloId}/baixa/parcela/{tituloParcelaId}` | Baixar Parcela | `tituloParcelaId`(path), `tituloId`(path) |
| `POST` | `/v1/financeiro/contareceber/importacao/{tituloCodigoImportacao}/baixa/parcela` | Baixar Parcela (Cód. Importação) | `tituloCodigoImportacao`(path) |
| `POST` | `/v1/financeiro/contareceber/{tituloId}/extorno/parcela/{tituloParcelaId}` | Extornar Parcela | `tituloParcelaId`(path), `tituloId`(path) |
| `POST` | `/v1/financeiro/contareceber/importacao/{tituloCodigoImportacao}/extorno/parcela` | Extornar Parcela (Cód. Importação) | `tituloCodigoImportacao`(path) |
| `GET` | `/v1/financeiro/contareceber/consulta` | Consultar | Id, ClienteId, Documento, VencimentoInicial, VencimentoFinal |

**`POST` Cadastrar — body fields:** `empresaId`, `clienteId`, `documento`, `dataEmissao`, `dataEntrada`, `condicaoPagamentoId`, `operacaoFinanceiraId`, `moedaId`, `especieId`, `valor`, `dataCompetencia`, `codigoImportacao`, `pessoaVendaId`, `contaContabilCreditoId`, `historicoId`, `contaContabilDespesaId`, `historicoDespesaId`, `centroCustoId`, `projetoExecucaoTarefaItemId`, `statusAprovacao`

**`PUT` Editar — body fields:** `empresaId`, `clienteId`, `documento`, `dataEmissao`, `dataEntrada`, `condicaoPagamentoId`, `operacaoFinanceiraId`, `moedaId`, `especieId`, `valor`, `dataCompetencia`, `codigoImportacao`, `pessoaVendaId`, `contaContabilCreditoId`, `historicoId`, `contaContabilDespesaId`, `historicoDespesaId`, `centroCustoId`, `projetoExecucaoTarefaItemId`, `statusAprovacao`

**`POST` Cadastrar Parcela — body fields:** `vencimento`, `valor`, `condicaoPagamentoId`, `previsaoPagamento`, `cotacaoMoeda`, `percentualComissao`, `vendedorId`, `portadorId`, `codigoImportacao`, `complemento`, `observacao`, `observacaoCobranca`, `observacaoInterna`

**`POST` Cadastrar Parcela (Cód. Importação) — body fields:** `vencimento`, `valor`, `condicaoPagamentoId`, `previsaoPagamento`, `cotacaoMoeda`, `percentualComissao`, `vendedorId`, `portadorId`, `codigoImportacao`, `complemento`, `observacao`, `observacaoCobranca`, `observacaoInterna`

**`PATCH` Editar Parcela — body fields:** `vencimento`, `valor`, `condicaoPagamentoId`, `previsaoPagamento`, `cotacaoMoeda`, `percentualComissao`, `vendedorId`, `codigoImportacao`, `complemento`, `observacao`, `observacaoCobranca`

**`POST` Baixar Parcela — body fields:** `data`, `contaContabilId`, `historicoId`, `meioPagamentoId`, `valor`, `chequeId`, `valorJuros`, `valorMulta`, `valorDesconto`, `taxaOperadoraCartao`, `observacaoInterna`, `complemento`

**`POST` Baixar Parcela (Cód. Importação) — body fields:** `data`, `contaContabilId`, `historicoId`, `meioPagamentoId`, `valor`, `chequeId`, `valorJuros`, `valorMulta`, `valorDesconto`, `taxaOperadoraCartao`, `observacaoInterna`, `complemento`

**`POST` Extornar Parcela — body fields:** `json`

**`POST` Extornar Parcela (Cód. Importação) — body fields:** `json`

---

### Contratos de Serviços

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/contratos/contratoservico` | Cadastrar | — |
| `GET` | `/v1/contratos/contratoservico` | Listar | Id, Descricao, TipoContratoId, EstabelecimentoId, PessoaId, Page, PageSize |
| `POST` | `/v1/contratos/contratoservico/{contratoId}/valorfixo` | Cadastrar Valor Fixo | `contratoId`(path) |
| `GET` | `/v1/contratos/contratoservico/{contratoId}/valorfixo` | Listar Valores Fixos | `contratoId`(path), Page, PageSize |
| `PATCH` | `/v1/contratos/contratoservico/{contratoId}/valorfixo/{id}` | Editar Valor Fixo | `contratoId`(path), `id`(path) |
| `POST` | `/v1/contratos/contratoservico/{contratoId}/valorvariavel` | Cadastrar Valor Variável | `contratoId`(path) |
| `GET` | `/v1/contratos/contratoservico/{contratoId}/valorvariavel` | Listar Valor Variável | `contratoId`(path), Page, PageSize |
| `PATCH` | `/v1/contratos/contratoservico/{contratoId}/valorvariavel/{id}` | Editar Valor Variável | `contratoId`(path), `id`(path) |

**`POST` Cadastrar — body fields:** `descricao`, `estabelecimentoId`, `pessoaId`, `condicaoPagamentoId`, `emissao`, `inicioFaturamento`, `inicio`, `valor`, `periodicidade`, `reajusteAutomatico`, `descontoAdimplencia`, `final`, `tipoContratoId`, `slaId`, `projetoId`, `municipioPrestacaoId`, `bancoHoras`, `dataBancoHoras`, `valorHora`, `totalHorasValor`

**`POST` Cadastrar Valor Fixo — body fields:** `produtoId`, `inicioFaturamento`, `quantidade`, `valor`, `total`, `descricaoDetalhadaNFe`, `municipioPrestacaoId`, `separarFaturamento`, `finalFaturamento`, `fornecedorId`, `clienteId`, `condicaoPagamentoId`, `vendedorId`, `operacaoFiscalId`, `percentualComissao`, `diaVencimento`, `periodicidadeFaturamento`, `observacoesNf`, `observacoes`

**`PATCH` Editar Valor Fixo — body fields:** `produtoId`, `descricaoDetalhadaNFe`, `municipioPrestacaoId`, `diaVencimento`, `condicaoPagamentoId`, `vendedorId`, `operacaoFiscalId`, `observacoes`, `observacoesNf`, `quantidade`, `valor`, `percentualComissao`, `periodicidadeFaturamento`, `separarFaturamento`, `inicioFaturamento`, `finalFaturamento`, `clienteId`, `fornecedorId`

**`POST` Cadastrar Valor Variável — body fields:** `produtoId`, `inicioFaturamento`, `quantidade`, `valor`, `total`, `diaVencimento`, `percentualComissao`, `condicaoPagamentoId`, `fornecedorId`, `descricaoDetalhadaNFe`, `operacaoFiscalId`, `vendedorId`, `observacoesNf`, `observacoes`

**`PATCH` Editar Valor Variável — body fields:** `produtoId`, `descricaoDetalhadaNFe`, `diaVencimento`, `condicaoPagamentoId`, `vendedorId`, `observacoes`, `observacoesNf`, `ordensServicos`, `quantidade`, `valor`, `percentualComissao`, `inicioFaturamento`, `clienteId`, `fornecedorId`, `operacaoFiscalId`

---

### CRM — Contas

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/crm/conta` | Listar | Id, TipoConta, RazaoSocial, Fantasia, CpfCnpj, MunicipioNome, Ativo, Bloqueado, Page, PageSize |

**`POST` Cadastrar — body fields:** `empresaGrupoId`, `tipoConta`, `tipoPessoaInt`, `razaoSocial`, `fantasia`, `cpfCnpj`, `inscricaoEstadual`, `telefone`, `telefoneAdicional`, `site`, `email`, `dataAbertura`, `status`, `clienteId`, `tipoPessoaId`, `numeroExterior`, `grupoEconomicoId`, `porteId`, `rating`, `numeroFuncionarios`

---

### CRM — Oportunidades

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/crm/oportunidade` | Cadastrar | — |
| `GET` | `/v1/crm/oportunidade` | Listar | Id, ContatoPessoaId, ContatoPessoaNome, ModalidadeNegocioId, ModalidadeNegocioNome, OrigemId, Origem |
| `POST` | `/v1/crm/oportunidade/{oportunidadeId}/responsavel` | Cadastrar Responsável | `oportunidadeId`(path) |
| `GET` | `/v1/crm/oportunidade/{oportunidadeId}/responsavel` | Listar Responsáveis | `oportunidadeId`(path), Page, PageSize |
| `POST` | `/v1/crm/oportunidade/{oportunidadeId}/acao` | Cadastrar Ação | `oportunidadeId`(path) |
| `GET` | `/v1/crm/oportunidade/{oportunidadeId}/acao` | Listar Ações | `oportunidadeId`(path), Page, PageSize |
| `POST` | `/v1/crm/oportunidade/{oportunidadeId}/concorrente` | Cadastrar Concorrente | `oportunidadeId`(path) |
| `GET` | `/v1/crm/oportunidade/{oportunidadeId}/concorrente` | Listar Concorrentes | `oportunidadeId`(path), Page, PageSize |
| `POST` | `/v1/crm/oportunidade/{oportunidadeId}/comentario` | Cadastrar Comentário | `oportunidadeId`(path) |
| `GET` | `/v1/crm/oportunidade/{oportunidadeId}/comentario` | Listar Comentários | `oportunidadeId`(path), Page, PageSize |
| `POST` | `/v1/crm/oportunidade/{oportunidadeId}/anexo` | Cadastrar Anexo | `oportunidadeId`(path) |
| `GET` | `/v1/crm/oportunidade/{oportunidadeId}/anexo` | Listar Anexos | `oportunidadeId`(path), Page, PageSize |
| `GET` | `/v1/crm/oportunidade/{oportunidadeId}/anexo/{anexoId}` | Obter Anexo | `oportunidadeId`(path), `anexoId`(path) |

**`POST` Cadastrar — body fields:** `empresaGrupoId`, `dataAbertura`, `horaAbertura`, `descricao`, `contaId`, `tipoOportunidadeId`, `origemId`, `etapaNegociacao`, `previsaoFechamento`, `dataAcompanhamento`, `efetivacaoFechamento`, `previsaoEntrega`, `efetivacaoEntrega`, `valorPrevisto`, `valorFechado`, `vendedorId`, `modalidadeNegocioId`, `contatoPessoaId`, `oportunidadeStatusId`, `finalizarAgendamento`

**`POST` Cadastrar Responsável — body fields:** `usuariosId`, `of`

**`POST` Cadastrar Ação — body fields:** `data`, `hora`, `previsaoFechamento`, `tipoAcaoId`, `modificaOportunidade`, `valorPrevisto`, `arquivo`, `etapaNegociacao`, `contaContatoId`, `valorFechado`, `tarefaAgenda`, `probabilidade`, `numeroProposta`, `numeroPedido`, `efetivacaoFechamento`, `previsaoEntrega`, `efetivacaoEntrega`, `motivoPerdaId`, `motivoFechamentoId`, `orcamentoFechamentoId`

**`POST` Cadastrar Concorrente — body fields:** `concorrenteId`, `pontosFortes`, `pontosFracos`, `observacoes`

**`POST` Cadastrar Comentário — body fields:** `dataHora`, `hora`, `usuarioId`, `comentario`

**`POST` Cadastrar Anexo — body fields:** `nome`, `arquivo`

---

### CRM — Orçamentos

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/crm/orcamento` | Listar | Id, ClienteId, ClienteNome, Status, DataEmissaoInicial, DataEmissaoFinal, NumeroProposta, StatusLanc |
| `GET` | `/v1/crm/orcamento/{orcamentoId}/imprimir` | Imprimir | `orcamentoId`(path), Tipos, of |
| `GET` | `/v1/crm/orcamento/{orcamentoId}/produto` | Listar Produtos | `orcamentoId`(path), Page, PageSize |
| `GET` | `/v1/crm/orcamento/{orcamentoId}/servico` | Listar Serviços | `orcamentoId`(path), Page, PageSize |
| `GET` | `/v1/crm/orcamento/{orcamentoId}/vendedor` | Listar Vendedores | `orcamentoId`(path), Page, PageSize |

---

### Endereços

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/configuracoes/bairro` | Cadastrar Bairro | — |
| `GET` | `/v1/configuracoes/bairro` | Listar Bairros | MunicipioId, Id, Nome, Page, PageSize |
| `POST` | `/v1/configuracoes/municipio` | Cadastrar Municipio | — |
| `GET` | `/v1/configuracoes/municipio` | Listar Municipio | EstadoId, EstadoUf, Ibge, Id, Nome, Page, PageSize |
| `GET` | `/v1/configuracoes/estado` | Listar Estados | Uf, PaisId, PaisNome, Id, Nome, Page, PageSize |
| `GET` | `/v1/configuracoes/endereco` | Listar Endereços | TipoEndereco, Cep, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSize |

**`POST` Cadastrar Bairro — body fields:** `nome`, `municipioId`

**`POST` Cadastrar Municipio — body fields:** `nome`, `estadoId`, `ibge`, `cep`, `siafi`, `tributacaoNfse`, `codigoEstadual`, `aliquotaISS`, `estrangeira`, `comarcaId`, `enviaMunicipioPrestacao`

---

### Equipamentos

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/estoque/equipamento` | Listar | Id, Nome, Apelido, CodigoIdentificacaoInterno, CodigoBarras, MarcaId, GrupoEstoqueId, FamiliaId, Cat |
| `GET` | `/v1/estoque/equipamento/pessoa/{pessoaId}` | Listar Equipamentos Pessoa | `pessoaId`(path), Page, PageSize |

**`POST` Cadastrar — body fields:** `origem`, `nome`, `apelido`, `ncm`, `codigoTipoSped`, `unidadeId`, `familiaId`, `grupoEstoqueId`, `codigoGenero`, `codigoMarketPlace`, `referenciaFabricante`, `codigoSimilaridade`, `codigoImportacao`, `codigoBarras`, `capacidadeNominal`, `bateria`, `codigoEspecificadorCEST`, `categoriaId`, `precoVenda`, `precoVendaMinimo`

---

### Estoque

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/estoque/produto/{produtoId}/estoque` | Consultar Por Produto | `produtoId`(path), EstabelecimentoId, EmpresaGrupoId, StatusAprovacao, Page, PageSize |
| `GET` | `/v1/estoque/movimentacaofuturo` | Consultar Movimentação Estoque Futuro | DataInicial, DataFinal, EmpresaGrupoId, EmpresaId, ProdutoServicoId, CodigoIdentificacaoInterno, Pes |
| `GET` | `/v1/estoque/movimentacaofuturodisponivel` | Consultar Movimentação Estoque Futuro Disponível | QuantidadeRequerida, EmpresaGrupoId, EmpresaId, ProdutoServicoId, ProdutoServicoIds, of, CodigoIdent |
| `GET` | `/v1/estoque/tabelaprecoprodutosaldo` | Consultar Tabela Preços/Saldo | ProdutoId, ProdutoNome, ProdutoApelido, CodigoIdentificacaoInterno, of, TabelaPrecoId, GrupoEstoqueI |
| `GET` | `/v1/estoque/estoquedisponivelestabelecimento` | Consultar Por Produto/Estabelecimento (Disponível) | EmpresaId, ProdutosIds, of, Page, PageSize |

---

### Follow Up (Clientes/Contas)

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/crm/pessoa/{pessoaId}/followup` | Cadastrar | `pessoaId`(path) |
| `GET` | `/v1/crm/pessoa/{pessoaId}/followup` | Listar | `pessoaId`(path), Page, PageSize |

**`POST` Cadastrar — body fields:** `usuarioId`, `dataHora`, `tipoAcaoId`, `observacao`, `contatoId`, `documentoFiscalId`, `latitude`, `longitude`

---

### Fornecedores

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/configuracoes/fornecedor` | Listar | Id, RazaoSocial, Fantasia, CpfCnpj, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSize |
| `GET` | `/v1/configuracoes/fornecedor/{id}` | Obter | `id`(path) |
| `GET` | `/v1/configuracoes/fornecedor/{fornecedorId}/endereco` | Listar Endereços | `fornecedorId`(path), TipoEndereco, Cep, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSiz |

**`POST` Cadastrar — body fields:** `tipoPessoaId`, `classificacaoId`, `cpfCnpj`, `razaoSocial`, `cep`, `logradouro`, `numero`, `bairroId`, `bairroNome`, `municipioId`, `municipioNome`, `uf`, `municipioIbge`, `fantasia`, `complemento`, `letra`, `apelido`, `tipoContribuinte`, `regimeTributario`, `operacaoConsumidorNFe`

---

### Fretes

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/configuracoes/frete` | Listar | Id, Nome, Page, PageSize |

---

### Funcionarios

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/configuracoes/funcionario` | Cadastrar | — |
| `GET` | `/v1/configuracoes/funcionario` | Listar | Id, RazaoSocial, Fantasia, CpfCnpj, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSize |

**`POST` Cadastrar — body fields:** `tipoPessoa`, `cpfCnpj`, `razaoSocial`, `cep`, `logradouro`, `numero`, `bairroId`, `municipioId`, `fantasia`, `complemento`, `letra`, `telefone`, `email`, `inscricaoEstadual`

---

### Logs

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/logs/operacao` | Listar Log de Operações | Id, Tabela, CriadoEmInicial, CriadoEmFinal, RotuloCampo, ValorAnterior, ValorAtual, GeradoPor, Page, |

---

### Meios de Pagamento

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/financeiro/meiopagamento` | Listar | Id, Nome, Page, PageSize |

---

### Montagem de Carga

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/montagemcarga` | Listar | Id, EmpresaGrupoId, Status, DescricaoCarga, DataCarregamentoInicial, DataCarregamentoFinal, DataAtua |
| `GET` | `/v1/faturamento/montagemcarga/{montagemCargaId}/item` | Listar Itens por ID Carga | `montagemCargaId`(path) |
| `GET` | `/v1/faturamento/montagemcarga/item` | Listar Itens | Id, MontagemCargaId, PedidoId, ProdutoId, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSi |

---

### NCM/IBPT

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/estoque/ncm` | Listar | Id, Descricao, Ncm, Excecao, Page, PageSize |

---

### Notas Fiscais — Compra

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/compras/notafiscal` | Listar | Id, PessoaId, FornecedorCnpj, Documento, ChaveNfe, Status, EmissaoInicial, EmissaoFinal, Page, PageS |
| `POST` | `_see description_` | Cadastrar Produto | `documentoFiscalId`(path) |
| `GET` | `/v1/compras/notafiscal/{documentoFiscalId}/produto` | Listar Produtos | `documentoFiscalId`(path), Page, PageSize |
| `POST` | `/v1/compras/notafiscal/{documentoFiscalId}/servico` | Cadastrar Serviço | `documentoFiscalId`(path) |
| `GET` | `/v1/compras/notafiscal/{documentoFiscalId}/servico` | Listar Serviços | `documentoFiscalId`(path), Page, PageSize |

**`POST` Cadastrar — body fields:** `empresaId`, `pessoaId`, `tipoCompraId`, `emissao`, `lancamento`, `freteId`, `condicaoPagamentoId`, `sintegraId`, `documento`, `serie`, `especieDocumento`, `especieId`, `status`, `participanteId`, `moedaId`, `municipioOrigemId`, `municipioDestinoId`, `chaveNfe`, `imovelRuralId`, `documentoFiscalSaidaId`

**`POST` Cadastrar Produto — body fields:** `produtoId`, `operacaoFiscalId`, `destinoEstoqueId`, `quantidade`, `valorUnitario`, `contaContabilId`, `centroCustoId`, `projetoExecucaoId`, `projetoExecucaoTarefaItemId`, `destinoEstoqueTerceiroId`, `fatorConversao`, `quantidadeConversao`, `valorUnitarioConversao`, `unidadeFatorConversaoId`, `vendedorId`, `custoOperacao`, `valorFreteRateio`, `valorFreteAPagarRateio`, `outrasDespesas`, `custoDolar`

**`POST` Cadastrar Serviço — body fields:** `produtoId`, `operacaoFiscalId`, `quantidade`, `valorUnitario`, `contaContabilId`, `centroCustoId`, `vendedorId`, `projetoExecucaoId`, `projetoExecucaoTarefaItemId`, `ordemProducaoId`, `operacaoFinanceiraId`, `aliquotaIss`, `aliquotaInss`, `aliquotaIrrf`, `aliquotaPis`, `aliquotaCofins`, `aliquotaCsll`, `codigoTributarioIbsCbs`, `aliquotaCbs`, `percentualReducaoCbs`

---

### Notas Fiscais — Outras

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/notafiscaloutra` | Listar | Id, PessoaId, PessoaNome, PessoaCnpj, Documento, ChaveNfe, Status, EmissaoInicial, EmissaoFinal, Pag |
| `GET` | `/v1/faturamento/notafiscaloutra/{documentoFiscalId}/produto` | Listar Produtos | `documentoFiscalId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/notafiscaloutra/{documentoFiscalId}/servico` | Listar Serviços | `documentoFiscalId`(path), Page, PageSize |

---

### Notas Fiscais — Venda

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/notafiscalvenda` | Listar | Id, PessoaId, PessoaNome, PessoaCnpj, Documento, ChaveNfe, Status, EmissaoInicial, EmissaoFinal, Usu |
| `PATCH` | `/v1/faturamento/notafiscalvenda/{documentoFiscalId}` | Editar | `documentoFiscalId`(path) |
| `GET` | `/v1/faturamento/notafiscalvenda/{documentoFiscalId}/produto` | Listar Produtos | `documentoFiscalId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/notafiscalvenda/{documentoFiscalId}/servico` | Listar Serviços | `documentoFiscalId`(path), Page, PageSize |
| `POST` | `/v1/faturamento/notafiscalvenda/{documentoFiscalId}/faturar` | Faturar | `documentoFiscalId`(path) |
| `POST` | `/v1/faturamento/notafiscalvenda/{documentoFiscalId}/cancelar` | Cancelar | `documentoFiscalId`(path) |
| `POST` | `/v1/faturamento/notafiscalvenda/importar` | Importar | — |
| `GET` | `/v1/faturamento/notafiscalvenda/{documentoFiscalId}/danfe` | Imprimir Danfe | `documentoFiscalId`(path) |
| `GET` | `/v1/faturamento/notafiscalvenda/centrocusto` | Centro de Custos | Id, DocumentoFiscalId, CentroCustoId, CentroCustoClassificacao, Natureza, OperacaoFinanceiraId, Data |

**`PATCH` Editar — body fields:** `municipioPrestacaoId`, `emissao`

**`POST` Faturar — body fields:** `json`

**`POST` Cancelar — body fields:** `motivo`

**`POST` Importar — body fields:** `dataLote`, `documentos`

---

### Números de Série

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/numeroserie` | Listar | ProdutoId, ProdutoNome, NumeroSerie, PedidoId, PedidoItemId, OrdemServicoSaidaId, OrdemServicoItemId |

---

### Operações Fiscais

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/configuracoes/operacaofiscal` | Listar | CodigoImportacao, TipoOperacao, TipoEmissor, EmpresaGrupoNome, CfopComInscricaoEstadualDentro, CfopC |

---

### Orçamentos (Faturamento)

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/orcamento` | Listar | Id, ClienteId, ClienteNome, Status, TipoId, TabelaPrecoId, ContratoId, EmissaoInicial, EmissaoFinal, |
| `GET` | `/v1/faturamento/orcamento/{orcamentoId}/produto` | Listar Produtos | `orcamentoId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/orcamento/{orcamentoId}/servico` | Listar Serviços | `orcamentoId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/orcamento/{orcamentoId}/parcela` | Listar Parcelas | `orcamentoId`(path), Page, PageSize |

---

### Ordens de Compra

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/compras/ordemcompra` | Listar | Id, ClienteId, DataEmissaoInicial, DataEmissaoFinal, Page, PageSize |
| `POST` | `/v1/compras/ordemcompra/{ordemCompraId}/item` | Cadastrar Item | `ordemCompraId`(path) |
| `GET` | `/v1/compras/ordemcompra/{ordemCompraId}/item` | Listar Itens | `ordemCompraId`(path), Page, PageSize |
| `POST` | `/v1/compras/ordemcompra/{ordemCompraId}/parcela` | Cadastrar Parcela | `ordemCompraId`(path) |
| `GET` | `/v1/compras/ordemcompra/{ordemCompraId}/parcela` | Listar Parcelas | `ordemCompraId`(path), Page, PageSize |
| `POST` | `/v1/compras/ordemcompra/{ordemCompraId}/cancelar` | Cancelar | `ordemCompraId`(path) |

**`POST` Cadastrar — body fields:** `empresaId`, `status`, `emissao`, `fornecedorId`, `funcionarioId`, `freteId`, `condicaoPagamentoId`, `transportadorId`, `tipoOrdemCompraId`, `clienteId`, `contatoId`, `contatoDigitado`, `solicitanteId`, `moedaId`, `contratoId`, `contratoFornecedorId`, `projetoExecucaoId`, `projetoExecucaoItemId`, `unidadeNegocioId`, `grupoEconomicoId`

**`POST` Cadastrar Item — body fields:** `produtoId`, `unidadeId`, `quantidade`, `quantidadeComprada`, `valorUnitario`, `operacaoFiscalId`, `moedaId`, `referenciaFabricante`, `codigoProdutoFornecedor`, `descricaoLivre`, `cotacaoMoeda`, `valorDesconto`, `aliquotaICMS`, `valorICMS`, `aliquotaIcmsSt`, `aliquotaMva`, `valorICMSST`, `aliquotaIPI`, `valorIPI`, `aliquotaPis`

**`POST` Cadastrar Parcela — body fields:** `vencimento`, `valor`, `condicaoPagamentoId`

**`POST` Cancelar — body fields:** `motivoCancelamento`

---

### Ordens de Produção

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/pcpproducao/tipoordemproducao` | Listar Tipos | Id, Nome, Page, PageSize |
| `POST` | `/v1/pcpproducao/ordemproducao` | Cadastrar | — |
| `GET` | `/v1/pcpproducao/ordemproducao` | Listar | Id, TipoOrdemProducaoId, StatusFluxoId, ProdutoId, PedidoId, Status, Page, PageSize |
| `GET` | `/v1/pcpproducao/ordemproducao/{id}` | Obter | `id`(path) |
| `POST` | `/v1/pcpproducao/ordemproducao/{ordemProducaoId}/item` | Cadastrar Item | `ordemProducaoId`(path) |
| `GET` | `/v1/pcpproducao/ordemproducao/{ordemProducaoId}/item` | Listar Itens | `ordemProducaoId`(path), Page, PageSize |
| `PATCH` | `/v1/pcpproducao/ordemproducao/{ordemProducaoId}/statusfluxo` | Alterar Status (Fluxo) | `ordemProducaoId`(path) |
| `POST` | `/v1/pcpproducao/ordemproducao/{ordemProducaoId}/cancelar` | Cancelar | `ordemProducaoId`(path) |

**`POST` Cadastrar — body fields:** `tipoOrdemProducaoId`, `produtoId`, `estabelecimentoId`, `destinoEstoqueId`, `usuarioId`, `quantidade`, `emissao`, `inicio`, `vencimento`, `statusFluxoId`, `status`, `gerarNotaRemessa`, `centroCustoId`, `pedidoId`, `clienteId`, `quantidadeNecessaria`, `versao`, `encerramento`, `projetoId`, `etapaId`

**`POST` Cadastrar Item — body fields:** `tipoComposicao`, `descricao`, `produtoId`, `localEstoqueId`, `recursoId`, `componenteId`, `servicoId`, `quantidade`, `quantidadeEngenharia`, `indicePerda`, `custo`

**`PATCH` Alterar Status (Fluxo) — body fields:** `statusFluxoId`

**`POST` Cancelar — body fields:** `json`

---

### Ordens de Serviço — Assist. Técnica

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/assistenciatecnica/ordemservico` | Listar | Id, ClienteId, ResponsavelTecnicoId, TipoId, EmissaoInicial, EmissaoFinal, DataAtualizacaoInicial, D |
| `PUT` | `_see description_` | Editar | `id`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservicocompleta` | Listar Completa | Id, ClienteId, ResponsavelTecnicoId, TipoId, EmissaoInicial, EmissaoFinal, DataAtualizacaoInicial, D |
| `PATCH` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/statusfluxo` | Alterar Status (Fluxo) | `ordemServicoId`(path) |
| `POST` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/anexo` | Cadastrar Anexo | `ordemServicoId`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/anexo` | Listar Anexos | `ordemServicoId`(path), Page, PageSize |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/anexo/{anexoId}` | Obter Anexo | `ordemServicoId`(path), `anexoId`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/equipamento` | Listar Equipamentos | `ordemServicoId`(path), Page, PageSize |
| `POST` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/equipamento` | Cadastrar Equipamento | `ordemServicoId`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/manutencao` | Listar Manutenções | `ordemServicoId`(path), Page, PageSize |
| `POST` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/manutencao` | Cadastrar Manutenção | `ordemServicoId`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/produto` | Listar Itens Produtos | `ordemServicoId`(path), EstaExcluido, Id, Nome, Page, PageSize |
| `POST` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/produto` | Cadastrar Item Produto | `ordemServicoId`(path) |
| `PATCH` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/produto/{ordemServicoItemId}` | Editar Item Produto | `ordemServicoId`(path), `ordemServicoItemId`(path) |
| `DELETE` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/produto/{ordemServicoItemId}` | Remover Item Produto | `ordemServicoId`(path), `ordemServicoItemId`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/servico` | Listar Itens Serviços | `ordemServicoId`(path), Page, PageSize |
| `POST` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/servico` | Cadastrar Item Serviço | `ordemServicoId`(path) |
| `PATCH` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/servico/{ordemServicoItemId}` | Editar Item Serviço | `ordemServicoId`(path), `ordemServicoItemId`(path) |
| `DELETE` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/servico/{ordemServicoItemId}` | Remover Item Serviço | `ordemServicoId`(path), `ordemServicoItemId`(path) |
| `POST` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/apontamentohora` | Cadastrar Apontamentos de Hora | `ordemServicoId`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/apontamentohora` | Listar Apontamentos de Hora | `ordemServicoId`(path), Page, PageSize |
| `POST` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/checklistresposta` | Cadastrar Respostas da Checklist | `ordemServicoId`(path) |
| `GET` | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/checklistpergunta` | Listar Perguntas da Checklist | `ordemServicoId`(path), Page, PageSize |
| `GET` | `/v1/assistenciatecnica/ordemservico/checklistcompleta` | Listar Perguntas da ChecklistCompleta | Page, PageSize |
| `POST` | `/v1/assistenciatecnica/ordemservico/situacao` | Cadastrar Situação | — |
| `GET` | `/v1/assistenciatecnica/ordemservico/situacao` | Listar Situações | Id, Nome, Page, PageSize |

**`POST` Cadastrar — body fields:** `tipoId`, `clienteId`, `emissao`, `dataEntregaPrevista`, `dataEntrega`, `condicaoPagamentoId`, `funcionarioId`, `numeroSequencia`, `dataFaturamento`, `enderecoEntregaId`, `enderecoRetiradaId`, `responsavelId`, `revendaContratoId`, `projetoId`, `slaId`, `tipoAtendimentoId`, `modalidadeAtendimentoId`, `origemId`, `contato`, `situacaoId`

**`PUT` Editar — body fields:** `tipoId`, `clienteId`, `emissao`, `dataEntregaPrevista`, `dataEntrega`, `condicaoPagamentoId`, `funcionarioId`, `numeroSequencia`, `dataFaturamento`, `enderecoEntregaId`, `enderecoRetiradaId`, `responsavelId`, `revendaContratoId`, `projetoId`, `slaId`, `tipoAtendimentoId`, `modalidadeAtendimentoId`, `origemId`, `contato`, `situacaoId`

**`PATCH` Alterar Status (Fluxo) — body fields:** `statusFluxoId`

**`POST` Cadastrar Anexo — body fields:** `nome`, `arquivo`

**`POST` Cadastrar Equipamento — body fields:** `equipamentoId`, `equipamentoProdutoId`, `horimetro`, `dataHorimetro`, `horimetroDois`, `dataHorimetroDois`, `horimetroTres`, `dataHorimetroTres`, `box`, `numeroSerie`, `numeroFrota`, `dataInstalacao`, `diasGarantia`, `anoFabricacao`, `torre`, `marcaId`, `defeitoId`, `tecnicoId`, `problemaId`, `causaProblemaId`

**`POST` Cadastrar Manutenção — body fields:** `veiculoPessoaId`, `motoristaNome`, `kmAtual`, `box`, `dataUltimaTrocaOleo`, `kmUltimaTroca`, `kmRodado`, `quantidadeCombustivel`, `condicaoEntrada`, `dataProximaTrocaOleo`, `avisoAntecedenciaTrocaOleo`, `observacoesTrocaOleo`, `dataProximaRevisao`, `avisoAntecedencia`, `observacoesRevisao`, `observacao`, `avarias`, `defeitos`, `laudo`, `recarregarEquipamento`

**`POST` Cadastrar Item Produto — body fields:** `produtoId`, `quantidade`, `valorUnitario`, `valorTotal`, `id`, `valorUnitarioDesconto`, `percentualDesconto`, `valorDesconto`, `descricaoDetalhadaNfe`, `destinoEstoqueId`, `situacaoItemId`, `observacaoInterna`, `observacao`

**`PATCH` Editar Item Produto — body fields:** `produtoId`, `quantidade`, `valorUnitario`, `valorTotal`, `valorUnitarioDesconto`, `percentualDesconto`, `valorDesconto`, `descricaoDetalhadaNfe`, `destinoEstoqueId`, `situacaoItemId`, `observacaoInterna`, `observacao`

**`POST` Cadastrar Item Serviço — body fields:** `servicoId`, `quantidade`, `valorUnitario`, `valorTotal`, `id`, `quantidadeHora`, `valorUnitarioDesconto`, `percentualDesconto`, `valorDesconto`, `descricaoDetalhadaNfe`, `responsavelTecnicoId`, `destinoEstoqueId`, `situacaoItemId`, `observacaoInterna`, `observacao`

**`PATCH` Editar Item Serviço — body fields:** `servicoId`, `quantidade`, `valorUnitario`, `valorTotal`, `valorUnitarioDesconto`, `percentualDesconto`, `valorDesconto`, `descricaoDetalhadaNfe`, `destinoEstoqueId`, `situacaoItemId`, `observacaoInterna`, `observacao`, `responsavelTecnicoId`

**`POST` Cadastrar Apontamentos de Hora — body fields:** `servicoId`, `funcionarioId`, `horaInicio`, `horaFim`, `totalHoras`, `descricaoServico`, `data`, `id`, `observacao`

**`POST` Cadastrar Respostas da Checklist — body fields:** `checklistPerguntaExecucaoRelacionadaId`, `observacao`, `avaliacaoNota`

**`POST` Cadastrar Situação — body fields:** `nome`

---

### Ordens de Serviço — Faturamento

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/faturamento/ordemservico` | Cadastrar | — |
| `GET` | `/v1/faturamento/ordemservico` | Listar | Id, ClienteId, TipoId, EmissaoInicial, EmissaoFinal, Status, Page, PageSize |

**`POST` Cadastrar — body fields:** `empresaId`, `clienteId`, `contatoPessoaId`, `emissao`, `dataLancamento`, `dataEntrega`, `dataEntregaPrevista`, `situacaoId`, `condicaoPagamentoId`, `municipioPrestacaoId`, `funcionarioId`, `responsavelTecnicoId`, `projetoExecucaoId`, `grupoEconomicoId`, `tipoId`, `veiculoManutencaoId`, `kmAtual`, `status`, `indicadorPresencaComprador`, `numeroSequencia`

---

### Pedidos — Faturamento Direto

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/pedidodireto/{pedidoId}/item` | Listar Itens | `pedidoId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/pedidodireto/{pedidoId}/servico` | Listar Serviços | `pedidoId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/pedidodireto/{pedidoId}/parcela` | Listar Parcelas | `pedidoId`(path), Page, PageSize |

---

### Pedidos — Padrão

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/faturamento/pedidopadrao` | Cadastrar Pedido | — |
| `GET` | `/v1/faturamento/pedidopadrao/{pedidoId}/item` | Listar Itens | `pedidoId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/pedidopadrao/{pedidoId}/volume` | Listar Volumes | `pedidoId`(path), Page, PageSize |
| `POST` | `/v1/faturamento/pedidopadrao/{pedidoId}/volume` | Cadastrar Volume | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedidopadrao/{pedidoId}/volume/gerar` | Gerar Etiqueta | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedidopadrao/{pedidoId}/item/embalar` | Embalar Item | `pedidoId`(path) |

**`POST` Cadastrar Pedido — body fields:** `tipoPedidoCadastroId`, `clienteId`, `condicaoPagamentoId`, `moedaId`, `emissao`, `dataFaturamento`, `contratoId`, `dataLancamento`, `contatoPessoaId`, `contato`, `funcionarioId`, `freteId`, `portadorId`, `operacaoFiscalId`, `projetoOrcamentoCrmId`, `cotacaoMoeda`, `observacao`

**`POST` Cadastrar Volume — body fields:** `volumeId`, `peso`, `pesoCadastro`

**`POST` Gerar Etiqueta — body fields:** `volumeId`, `quantidade`, `numeroInicial`

**`POST` Embalar Item — body fields:** `volumeCodigoBarras`, `produtoId`

---

### Pedidos — Rápido

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar Pedido | — |
| `GET` | `/v1/faturamento/pedido` | Listar Pedidos | Id, of, ClienteId, TipoId, DataEmissaoInicial, DataEmissaoFinal, Status, StatusLancamentoNome, of, C |
| `PATCH` | `/v1/faturamento/pedido/{id}` | Editar Pedido | `id`(path) |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/servico` | Cadastrar Serviço | `pedidoId`(path) |
| `GET` | `/v1/faturamento/pedido/{pedidoId}/servico` | Listar Serviços | `pedidoId`(path), Page, PageSize |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/produto` | Cadastrar Produto | `pedidoId`(path) |
| `GET` | `/v1/faturamento/pedido/{pedidoId}/produto` | Listar Produtos | `pedidoId`(path), Page, PageSize |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/parcela/gerar` | Gerar Parcelas | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/parcela` | Cadastrar Parcela | `pedidoId`(path) |
| `GET` | `/v1/faturamento/pedido/{pedidoId}/parcela` | Listar Parcelas | `pedidoId`(path), Page, PageSize |
| `PATCH` | `/v1/faturamento/pedido/{pedidoId}/statusfluxo` | Alterar Status (Fluxo) do Pedido | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/gerarordemproducao` | Gerar Ordem de Produção | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/faturarnotafiscal` | Faturar Nota Fiscal | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/simplesfatura` | Faturar Simples Fatura | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/cancelar` | Cancelar | `pedidoId`(path) |
| `POST` | `/v1/faturamento/pedido/{pedidoId}/anexo` | Cadastrar Anexo | `pedidoId`(path) |
| `GET` | `/v1/faturamento/pedido/{pedidoId}/anexo` | Listar Anexos | `pedidoId`(path), Page, PageSize |
| `GET` | `/v1/faturamento/pedido/{pedidoId}/anexo/{anexoId}` | Obter Anexo | `pedidoId`(path), `anexoId`(path) |
| `GET` | `/v1/faturamento/pedido/{pedidoId}/danfe` | Imprimir Danfe | `pedidoId`(path), Temp |
| `GET` | `/v1/faturamento/pedido/danfe/vinculada` | Imprimir Danfe (Vinculadas) | Id, CodigoMarketPlace, Temp, Page, PageSize |
| `GET` | `/v1/faturamento/pedido/danfe/boleto/vinculada` | Imprimir Danfe/Boletos (Vinculados) | Id, CodigoMarketPlace, Temp, Page, PageSize |
| `POST` | `/v1/faturamento/pedido/notafiscal/devolucao` | Devolução Nota Fiscal (Venda) | — |
| `POST` | `/v1/faturamento/pedido/desmontar` | Desmontar Pedido | — |
| `GET` | `/v1/faturamento/pedido/capacidadeseparacao` | Consultar Capacidade de Separação | EmpresaId, DataInicial, DataFinal, Page, PageSize |

**`POST` Cadastrar Pedido — body fields:** `empresaId`, `condicaoPagamentoId`, `tipoId`, `dataEmissao`, `clienteId`, `cliente`, `produtos`, `servicos`, `parcelas`, `comissoes`, `gerarNfFutura`, `freteId`, `valorFrete`, `transportadorId`, `quantidadeVolume`, `pesoLiquido`, `pesoBruto`, `vendedorId`, `destinatarioId`, `orcamentoCrmId`

**`PATCH` Editar Pedido — body fields:** `condicaoPagamentoId`, `transportadorId`, `quantidadeVolume`, `pesoLiquido`, `pesoBruto`

**`POST` Cadastrar Serviço — body fields:** `servicoId`, `quantidade`, `valorUnitario`, `valorTotal`, `valorDesconto`, `percentualDesconto`, `dataEntrega`, `observacao`

**`POST` Cadastrar Produto — body fields:** `produtoId`, `produto`, `quantidade`, `valorUnitario`, `valorTotal`, `classificacaoId`, `destinoEstoqueId`, `contratoId`, `valorDesconto`, `valorUnitarioDesconto`, `numeroItemPedido`, `codigoPedido`, `percentualDesconto`, `percentualComissao`, `dataEntrega`, `observacao`, `insumosProducao`

**`POST` Gerar Parcelas — body fields:** `condicaoPagamentoId`, `valor`, `dataTransacao`, `autenticacao`, `autorizacaoCartao`, `nsu`

**`POST` Cadastrar Parcela — body fields:** `condicaoPagamentoId`, `vencimento`, `valor`, `autenticacao`, `autorizacaoCartao`, `nsu`, `observacao`

**`PATCH` Alterar Status (Fluxo) do Pedido — body fields:** `statusFluxoId`

**`POST` Gerar Ordem de Produção — body fields:** `json`

**`POST` Faturar Nota Fiscal — body fields:** `json`

**`POST` Faturar Simples Fatura — body fields:** `json`

**`POST` Cancelar — body fields:** `motivo`

**`POST` Cadastrar Anexo — body fields:** `nome`, `arquivo`

**`POST` Devolução Nota Fiscal (Venda) — body fields:** `tipoDocumentoId`, `id`, `codigoMarketPlace`

**`POST` Desmontar Pedido — body fields:** `destinoEstoqueId`, `id`, `codigoMarketPlace`

---

### Plano de Contas

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/contabil/planoconta` | Listar | EhContaCaixa, Id, Nome, Page, PageSize |
| `GET` | `/v1/contabil/saldoconta` | Consultar Saldo Atual | ContaContabilIds, of, EmpresaGrupoId |

---

### Produtos

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar Produto | — |
| `GET` | `/v1/estoque/produto` | Listar Produtos | Id, Nome, Apelido, CodigoIdentificacaoInterno, CodigoBarras, AtivoEcommerce, Kit, Ids, of, IdsIntern |
| `PATCH` | `/v1/estoque/produto/{id}` | Editar | `id`(path) |
| `GET` | `/v1/estoque/produto/{produtoId}/imagem` | Listar Imagens Produto | `produtoId`(path) |
| `GET` | `/v1/estoque/produto/{produtoId}/composicao` | Listar Composições Produto | `produtoId`(path), Page, PageSize |
| `GET` | `/v1/estoque/unidade` | Listar Unidades | Id, Nome, Page, PageSize |
| `GET` | `/v1/estoque/grupo` | Listar Grupos | Id, Nome, Mobile, Page, PageSize |
| `GET` | `/v1/estoque/familia` | Listar Famílias | Id, Nome, Page, PageSize |
| `GET` | `/v1/estoque/marca` | Listar Marcas | ExibeOS, ExibePedido, Propria, Id, Nome, Page, PageSize |
| `GET` | `/v1/estoque/categoria` | Listar Categorias | CategoriaPaiId, Id, Nome, Page, PageSize |
| `GET` | `/v1/estoque/categoria/{id}` | Obter Categoria | `id`(path) |
| `GET` | `/v1/estoque/sugestaocompra` | Consulta Sugestão de Compra | EstoqueDias, EstabelecimentoGerar, Estabelecimentos, of, UltimosDias, DataInicial, DataFinal, Codigo |
| `POST` | `/v1/pcpproducao/desmontagemproduto` | Desmontar Produto | — |
| `GET` | `/v1/pcpproducao/desmontagemproduto` | Listar Desmontagens | Id, ProdutoId, Status, Page, PageSize |

**`POST` Cadastrar Produto — body fields:** `nome`, `apelido`, `ncm`, `codigoTipoSped`, `precoVenda`, `unidadeId`, `familiaId`, `grupoEstoqueId`, `tipoPeso`, `precoVendaMinimo`, `percentualComissao`, `lucroEstimado`, `lucroEstimadoMinimo`, `lucroEstimadoAlocado`, `percentualDescontoMaximo`, `potencia`, `modeloResumido`, `configuracaoMarketplaceId`, `codigoMarketPlace`, `origem`

**`PATCH` Editar — body fields:** `precoVenda`, `precoVendaMinimo`, `custoFornecedor`, `fornecedorId`, `codigoIdentificacaoInterno`, `nome`, `apelido`

**`POST` Desmontar Produto — body fields:** `produtoId`, `estabelecimentoId`, `localEstoqueId`, `usuarioId`, `quantidade`, `inicio`, `encerramento`, `ordemProducaoId`, `statusFluxoId`, `centroCustoId`, `clienteId`, `observacao`

---

### Projetos

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/projetos/projetoexecucao` | Listar | ClienteId, EstabelecimentoId, Descricao, Status, EstaExcluido, Page, PageSize |
| `GET` | `/v1/projetos/etapa` | Listar Etapas | ProjetoId, Nome, Page, PageSize |

---

### Serviços LC-116

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/estoque/servicoleicomplementar` | Listar | Id, Nome, Codigo, Page, PageSize |

---

### Serviços Prestados

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/estoque/servico` | Cadastrar | — |
| `GET` | `/v1/estoque/servico` | Listar | Id, Nome, Apelido, CodigoIdentificacaoInterno, MarcaId, FamiliaId, ExibeOs, Page, PageSize |

**`POST` Cadastrar — body fields:** `nome`, `apelido`, `ncm`, `unidadeId`, `familiaId`, `precoVenda`, `precoVendaMinimo`, `estabelecimentoFaturamentoId`, `codigoIdentificacaoInterno`, `codigoEspecificadorCEST`, `grupoEstoqueId`, `codigoGenero`, `codigoTipoSped`, `marcaId`, `listaServicoId`, `tecnicoRecebeComissao`, `controlaComissaoSupervisor`, `bloqueiaLancamentoProjeto`, `tributacaoNfse`, `cnae`

---

### Serviços Tomados

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/estoque/servicotomado` | Cadastrar | — |
| `GET` | `/v1/estoque/servicotomado` | Listar | Id, Nome, Apelido, CodigoIdentificacaoInterno, MarcaId, FamiliaId, ExibeOs, Page, PageSize |

**`POST` Cadastrar — body fields:** `nome`, `apelido`, `ncm`, `unidadeId`, `familiaId`, `listaServicoId`, `precoVenda`, `precoVendaMinimo`, `estabelecimentoFaturamentoId`, `codigoIdentificacaoInterno`, `codigoEspecificadorCEST`, `grupoEstoqueId`, `codigoGenero`, `codigoTipoSped`, `marcaId`, `tecnicoRecebeComissao`, `controlaComissaoSupervisor`, `bloqueiaLancamentoProjeto`, `tributacaoNfse`, `cnae`

---

### Status (Fluxo)

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/status` | Listar | Id, Nome, Page, PageSize |

---

### Tabelas de Preço

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/faturamento/tabelapreco` | Cadastrar Tabela de Preço | — |
| `GET` | `/v1/faturamento/tabelapreco` | Listar Tabela de Preços | Id, Nome, Page, PageSize |
| `POST` | `/v1/faturamento/tabelapreco/{tabelaPrecoId}/item` | Cadastrar Item | `tabelaPrecoId`(path) |
| `GET` | `/v1/faturamento/tabelapreco/{tabelaPrecoId}/item` | Listar Itens | `tabelaPrecoId`(path), ProdutoId, CodigoIdentificacaoInterno, Page, PageSize |

**`POST` Cadastrar Tabela de Preço — body fields:** `nome`, `empresaGrupoId`, `percentualComissao`, `percentualAcrescimo`, `percentualDesconto`, `calcularPesoLiquido`, `mobile`, `codigoImportacao`, `observacao`

**`POST` Cadastrar Item — body fields:** `condicaoPagamentoId`, `valor`, `produtoId`, `categoriaId`, `valorMinimo`, `percentualDescontoMaximo`, `margem`

---

### Tipo de Ações

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/crm/tipoacao` | Listar | Id, Nome, Page, PageSize |

---

### Tipo Ordens de Servico

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/tipoordemservico` | Listar | Id, Nome, Mobile, Page, PageSize |

---

### Tipos de Pedidos

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/faturamento/tipopedido` | Listar | Id, Nome, Page, PageSize |

---

### Tipos de Pessoas

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/configuracoes/tipopessoa` | Listar | Id, Nome, Page, PageSize |

---

### Transportadores

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/configuracoes/transportador` | Listar | Id, RazaoSocial, Fantasia, CpfCnpj, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSize |
| `GET` | `/v1/configuracoes/transportador/{id}` | Obter | `id`(path) |
| `GET` | `/v1/configuracoes/transportador/{transportadorId}/endereco` | Listar Endereços | `transportadorId`(path), TipoEndereco, Cep, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, Page |

**`POST` Cadastrar — body fields:** `tipoPessoaId`, `classificacaoId`, `cpfCnpj`, `razaoSocial`, `cep`, `logradouro`, `numero`, `bairroId`, `bairroNome`, `municipioId`, `municipioNome`, `uf`, `municipioIbge`, `fantasia`, `complemento`, `letra`, `apelido`, `tipoContribuinte`, `regimeTributario`, `operacaoConsumidorNFe`

---

### Usuarios

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/configuracoes/usuario` | Listar | Login, PessoaId, Administrador, Id, Nome, Page, PageSize |
| `GET` | `/v1/configuracoes/usuario/{id}/estabelecimento` | Listar Usuario Estabelecimentos | `id`(path), Page, PageSize |

---

### Utilitários

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `GET` | `/v1/utilitarios/consultacnpj` | Consulta CNPJ | Cnpj, SecurityKey |
| `GET` | `/v1/utilitarios/atualizarlicenca` | Atualizar Licenca | — |

---

### Veículos

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/configuracoes/veiculo` | Cadastrar | — |
| `GET` | `/v1/configuracoes/veiculo` | Listar | Placa, UF, EmpresaGrupoId, ProprietarioId, MotoristaId, TipoVeiculoId, VeiculoFipeId, Especie, Chass |

**`POST` Cadastrar — body fields:** `nome`, `placa`, `uf`, `proprietarioId`, `anoFabricacao`, `anoModelo`, `combustivel`, `tipoCarroceira`, `tipoRodado`, `combinacaoVeicular`, `empresaGrupoId`, `motoristaId`, `gestorId`, `centroCustoId`, `tipoVeiculoId`, `veiculoFipeId`, `marcaModelo`, `especie`, `chassi`, `renavam`

---

### Vendedores

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `_see description_` | Cadastrar | — |
| `GET` | `/v1/configuracoes/vendedor` | Listar | Id, RazaoSocial, Fantasia, CpfCnpj, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSize |
| `GET` | `/v1/configuracoes/vendedor/{id}` | Obter | `id`(path) |
| `GET` | `/v1/configuracoes/vendedor/{vendedorId}/endereco` | Listar Endereços | `vendedorId`(path), TipoEndereco, Cep, DataAtualizacaoInicial, DataAtualizacaoFinal, Page, PageSize |

**`POST` Cadastrar — body fields:** `tipoPessoaId`, `classificacaoId`, `cpfCnpj`, `razaoSocial`, `cep`, `logradouro`, `numero`, `bairroId`, `bairroNome`, `municipioId`, `municipioNome`, `uf`, `municipioIbge`, `fantasia`, `complemento`, `letra`, `apelido`, `tipoContribuinte`, `regimeTributario`, `operacaoConsumidorNFe`

---

### Volumes

| Method | Path | Summary | Params |
|--------|------|---------|--------|
| `POST` | `/v1/configuracoes/volume` | Cadastrar | — |
| `GET` | `/v1/configuracoes/volume` | Listar | Peso, Id, Nome, Page, PageSize |

**`POST` Cadastrar — body fields:** `nome`, `peso`, `observacao`

---

## Common Patterns

```
# List with filters
GET /v1/{resource}?Page=1&PageSize=50&<FilterField>=<value>

# Get by ID
GET /v1/{resource}/{id}

# Create
POST /v1/{resource}
Authorization: Bearer <token>
Content-Type: application/json

# Update (full)
PUT /v1/{resource}/{id}

# Update (partial)
PATCH /v1/{resource}/{id}

# Sub-resources
GET  /v1/{resource}/{parentId}/{subresource}
POST /v1/{resource}/{parentId}/{subresource}

# Actions
POST /v1/{resource}/{id}/cancelar
POST /v1/{resource}/{id}/faturar
PATCH /v1/{resource}/{id}/statusfluxo
```