import requests
import dotenv
from datetime import datetime, timedelta
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
            "date_till": date_stop,
			"offset":0,
			"limit":10000
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
    with open(f'data/calls1.json', 'a', encoding='utf-8') as file:
        json.dump(calls, file)
        file.write('\n')

        # save_record(id, call_records)


def save_record():
    output_directory = 'media/'
    with open('data/calls1.json') as f:
        calls_info = json.load(f)
    for call in calls_info:
        if call['call_records']:
            for call_record in call['call_records']:
            # call_records = call['call_records'][0]
                url = f"https://app.uiscom.ru/system/media/talk/{call['id']}/{call_record}/"
                try:
                    filename = wget.download(url, out=output_directory)
                    print(filename)
                except Exception as ex:
                    'Нет файла'


def collect_old_records():
    date_start = datetime.fromisoformat("2015-01-01 00:00:00")
    now = datetime.today()
    # date_stop = now
    # for n in range(int ((now - date_stop).days)):
    #     print(date_start.strftime("%Y-%m-%d"), date_stop.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d"))
    #     date_start = date_start + timedelta(n)
    #     print(date_start.strftime("%Y-%m-%d"), date_stop.strftime("%Y-%m-%d"), now.strftime("%Y-%m-%d"))
    date_stop = date_start + timedelta(days=60)
    delta = timedelta(days=60)
    while date_stop <= now:
        print (date_start.strftime("%Y-%m-%d"))
        print (date_stop.strftime("%Y-%m-%d"))
        date_stop += delta
        date_start += delta
    # print()







def main():
    # con = sl.connect('uis_calls.db')
    dotenv.load_dotenv()
    uis_token = os.getenv('UIS_TOKEN')
    date_start = "2023-01-26 00:00:00"
    date_stop = "2023-01-29 00:00:00"
    # get_calls(uis_token, date_start, date_stop)
    # save_call(uis_token, date_start, date_stop)
    save_record()
    # collect_old_records()


if __name__ == "__main__":
    main()