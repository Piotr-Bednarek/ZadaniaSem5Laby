import json

nb_path = r"C:\Users\janek\Documents\ZadaniaSem5Laby\uso\lab6.ipynb"

try:
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    print("Markdown cells content:")
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            print(f"--- Cell {i} ---")
            print("".join(cell['source']))
            print("----------------")
except Exception as e:
    print(f"Error: {e}")
