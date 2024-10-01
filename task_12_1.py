
import json

with open('example.json', 'r') as file:  # открыть файл
    #data = file.read()
    #data = json.loads(data)
    data = json.load(file)
    #data2 = json.load(file)


    print(data)

def weather_to_city(city: str) -> None:
    with open('example.json', 'r') as file:  # открыть файл
        data_json = json.load(file)
    data_city = data_json[city]
    #for x in data_json[city]:
    #average_value = round(sum(data_city.values()) / len(data_city),1)
    average_value = {}
    average_value['Average temperature'] = round(sum(data_city.values()) / len(data_city),1)
    data_json_output = {}
    data_json_output[city] = average_value


    with open('example_output.json', 'w') as file:  # открыть файл
        json.dump(data_json_output, file, indent=4)


# weather_to_city('Moscow')
from datetime import datetime

def get_days_between_dates(data_start: str, date_end: str) -> int:
    ''' Возвращает количество дней между датами'''
    data_start_date = datetime.strptime(data_start, "%d.%m.%Y")
    data_end_date = datetime.strptime(date_end, "%d.%m.%Y")

    date_period =  (data_end_date - data_start_date).days
    return date_period

get_days_between_dates("01.01.2022", "31.01.2022")

