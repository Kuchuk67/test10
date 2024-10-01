from currency import get_currency_rate
import json
from unittest.mock import patch

@patch('currency.requests.get')
def test_get_currency_rate(mocked_get):
    mocked_get.return_value.status_code = 200
    mocked_get.return_value.json.return_value = {
"Date": "2024-10-01T11:30:00+03:00",
"Valute": {
    "USD": {
        "CharCode": "USD",
        "Value": 91.7571,
        "Previous": 63.7677
        }
    }
}
    result  = get_currency_rate("USD")
    assert result == '''{
    "currency_code": "USD",
    "rate": 91.7571
}'''

@patch('currency.requests.get')
def test_get_currency_rate_no_200(mocked_get):
    mocked_get.return_value.status_code = 404
    result = get_currency_rate("USD")
    assert result == False
