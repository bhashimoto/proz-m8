# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Python library (`proz-m8`) for integrating with the M8 ERP API (`api.integra.m8sistemas.com.br`). It wraps M8's REST API endpoints for invoices, purchase orders, and receivables.

The full M8 API reference is documented in [`m8-api-doc.md`](m8-api-doc.md). Consult it for available endpoints, request/response schemas, enums, and pagination conventions.

## Setup & Installation

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install in editable mode
pip install -e .
```

## Architecture

The library is structured as a single `M8` class (`src/m8/m8.py`) with supporting dataclasses.

### Core class: `M8`

- **Authentication**: JWT token-based via `authenticate()`. The `@auth` decorator (defined as a static method on the class) auto-refreshes the token before any decorated method call if expired.
- **`set_credentials(username, password, tenant, company_id)`**: Must be called before any API operation.
- **`switch_company(new_company_id)`**: Re-authenticates for a different company within the same tenant.
- **Endpoints dict**: All API paths are centralized in `M8.endpoints` class variable.
- **`ESTABS` dict**: Maps establishment names to company IDs.

### Submodule: `purchase_order`

`src/m8/purchase_order/purchase_order.py` contains three dataclasses:
- `PurchaseOrder` — header fields; `items` and `installments` lists are only serialized when `to_dict(full=True)` is called
- `PurchaseOrderItem`
- `PurchaseOrderInstallment`

All exported from `src/m8/__init__.py` alongside `M8` and `load_credentials_from_file`.

### Credentials file format

`load_credentials_from_file(filename)` reads a JSON file:
```json
{"username": "...", "password": "..."}
```

### API response conventions

- Success responses wrap data in `resp.json()["data"]`
- Error messages are in `resp.json()["errors"][0]["message"]`
- HTTP status > 299 is treated as an error
- `get_receivables()` fetches installment details per receivable and normalizes date strings to `YYYY-MM-DD`

## Building & Publishing

```bash
pip install hatchling
python -m build
```

The package builds from `src/m8/` as the wheel source.
