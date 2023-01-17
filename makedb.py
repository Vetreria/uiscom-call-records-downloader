import sqlite3 as sl
con = sl.connect('uis_calls.db')

with con:
# calls_log = con.calls_log()

    con.execute('''CREATE TABLE calls_log
              (
              id INT,
				source VARCHAR(255),
				is_lost BOOLEAN,
				direction VARCHAR(255),
				start_time DATETIME,
				finish_time DATETIME,
				call_records TEXT,
				cpn_region_id INT,
				finish_reason TEXT,
				talk_duration INT,
				wait_duration INT,
				total_duration INT,
				cpn_region_name TEXT,
				communication_id INT,
				wav_call_records TEXT,
				communication_type TEXT,
				clean_talk_duration INT,
				total_wait_duration INT,
				contact_phone_number TEXT,
				virtual_phone_number TEXT,
                record TEXT,
                file BLOB
              )''')

con.commit()
con.close()