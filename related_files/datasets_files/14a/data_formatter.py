import json
import os
import csv
from pwn import random

working_directory = os.path.dirname(__file__)
in_file = os.path.join(working_directory, 'TA_restaurants_curated.csv')
out_file = os.path.join(working_directory, 'TA_restaurants_curated.py')

def read_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data

def format_entry(entry, header, keep_cities=None, remove_fields=None):
    row = dict(zip(header, entry))
    if keep_cities is not None and row.get('City') not in keep_cities:
        return None
    if row.get('index'):
        row['index'] = int(row['index'])
    if row.get('Ranking'):
        row['Ranking'] = int(float(row['Ranking']))
    if row.get('Rating'):
        row['Rating'] = float(row['Rating'])
    else:
        row['Rating'] = -1
    if row.get('Number of Reviews'):
        row['Number of Reviews'] = int(float(row['Number of Reviews']))
    else:
        row['Number of Reviews'] = -1
    if row.get('Price Range'):
        price = row['Price Range']
        if '$' in price:  # low price
            row['Price Range'] = 1
        elif '$$ - $$$' in price:  # medium price
            row['Price Range'] = 2
        elif '$$$$' in price:  # high price
            row['Price Range'] = 3
        else:  # no price range
            row['Price Range'] = -1
    else:
        row['Price Range'] = -1
    if remove_fields:
        for field in remove_fields:
            if isinstance(field, list):
                for f in field:
                    row.pop(f, None)
            else:
                row.pop(field, None)
    return row

def convert_csv_to_json(csv_data):
    header, *entries= csv_data
    json_data = []
    for entry in entries:
        formatted = format_entry(entry, header, ["Milan"], remove_fields=["Cuisine Style", "index", "Ranking", "Reviews", "URL_TA"])
        if formatted is not None:
            json_data.append(formatted)
    return json_data

def write_output(output_file, json_data):
    with open(os.path.join(os.path.dirname(__file__), output_file), 'w', encoding='utf-8') as out_file:
        out_file.write('restaurants_raw  = ' + json.dumps(json_data, ensure_ascii=False))



def main():
    csv_data = read_csv(in_file)
    json_data = convert_csv_to_json(csv_data)
    json_data = random.sample(json_data, min(200, len(json_data)))
    write_output(out_file, json_data)

if __name__ == '__main__':
    main()