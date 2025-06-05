import pandas as pd
import os

file_path = os.path.join(os.path.dirname(__file__), 'seeds_dataset.txt')
data = pd.read_csv(file_path, delim_whitespace=True, header=None, names=[
    'area', 'perimeter', 'compactness', 'length_of_kernel', 'width_of_kernel',
    'asymmetry_coefficient', 'length_of_kernel_groove', 'type_of_seed'
])
data['type_of_seed'] = pd.to_numeric(data['type_of_seed'], errors='coerce').astype('Int64')
output_path = os.path.join(os.path.dirname(__file__), 'seeds_dataset_list.py')
with open(output_path, 'w') as f:
    f.write(f"data = {data.values.tolist()}\n")

