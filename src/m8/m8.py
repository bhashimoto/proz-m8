import json
import datetime as dt
from functools import wraps
import logging
import time


import requests

from .purchase_order import (PurchaseOrder,
                             PurchaseOrderInstallment,
                             PurchaseOrderItem)


logger = logging.getLogger(__name__)


class BadRequestException(Exception):
    pass


class UnauthorizedException(Exception):
    pass


class M8:
    endpoints = {
        "auth": {
            "endpoint": "v1/auth/token",
            "methods": {}
        },
        "invoices": {
            "endpoint": "v1/faturamento/notafiscalvenda",
            "methods": {
                "cancel": "cancelar",
                "send": "faturar",
                "patch": "editar",
            }
        },
        "purchase_orders": {
            "endpoint": "v1/compras/ordemcompra",
            "methods": {
                "listar": "",
                "cadastrar": "",
                "listar_itens": "item",
                "cadastrar_item": "item",
                "cadastrar_parcela": "parcela",
            }
        },
        "receivables": {
            "endpoint": "v1/financeiro/contareceber",
            "methods": {
                "listar": "",
                "listar_parcelas": "parcela",
            },
        },
    }

    ESTABS = {
        "ESSA": 1,
        "Sacomã": 17,
        "Belo Horizonte": 31,
    }

    def __init__(self):
        self._base_url: str = "https://api.integra.m8sistemas.com.br"
        self._auth_token_expiration_dt = dt.datetime.now() + \
            dt.timedelta(days=-1)
        self._auth_token = ""
        self._headers = {
            "Authorization": "Bearer " + self._auth_token,
            "Content-Type": "application/json; charset=utf-8",
        }
        print("inicializando m8 em ", dt.datetime.now())

    def auth(func):
        """
        Calls the wrapped method. If the response is
        a 401 error (Unauthorized), calls the authenticate
        method and calls the wrapped method again.
        """
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self._auth_token_expiration_dt + dt.timedelta(minutes=-1) < dt.datetime.now():
                tries = 1
                max_tries = 3
                while tries < max_tries:
                    try:
                        self.authenticate()
                        break
                    except BadRequestException as e:
                        tries += 1
                        if tries == max_tries:
                            raise e
                        time.sleep(1.0)

            return func(self, *args, **kwargs)
        return wrapper

    @auth
    def _request_get_with_query_params(self, url: str,
                                       search_params: dict) -> list:
        params: list = []

        for key in search_params.keys():
            params.append(f"{key}={search_params[key]}")
        if len(params) > 0:
            url = url + f"?{"&".join(params)}"

        resp = requests.get(url=url, headers=self._headers)

        if resp.status_code > 299:
            logger.error(resp.json()["errors"][0]["message"])
            return []

        return resp.json()["data"]

    def set_credentials(self, username: str, password: str,
                        tenant: str, company_id: int):
        self._username = username
        self._password = password
        self._tenant = tenant
        self._company = company_id

    def authenticate(self):
        print("renovando token", end="")
        data = {
            "tenant": self._tenant,
            "username": self._username,
            "password": self._password,
            "company": self._company,
        }

        logger.info(f"logging into tenant {self._tenant}, company {
                    self._company} with user {self._username}")

        url = self._base_url + "/" + M8.endpoints["auth"]["endpoint"]
        resp = requests.post(url, json=data)

        if resp.status_code == 200:
            print(" -- autenticado")
            resp_json = resp.json()
            min_exp = int(resp_json["data"]["minutesExpire"])
            exp_dt = dt.datetime.now() + dt.timedelta(minutes=min_exp)
            self._auth_token_expiration_dt = exp_dt
            self._auth_token = resp_json["data"]["token"]
            self._headers["Authorization"] = "Bearer " + self._auth_token
        elif resp.status_code == 401:
            raise UnauthorizedException
        else:
            raise BadRequestException(resp.json()["errors"][0]["message"])

    @auth
    def switch_company(self, new_company_id: int):
        if self._company != new_company_id:
            self._company = new_company_id
            self.authenticate()

    @auth
    def cancel_invoice(self, invoice_id: int, reason: str) -> str | None:
        url = "/".join([self._base_url,
                        M8.endpoints["invoices"]["endpoint"],
                        str(invoice_id),
                        M8.endpoints["invoices"]["methods"]["cancel"]])

        body = {
            "motivo": reason,
        }

        resp = requests.post(url, headers=self._headers, json=body)

        if resp.status_code == 401:
            raise UnauthorizedException
        if resp.status_code > 299:
            raise BadRequestException(resp.json()["errors"][0]["message"])

    @auth
    def send_invoice(self, invoice_id: int) -> None:
        url = "/".join([self._base_url,
                        M8.endpoints["invoices"]["endpoint"],
                        str(invoice_id),
                        M8.endpoints["invoices"]["methods"]["send"]])

        resp = requests.post(url=url, headers=self._headers, json={})

        if resp.status_code > 299:
            raise BadRequestException(resp.json()["errors"][0]["message"])

    def get_invoices(self, search_params: dict) -> list:
        url = self._base_url + "/" + M8.endpoints["invoices"]["endpoint"]

        return self._request_get_with_query_params(url=url,
                                                   search_params=search_params)

    def get_unsent_invoices(self) -> list:
        search_params = {
            "Status": "Pendente"
        }
        return self.get_invoices(search_params=search_params)

    @auth
    def update_invoice(self, invoice_id: int, context: dict = {}) -> None:
        url = "/".join([self._base_url,
                       M8.endpoints["invoices"]["endpoint"],
                       str(invoice_id)])

        resp = requests.patch(url=url, headers=self._headers, json=context)

        if resp.status_code > 299:
            raise BadRequestException(resp.json()["errors"][0]["message"])

    @auth
    def send_invoice_with_custom_date(self, invoice_id: int, date: str) -> None:
        self.update_invoice(invoice_id=invoice_id, context={"emissao": date})
        self.send_invoice(invoice_id=invoice_id)

    @auth
    def get_purchase_orders(self, search_params: dict) -> list:
        url = self._base_url + "/" + \
            M8.endpoints["purchase_orders"]["endpoint"]
        return self._request_get_with_query_params(url,
                                                   search_params=search_params)

    @auth
    def get_purchase_order_items(self, po_id: int,
                                 search_params: dict) -> list:
        url = "/".join([self._base_url,
                        M8.endpoints["purchase_orders"]["endpoint"],
                        str(po_id),
                        M8.endpoints["purchase_orders"]["methods"]["listar_itens"]])

        return self._request_get_with_query_params(url=url,
                                                   search_params=search_params)

    @auth
    def create_purchase_order(self, po_data: PurchaseOrder, full: bool = False) -> int:
        url = self._base_url + "/" + \
            M8.endpoints["purchase_orders"]["endpoint"]

        po_dict = po_data.to_dict()
        logger.debug(po_dict)
        resp = requests.post(url, json=po_dict, headers=self._headers)

        if resp.status_code > 299:
            logger.error(f"Error in create_purchase_order(). Status code: {
                         resp.status_code}")
            raise BadRequestException(resp.json()["errors"][0]["message"])

        po_id = resp.json()["data"]["id"]

        if full:
            for item in po_data.items:
                self.create_purchase_order_item(po_id, item)
            for installment in po_data.installments:
                self.create_purchase_order_installment(po_id, installment)

        return po_id

    @auth
    def create_purchase_order_item(self, po_id: int, item: PurchaseOrderItem) -> int:
        url = "/".join([self._base_url,
                        M8.endpoints["purchase_orders"]["endpoint"],
                        str(po_id),
                        M8.endpoints["purchase_orders"]["methods"]["cadastrar_item"]
                        ])

        logger.debug(item.to_dict())
        resp = requests.post(url, json=item.to_dict(), headers=self._headers)

        if resp.status_code > 299:
            logger.error(f"Error in create_purchase_order(). Status code: {
                         resp.status_code}")
            raise BadRequestException(resp.json()["errors"][0]["message"])

        return resp.json()["data"]["id"]

    @auth
    def create_purchase_order_installment(self, po_id: int, installment: PurchaseOrderInstallment):
        url = "/".join([self._base_url,
                        M8.endpoints["purchase_orders"]["endpoint"],
                        str(po_id),
                        M8.endpoints["purchase_orders"]["methods"]["cadastrar_parcela"]
                        ])

        resp = requests.post(
            url, json=installment.to_dict(), headers=self._headers)

        if resp.status_code > 299:
            logger.error(f"Error in create_purchase_order(). Status code: {
                         resp.status_code}")
            raise BadRequestException(resp.json()["errors"][0]["message"])

    def get_receivables(self, search_params: dict) -> list:
        url = self._base_url + "/" + M8.endpoints["receivables"]["endpoint"]
        data = self._request_get_with_query_params(
            url, search_params=search_params)

        for i in range(len(data)):
            detail_url = "/".join([self._base_url,
                                   M8.endpoints["receivables"]["endpoint"],
                                   str(data[i]["id"]),
                                   M8.endpoints["receivables"]["methods"]["listar_parcelas"]])
            details = self._request_get_with_query_params(
                detail_url, search_params={})

            # fix dom formatting
            data[i]['dataEntrada'] = data[i]['dataEntrada'][:10]
            data[i]['dataEmissao'] = data[i]['dataEmissao'][:10]
            data[i]['dataCompetencia'] = data[i]['dataCompetencia'][:10]

            # Considerando que não fazemos nenhum parcelamento.
            # Havendo parcelamento, precisa refatorar aqui
            if len(details) > 0:
                data[i]['vencimento'] = details[0]["vencimento"][:10]
            else:
                data[i]['vencimento'] = ""

        return data


def load_credentials_from_file(filename: str) -> tuple[str, str]:
    with open(filename) as f:
        data = json.load(f)
        username = data['username']
        password = data['password']
        return username, password
