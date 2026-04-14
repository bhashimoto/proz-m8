# M8 Integra API — SDK Reference

## Overview

- **Base URL:** `https://api.integra.m8sistemas.com.br`
- **OpenAPI Spec:** `GET /swagger/v1/swagger.json`
- **Version:** 1.0 (OpenAPI 3.0.4)
- **Auth:** Bearer token (JWT) — obtain via `POST /v1/auth/token`

---

## Authentication

### Obtain Token
`POST /v1/auth/token`

**Request body:** `AuthRequestDto`
```
tenant     string   (required) - tenant identifier
username   string   (required)
password   string   (required)
company    int32    (required) - company ID
domain     string?  (optional)
```

**Response 200:** `AuthResponseDtoResponseDto`
```
data.token       string  - Bearer token to use in Authorization header
data.expiration  string  - token expiry datetime
errors           ErrorResponseDto[]?
```

**Usage:** Include in all subsequent requests:
```
Authorization: Bearer <token>
```

---

## Response Envelope

All responses follow this structure:

```
{
  "data":   <object | array | null>,
  "errors": [ { "message": string, "field": string? } ] | null
}
```

- List endpoints return `{ data: T[], errors: ... }`
- Single-object endpoints return `{ data: T, errors: ... }`
- Mutation endpoints often return `ObjFormResponseDtoResponseDto`: `{ data: { id: int } }`
- Empty success returns `EmptyResponseDtoResponseDto`: `{ data: null, errors: null }`

**HTTP status codes:**
- `200` Success
- `400` Bad Request (validation errors in `errors[]`)
- `401` Unauthorized
- `500` Internal Server Error

---

## Pagination

List endpoints accept query params:
```
Page      integer  (default: 1)
PageSize  integer  (default: varies)
```

---

## Endpoints

### Autenticação
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/auth/token` | Obter Token |

---

### Checklist
| Method | Path | Summary | Query Params |
|--------|------|---------|--------------|
| GET | `/v1/configuracoes/checklist` | Listar Checklists | EstaExcluido, Id, Nome, Page, PageSize |

---

### Classificação de Pessoas
| Method | Path | Summary | Query Params |
|--------|------|---------|--------------|
| GET | `/v1/configuracoes/classificacaopessoa` | Listar | Id, Nome, Page, PageSize |

---

### Clientes
| Method | Path | Summary | Notes |
|--------|------|---------|-------|
| POST | `/v1/configuracoes/cliente` | Cadastrar | body: `ClienteRequestDto` |
| GET | `/v1/configuracoes/cliente` | Listar | many query filters |
| GET | `/v1/configuracoes/cliente/{id}` | Obter por ID | path: `id` |
| PUT | `/v1/configuracoes/cliente/{id}` | Atualizar | path: `id`, body: `ClienteRequestDto` |
| GET | `/v1/configuracoes/cliente/{clienteId}/endereco` | Listar Endereços | |
| POST | `/v1/configuracoes/cliente/{clienteId}/endereco` | Cadastrar Endereço | body: `EnderecoRequestDto` |
| GET | `/v1/configuracoes/cliente/{clienteId}/tabelapreco` | Listar Tabelas de Preço | |
| GET | `/v1/configuracoes/cliente/{clienteId}/contato` | Listar Contatos | |
| POST | `/v1/configuracoes/cliente/{clienteId}/contato` | Cadastrar Contato | body: `ContatoRequestDto` |
| GET | `/v1/configuracoes/cliente/{clienteId}/historicolimite` | Histórico de Limite | |
| GET | `/v1/configuracoes/cliente/{clienteId}/vendedor` | Listar Vendedores do Cliente | |

**Lista de clientes — filtros disponíveis:**
`IndicadorVendaId`, `IndicadorVendaNome`, `Id`, `RazaoSocial`, `Fantasia`, `CpfCnpj`, `DataAtualizacaoInicial`, `DataAtualizacaoFinal`, `Page`, `PageSize`

---

### Clientes Adiantamento
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/financeiro/adiantamentocliente` | Cadastrar |
| GET | `/v1/financeiro/adiantamentocliente` | Listar |
| GET | `/v1/financeiro/adiantamentocliente/{id}` | Obter por ID |

---

### Condições de Pagamento
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/financeiro/condicaopagamento` | Listar |
| GET | `/v1/financeiro/condicaopagamento/{id}` | Obter por ID |

---

### Contas à Pagar
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/financeiro/contapagar` | Cadastrar |
| GET | `/v1/financeiro/contapagar` | Listar |
| GET | `/v1/financeiro/contapagar/{id}` | Obter por ID |
| PUT | `/v1/financeiro/contapagar/{id}` | Atualizar |
| GET | `/v1/financeiro/contapagar/consulta` | Consulta |
| GET | `/v1/financeiro/contapagar/{tituloId}/parcela` | Listar Parcelas |
| POST | `/v1/financeiro/contapagar/{tituloId}/baixa` | Baixar |

---

### Contas à Receber
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/financeiro/contareceber` | Cadastrar |
| GET | `/v1/financeiro/contareceber` | Listar |
| GET | `/v1/financeiro/contareceber/{id}` | Obter por ID |
| GET | `/v1/financeiro/contareceber/{tituloId}/parcela` | Listar Parcelas |
| GET | `/v1/financeiro/contareceber/importacao/{tituloCodigoImportacao}/parcela` | Parcelas por Código Importação |
| PUT | `/v1/financeiro/contareceber/{tituloId}/parcela/{id}` | Atualizar Parcela |
| POST | `/v1/financeiro/contareceber/{tituloId}/baixa` | Baixar |
| POST | `/v1/financeiro/contareceber/{tituloId}/cancelarbaixa` | Cancelar Baixa |

---

### Contratos Serviços
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/contratoservico/contratoservico` | Cadastrar |
| GET | `/v1/contratoservico/contratoservico` | Listar |
| GET | `/v1/contratoservico/contratoservico/{id}` | Obter por ID |

---

### CRM - Contas
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/crm/conta` | Cadastrar |
| GET | `/v1/crm/conta` | Listar |
| GET | `/v1/crm/conta/{id}` | Obter por ID |
| PUT | `/v1/crm/conta/{id}` | Atualizar |
| POST | `/v1/crm/conta/{contaId}/contato` | Cadastrar Contato |
| GET | `/v1/crm/conta/{contaId}/contato` | Listar Contatos |
| POST | `/v1/crm/conta/{contaId}/comentario` | Cadastrar Comentário |
| GET | `/v1/crm/conta/{contaId}/comentario` | Listar Comentários |

---

### CRM - Oportunidades
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/crm/oportunidade` | Cadastrar |
| GET | `/v1/crm/oportunidade` | Listar |
| GET | `/v1/crm/oportunidade/{id}` | Obter por ID |
| PUT | `/v1/crm/oportunidade/{id}` | Atualizar |
| POST | `/v1/crm/oportunidade/{oportunidadeId}/produto` | Cadastrar Produto |
| GET | `/v1/crm/oportunidade/{oportunidadeId}/produto` | Listar Produtos |
| POST | `/v1/crm/oportunidade/{oportunidadeId}/comentario` | Cadastrar Comentário |
| GET | `/v1/crm/oportunidade/{oportunidadeId}/comentario` | Listar Comentários |
| POST | `/v1/crm/oportunidade/{oportunidadeId}/anexo` | Cadastrar Anexo |

---

### CRM - Orçamentos
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/crm/orcamento` | Listar |
| GET | `/v1/crm/orcamento/{id}` | Obter por ID |

---

### Endereços
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/endereco/municipio` | Listar Municípios |
| GET | `/v1/configuracoes/endereco/bairro` | Listar Bairros |
| GET | `/v1/configuracoes/endereco/cep/{cep}` | Consultar CEP |

---

### Equipamentos
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/equipamento` | Listar |
| GET | `/v1/configuracoes/equipamento/{id}` | Obter por ID |

---

### Estoque
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/estoque/estoque` | Listar Saldo Estoque |
| POST | `/v1/estoque/estoque/movimentacao` | Movimentar Estoque |
| GET | `/v1/estoque/estoque/movimentacao` | Listar Movimentações |
| GET | `/v1/estoque/local` | Listar Locais de Estoque |

---

### Follow Up (Clientes/Contas)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/configuracoes/followup` | Cadastrar |
| GET | `/v1/configuracoes/followup` | Listar |

---

### Fornecedores
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/configuracoes/fornecedor` | Cadastrar |
| GET | `/v1/configuracoes/fornecedor` | Listar |
| GET | `/v1/configuracoes/fornecedor/{id}` | Obter por ID |
| PUT | `/v1/configuracoes/fornecedor/{id}` | Atualizar |
| GET | `/v1/configuracoes/fornecedor/{fornecedorId}/endereco` | Listar Endereços |
| POST | `/v1/configuracoes/fornecedor/{fornecedorId}/endereco` | Cadastrar Endereço |
| GET | `/v1/configuracoes/fornecedor/{fornecedorId}/contato` | Listar Contatos |
| POST | `/v1/configuracoes/fornecedor/{fornecedorId}/contato` | Cadastrar Contato |

---

### Fretes
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/frete` | Listar |

---

### Funcionarios
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/funcionario` | Listar |
| GET | `/v1/configuracoes/funcionario/{id}` | Obter por ID |

---

### Logs
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/utilitarios/log` | Listar Logs |

---

### Meios de Pagamento
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/financeiro/meiopagamento` | Listar |
| GET | `/v1/financeiro/meiopagamento/{id}` | Obter por ID |

---

### Montagem de Carga
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/faturamento/montagemcarga` | Listar |
| GET | `/v1/faturamento/montagemcarga/{id}` | Obter por ID |
| POST | `/v1/faturamento/montagemcarga` | Cadastrar |
| PUT | `/v1/faturamento/montagemcarga/{id}` | Atualizar |

---

### Ncm/Ibpt
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/fiscal/ncm` | Listar NCM |
| GET | `/v1/fiscal/ibpt` | Consultar IBPT |

---

### Notas Fiscais (Compra)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/fiscal/notafiscalcompra` | Cadastrar |
| GET | `/v1/fiscal/notafiscalcompra` | Listar |
| GET | `/v1/fiscal/notafiscalcompra/{id}` | Obter por ID |
| POST | `/v1/fiscal/notafiscalcompra/{id}/cancelar` | Cancelar |

---

### Notas Fiscais (Outras)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/fiscal/notafiscaloutras` | Cadastrar |
| GET | `/v1/fiscal/notafiscaloutras` | Listar |
| GET | `/v1/fiscal/notafiscaloutras/{id}` | Obter por ID |
| POST | `/v1/fiscal/notafiscaloutras/{id}/faturar` | Faturar |
| PUT | `/v1/fiscal/notafiscaloutras/{id}/atualizar` | Atualizar |
| POST | `/v1/fiscal/notafiscaloutras/{id}/cancelar` | Cancelar |

---

### Notas Fiscais (Venda)
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/fiscal/notafiscalvenda` | Listar |
| GET | `/v1/fiscal/notafiscalvenda/{id}` | Obter por ID |
| POST | `/v1/fiscal/notafiscalvenda/{id}/cancelar` | Cancelar |
| POST | `/v1/fiscal/notafiscalvenda/{id}/cartacorrecao` | Carta de Correção |

---

### Números de Série
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/numeroserie` | Listar |

---

### Operações Fiscais
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/fiscal/operacaofiscal` | Listar |
| GET | `/v1/fiscal/operacaofiscal/{id}` | Obter por ID |

---

### Orçamentos (Faturamento)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/faturamento/orcamento` | Cadastrar |
| GET | `/v1/faturamento/orcamento` | Listar |
| GET | `/v1/faturamento/orcamento/{id}` | Obter por ID |
| PUT | `/v1/faturamento/orcamento/{id}` | Atualizar |
| POST | `/v1/faturamento/orcamento/{id}/cancelar` | Cancelar |

---

### Ordens de Compra
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/compras/ordemcompra` | Cadastrar |
| GET | `/v1/compras/ordemcompra` | Listar |
| GET | `/v1/compras/ordemcompra/{id}` | Obter por ID |
| PUT | `/v1/compras/ordemcompra/{id}` | Atualizar |
| GET | `/v1/compras/ordemcompra/{ordemCompraId}/item` | Listar Itens |
| POST | `/v1/compras/ordemcompra/{ordemCompraId}/cancelar` | Cancelar |

---

### Ordens de Produção
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/pcpproducao/tipoordemproducao` | Listar Tipos |
| POST | `/v1/pcpproducao/ordemproducao` | Cadastrar |
| GET | `/v1/pcpproducao/ordemproducao` | Listar |
| GET | `/v1/pcpproducao/ordemproducao/{id}` | Obter por ID |
| PUT | `/v1/pcpproducao/ordemproducao/{id}` | Atualizar |
| POST | `/v1/pcpproducao/ordemproducao/{id}/cancelar` | Cancelar |
| POST | `/v1/pcpproducao/ordemproducao/{id}/finalizar` | Finalizar |

---

### Ordens de Serviço (Assist. Técnica)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/assistenciatecnica/ordemservico` | Cadastrar |
| GET | `/v1/assistenciatecnica/ordemservico` | Listar |
| GET | `/v1/assistenciatecnica/ordemservico/{id}` | Obter por ID |
| PUT | `/v1/assistenciatecnica/ordemservico/{id}` | Atualizar |
| POST | `/v1/assistenciatecnica/ordemservico/{id}/cancelar` | Cancelar |
| POST | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/apontamentohora` | Apontar Horas |
| GET | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/apontamentohora` | Listar Apontamentos |
| POST | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/equipamento` | Cadastrar Equipamento |
| GET | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/equipamento` | Listar Equipamentos |
| POST | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/servico` | Cadastrar Serviço |
| GET | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/servico` | Listar Serviços |
| POST | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/produto` | Cadastrar Produto |
| GET | `/v1/assistenciatecnica/ordemservico/{ordemServicoId}/produto` | Listar Produtos |

---

### Ordens de Serviço (Faturamento)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/faturamento/ordemservico` | Cadastrar |
| GET | `/v1/faturamento/ordemservico` | Listar |
| GET | `/v1/faturamento/ordemservico/{id}` | Obter por ID |
| PUT | `/v1/faturamento/ordemservico/{id}` | Atualizar |
| POST | `/v1/faturamento/ordemservico/{id}/cancelar` | Cancelar |

---

### Pedidos (Fat. Direto)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/faturamento/pedidodiretofaturamento` | Cadastrar |
| GET | `/v1/faturamento/pedidodiretofaturamento` | Listar |
| GET | `/v1/faturamento/pedidodiretofaturamento/{id}` | Obter por ID |

---

### Pedidos (Padrão)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/faturamento/pedido` | Cadastrar |
| GET | `/v1/faturamento/pedido` | Listar |
| GET | `/v1/faturamento/pedido/{id}` | Obter por ID |
| PUT | `/v1/faturamento/pedido/{id}` | Atualizar |
| POST | `/v1/faturamento/pedido/{id}/cancelar` | Cancelar |
| POST | `/v1/faturamento/pedido/{id}/duplicar` | Duplicar |
| POST | `/v1/faturamento/pedido/{id}/faturar` | Faturar |
| GET | `/v1/faturamento/pedido/{pedidoId}/item` | Listar Itens |

---

### Pedidos (Rápido)
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/faturamento/pedido/rapido` | Cadastrar Rápido |
| GET | `/v1/faturamento/pedido/rapido` | Listar |
| GET | `/v1/faturamento/pedido/rapido/{id}` | Obter por ID |
| POST | `/v1/faturamento/pedido/rapido/{id}/cancelar` | Cancelar |
| POST | `/v1/faturamento/pedido/rapido/{id}/faturar` | Faturar |
| POST | `/v1/faturamento/pedido/notafiscal/devolucao` | Devolução NF Venda |
| POST | `/v1/faturamento/pedido/desmontar` | Desmontar Pedido |
| GET | `/v1/faturamento/pedido/capacidadeseparacao` | Capacidade de Separação |

---

### Plano de Contas
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/financeiro/planodeconta` | Listar |
| GET | `/v1/financeiro/planodeconta/{id}` | Obter por ID |

---

### Produtos
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/configuracoes/produto` | Cadastrar |
| GET | `/v1/configuracoes/produto` | Listar |
| GET | `/v1/configuracoes/produto/{id}` | Obter por ID |
| PUT | `/v1/configuracoes/produto/{id}` | Atualizar |
| GET | `/v1/configuracoes/produto/{produtoId}/preco` | Listar Preços |
| POST | `/v1/configuracoes/produto/{produtoId}/preco` | Cadastrar Preço |
| PUT | `/v1/configuracoes/produto/{produtoId}/preco/{id}` | Atualizar Preço |
| GET | `/v1/configuracoes/produto/{produtoId}/complemento` | Obter Complemento |
| PUT | `/v1/configuracoes/produto/{produtoId}/complemento` | Atualizar Complemento |
| GET | `/v1/configuracoes/produto/{produtoId}/imagem` | Listar Imagens |
| POST | `/v1/configuracoes/produto/{produtoId}/imagem` | Cadastrar Imagem |
| DELETE | `/v1/configuracoes/produto/{produtoId}/imagem/{id}` | Excluir Imagem |

---

### Projetos
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/projetos/projeto` | Cadastrar |
| GET | `/v1/projetos/projeto` | Listar |
| GET | `/v1/projetos/projeto/{id}` | Obter por ID |
| PUT | `/v1/projetos/projeto/{id}` | Atualizar |

---

### Serviços LC-116
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/fiscal/servicolc116` | Listar |

---

### Serviços Prestados
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/fiscal/nfse/servicoprestado` | Cadastrar |
| GET | `/v1/fiscal/nfse/servicoprestado` | Listar |
| GET | `/v1/fiscal/nfse/servicoprestado/{id}` | Obter por ID |
| POST | `/v1/fiscal/nfse/servicoprestado/{id}/faturar` | Faturar |
| POST | `/v1/fiscal/nfse/servicoprestado/{id}/cancelar` | Cancelar |

---

### Serviços Tomados
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/fiscal/nfse/servicotomado` | Cadastrar |
| GET | `/v1/fiscal/nfse/servicotomado` | Listar |
| GET | `/v1/fiscal/nfse/servicotomado/{id}` | Obter por ID |

---

### Status (Fluxo)
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/status` | Listar |
| GET | `/v1/configuracoes/status/{id}` | Obter por ID |

---

### Tabelas de Preço
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/tabelapreco` | Listar |
| GET | `/v1/configuracoes/tabelapreco/{id}` | Obter por ID |

---

### Tipo Ações
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/tipoacao` | Listar |

---

### Tipo Ordens de Serviço
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/tipoordemservico` | Listar |

---

### Tipos de Pedidos
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/faturamento/tipopedido` | Listar |
| GET | `/v1/faturamento/tipopedido/{id}` | Obter por ID |

---

### Tipos de Pessoas
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/tipopessoa` | Listar |

---

### Transportadores
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/transportador` | Listar |
| GET | `/v1/configuracoes/transportador/{id}` | Obter por ID |

---

### Usuarios
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/utilitarios/usuario` | Listar |
| GET | `/v1/utilitarios/usuario/{id}` | Obter por ID |

---

### Utilitários
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/utilitarios/empresa` | Listar Empresas |
| GET | `/v1/utilitarios/empresa/{id}` | Obter Empresa por ID |

---

### Veículos
| Method | Path | Summary |
|--------|------|---------|
| POST | `/v1/configuracoes/veiculo` | Cadastrar |
| GET | `/v1/configuracoes/veiculo` | Listar |
| GET | `/v1/configuracoes/veiculo/{id}` | Obter por ID |
| PUT | `/v1/configuracoes/veiculo/{id}` | Atualizar |

---

### Vendedores
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/vendedor` | Listar |
| GET | `/v1/configuracoes/vendedor/{id}` | Obter por ID |

---

### Volumes
| Method | Path | Summary |
|--------|------|---------|
| GET | `/v1/configuracoes/volume` | Listar |

---

## Key Request Schemas

### `AuthRequestDto`
| Field | Type | Required |
|-------|------|----------|
| tenant | string | ✅ |
| username | string | ✅ |
| password | string | ✅ |
| company | int32 | ✅ |
| domain | string | ❌ |

---

### `ClienteRequestDto` / `FornecedorRequestDto`
| Field | Type | Required |
|-------|------|----------|
| tipoPessoaId | int32 | ✅ |
| classificacaoId | int32 | ✅ |
| cpfCnpj | string | ✅ |
| razaoSocial | string | ✅ |
| cep | string | ✅ |
| logradouro | string | ✅ |
| numero | string | ✅ |
| bairroId | int32 | ❌ |
| bairroNome | string | ❌ |
| municipioId | int32 | ❌ |
| municipioNome | string | ❌ |
| uf | string | ❌ |
| fantasia | string | ❌ |
| complemento | string | ❌ |
| tabelaPrecoId | int32 | ❌ |
| tipoContribuinte | `TipoContribuinteNfeEnum` | ❌ |
| regimeTributario | `RegimeTributarioEnum` | ❌ |
| nascimento | datetime | ❌ |
| inscricaoEstadual | string | ❌ |
| inscricaoMunicipal | string | ❌ |

---

### `ProdutoRequestDto`
| Field | Type | Required |
|-------|------|----------|
| grupoProdutoId | int32 | ✅ |
| unidadeId | int32 | ✅ |
| descricao | string | ✅ |
| codigo | string | ❌ |
| codigoBarras | string | ❌ |
| ncmId | int32 | ❌ |
| precoVenda | decimal | ❌ |
| precoCusto | decimal | ❌ |
| estocavel | bool | ❌ |
| ativo | bool | ❌ |
| observacao | string | ❌ |

---

### `PedidoRequestDto`
| Field | Type | Required |
|-------|------|----------|
| tipoPedidoId | int32 | ✅ |
| clienteId | int32 | ✅ |
| operacaoFiscalId | int32 | ✅ |
| dataEmissao | datetime | ✅ |
| dataPrevisaoEntrega | datetime | ❌ |
| condicaoPagamentoId | int32 | ❌ |
| vendedorId | int32 | ❌ |
| transportadorId | int32 | ❌ |
| observacao | string | ❌ |
| itens | `PedidoItemRequestDto[]` | ✅ |

---

### `PedidoItemRequestDto`
| Field | Type | Required |
|-------|------|----------|
| produtoId | int32 | ✅ |
| quantidade | decimal | ✅ |
| precoUnitario | decimal | ✅ |
| desconto | decimal | ❌ |
| observacao | string | ❌ |

---

### `OrdemCompraRequestDto`
| Field | Type | Required |
|-------|------|----------|
| fornecedorId | int32 | ✅ |
| dataEmissao | datetime | ✅ |
| dataPrevisaoEntrega | datetime | ❌ |
| condicaoPagamentoId | int32 | ❌ |
| observacao | string | ❌ |
| itens | `OrdemCompraItemRequestDto[]` | ✅ |

---

### `ContaPagarRequestDto` / `ContaReceberRequestDto`
| Field | Type | Required |
|-------|------|----------|
| pessoaId | int32 | ✅ |
| planoContaId | int32 | ✅ |
| dataEmissao | datetime | ✅ |
| dataVencimento | datetime | ✅ |
| valor | decimal | ✅ |
| historico | string | ❌ |
| numeroParcelas | int32 | ❌ |
| meiopagamentoId | int32 | ❌ |

---

### `EstoqueMovimentacaoRequestDto`
| Field | Type | Required |
|-------|------|----------|
| produtoId | int32 | ✅ |
| localEstoqueId | int32 | ✅ |
| tipoMovimentacao | `TipoMovimentacaoEstoqueEnum` | ✅ |
| quantidade | decimal | ✅ |
| dataMovimentacao | datetime | ✅ |
| observacao | string | ❌ |

---

### `EnderecoRequestDto`
| Field | Type | Required |
|-------|------|----------|
| cep | string | ✅ |
| logradouro | string | ✅ |
| numero | string | ✅ |
| bairroId | int32 | ❌ |
| bairroNome | string | ❌ |
| municipioId | int32 | ❌ |
| municipioNome | string | ❌ |
| uf | string | ❌ |
| complemento | string | ❌ |
| principal | bool | ❌ |

---

### `ContatoRequestDto`
| Field | Type | Required |
|-------|------|----------|
| nome | string | ✅ |
| email | string | ❌ |
| telefone | string | ❌ |
| celular | string | ❌ |
| cargo | string | ❌ |

---

## Key Enums

| Enum | Values |
|------|--------|
| `TipoContribuinteNfeEnum` | `ContribuinteIcms`, `ContribuinteIsento`, `NaoContribuinte` |
| `RegimeTributarioEnum` | `SimplesNacional`, `SimplesNacionalExcesso`, `RegimeNormal` |
| `OperacaoConsumidorNfeEnum` | `Normal`, `ConsumidorFinal` |
| `TipoMovimentacaoEstoqueEnum` | `Entrada`, `Saida` |
| `BoleanoEnum` | `Nao`, `Sim` |
| `CombustivelEnum` | `Gasolina`, `Alcool`, `Diesel`, `GNV`, `Eletrico`, `Hibrido` |
| `SituacaoNfeEnum` | `Pendente`, `Autorizada`, `Cancelada`, `Denegada`, `Inutilizada` |
| `TipoFreteCteEnum` | `CIF`, `FOB`, `Terceiros`, `SemFrete` |
| `ModalidadeFreteNfeEnum` | `ContratacaoRemetente`, `ContratacaoDestinatario`, `ContratacaoTerceiros`, `SemOcorrencia` |
| `AtivoEcommerceEnum` | `NaoApresentaPortal`, `ApresentaPortalUsuarioInterno`, `ApresentaPortalTodos`, ... |

---

## Common Patterns

### Listing with filters
```
GET /v1/{resource}?Page=1&PageSize=50&<FilterField>=<value>
```

### Get by ID
```
GET /v1/{resource}/{id}
```

### Create
```
POST /v1/{resource}
Content-Type: application/json
Authorization: Bearer <token>
Body: <RequestDto>
```

### Update
```
PUT /v1/{resource}/{id}
Content-Type: application/json
Authorization: Bearer <token>
Body: <RequestDto>
```

### Sub-resources
```
GET  /v1/{resource}/{parentId}/{subresource}
POST /v1/{resource}/{parentId}/{subresource}
```

### Actions (non-CRUD)
```
POST /v1/{resource}/{id}/cancelar
POST /v1/{resource}/{id}/faturar
POST /v1/{resource}/{id}/baixa
POST /v1/{resource}/{id}/finalizar
```