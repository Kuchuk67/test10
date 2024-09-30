import pytest
from functions import func


@pytest.fixture
def input_json():
    return '''[
    {
        "date": "2021-05-01",
        "amount": 1000,
        "currency": "USD",
        "description": "Salary"
    },
    {
        "date": "2021-05-02",
        "amount": -50,
        "currency": "EUR",
        "description": "Dinner"
    },
    {
        "date": "2021-05-03",
        "amount": -20,
        "currency": "USD",
        "description": "Coffee"
    },
    {
        "date": "2021-05-04",
        "amount": 200,
        "currency": "GBP",
        "description": "Gift"
    }
    ]'''


@pytest.fixture
def output_json():
    return '''[
    {
        "date": "2021-05-01",
        "amount": 1000,
        "currency": "USD",
        "description": "Salary"
    },
    {
        "date": "2021-05-03",
        "amount": -20,
        "currency": "USD",
        "description": "Coffee"
    }
]'''


def test_func(input_json: str, output_json: str) -> None:
    result = func(input_json, "USD")
    assert result == output_json
    pass
