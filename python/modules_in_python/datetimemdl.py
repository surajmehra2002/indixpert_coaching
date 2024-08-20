
# in this code JSON_file is list in which multiple dict are created so write a program to check all data in list in specific date

import json
from datetime import datetime

JSON_file = r"S:\indixpert_coaching\python\data_storing_files/date_data.json"

with open(JSON_file) as file:
            items = json.load(file)
            date = datetime.now().strftime("%Y-%m-%d")
            list_of_filter_item = []
            # date = "2024-08-16"
            for item in items:
                if item["created_time"].startswith(date):
                    list_of_filter_item.append(item)

            for item in list_of_filter_item:
                print(item)


