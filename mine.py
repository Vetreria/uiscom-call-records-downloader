import requests
import dotenv
import datetime
import os.path
import sqlite3 as sl
import json
import wget


def get_calls(uis_token, date_start, date_stop):
    headers = {
        'Content-Type': 'application/json'
    }
    params={
        "jsonrpc": "2.0",
        "id": "number",
        "method": "get.calls_report",
        "params": {
            "access_token":uis_token,
			"date_from": date_start,
            "date_till": date_stop
            
        }}
    response = requests.post(
        "https://dataapi.uiscom.ru/v2.0", headers=headers, json=params
    )
    response.raise_for_status()
    return response.json()['result']['data']


def save_call(uis_token, date_start, date_stop):
    calls = get_calls(uis_token, date_start, date_stop)
    # con = sl.connect('uis_calls.db')
    # for call in calls:
    with open('calls.json', 'a', encoding='utf-8') as file:
        json.dump(calls, file)
        file.write('\n')

        # save_record(id, call_records)


def save_record():
    output_directory = 'media/'
    with open('calls.json') as f:
        calls_info = json.load(f)
    for call in calls_info:
        if call['call_records']:
            for call_record in call['call_records']:
            # call_records = call['call_records'][0]
                url = f"https://app.uiscom.ru/system/media/talk/{call['id']}/{call_record}/"
                try:
                    wget.download(url, out=output_directory)
                except Exception as ex:
                    'Нет файла'







def main():
    # con = sl.connect('uis_calls.db')
    dotenv.load_dotenv()
    uis_token = os.getenv('UIS_TOKEN')
    date_start = "2022-12-09 00:00:00"
    date_stop = "2023-02-09 00:00:00"
    # get_calls(uis_token, date_start, date_stop)
    # save_call(uis_token, date_start, date_stop)
    save_record()


if __name__ == "__main__":
    main()