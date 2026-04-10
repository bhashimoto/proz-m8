import pytest
from unittest.mock import patch
from m8 import BadRequestException
from .conftest import make_response, make_error_response


def make_receivable(id_=1):
    return {
        "id": id_,
        "dataEntrada": "2024-01-15T10:00:00",
        "dataEmissao": "2024-01-10T08:30:00",
        "dataCompetencia": "2024-01-01T00:00:00",
    }


def make_installment(vencimento="2024-02-15T00:00:00"):
    return {"vencimento": vencimento, "valor": 100.0}


class TestGetReceivables:
    def _setup_mocks(self, authenticated_m8, receivables, installments_per_id):
        """
        Patches requests.get to return receivables on first call,
        then installment data for each subsequent call.
        """
        list_response = make_response(200, {"data": receivables})
        detail_responses = [
            make_response(200, {"data": installments_per_id.get(r["id"], [])})
            for r in receivables
        ]
        return [list_response] + detail_responses

    def test_get_receivables_normalizes_dates(self, authenticated_m8):
        rec = make_receivable()
        responses = self._setup_mocks(authenticated_m8, [rec], {1: []})

        with patch("m8.m8.requests.get", side_effect=responses):
            result = authenticated_m8.get_receivables({})

        assert result[0]["dataEntrada"] == "2024-01-15"
        assert result[0]["dataEmissao"] == "2024-01-10"
        assert result[0]["dataCompetencia"] == "2024-01-01"

    def test_get_receivables_sets_vencimento_from_installment(self, authenticated_m8):
        rec = make_receivable()
        installment = make_installment("2024-02-28T00:00:00")
        responses = self._setup_mocks(authenticated_m8, [rec], {1: [installment]})

        with patch("m8.m8.requests.get", side_effect=responses):
            result = authenticated_m8.get_receivables({})

        assert result[0]["vencimento"] == "2024-02-28"

    def test_get_receivables_vencimento_empty_when_no_installments(self, authenticated_m8):
        rec = make_receivable()
        responses = self._setup_mocks(authenticated_m8, [rec], {1: []})

        with patch("m8.m8.requests.get", side_effect=responses):
            result = authenticated_m8.get_receivables({})

        assert result[0]["vencimento"] == ""

    def test_get_receivables_raises_on_error(self, authenticated_m8):
        with patch("m8.m8.requests.get", return_value=make_error_response(500, "server error")):
            with pytest.raises(BadRequestException, match="server error"):
                authenticated_m8.get_receivables({})

    def test_get_receivables_handles_multiple_records(self, authenticated_m8):
        recs = [make_receivable(1), make_receivable(2)]
        responses = self._setup_mocks(
            authenticated_m8, recs,
            {1: [make_installment("2024-02-01T00:00:00")], 2: []}
        )

        with patch("m8.m8.requests.get", side_effect=responses):
            result = authenticated_m8.get_receivables({})

        assert len(result) == 2
        assert result[0]["vencimento"] == "2024-02-01"
        assert result[1]["vencimento"] == ""
