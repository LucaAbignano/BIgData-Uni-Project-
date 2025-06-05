import os
import csv
import json

#https://www.scribbr.com/statistics/simple-linear-regression/


# Get the relative path to the CSV file
csv_path = os.path.join(os.path.dirname(__file__), 'income_data.csv')

# Read the CSV file
data = []
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Convert to JSON
# Convert types: 'income' and 'happiness' to float, 'index' to int
for row in data:
    if 'income' in row:
        row['income'] = float(row['income'])
    if 'happiness' in row:
        row['happiness'] = float(row['happiness'])
    if 'index' in row:
        del row['index']

json_data = json.dumps(data, indent=4)

# Save the JSON data as a Python variable (list of dicts) for copy-paste
with open('income_data_list.py', 'w', encoding='utf-8') as f:
    f.write('income_data_list = ')
    f.write(json.dumps(data, separators=(',', ':')))
print("Saved to income_data_list.py")
