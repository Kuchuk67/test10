import json


def func(input_json, currency):
    import json
    parsed_data = json.loads(input_json)
    # print((parsed_data))
    data = [x for x in parsed_data if x.get('currency') == currency]
    # print((data))
    return json.dumps(data, indent=4)


x = '''[
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

q = func(x, 'USD')
print(q)
