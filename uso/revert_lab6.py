import json

nb_path = r"C:\Users\janek\Documents\ZadaniaSem5Laby\uso\lab6.ipynb"

try:
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Remove the last cell if it is the LQR one we added
    if nb['cells'] and nb['cells'][-1].get('id') == "lqr_comparison":
        nb['cells'].pop()
        print("Removed LQR comparison cell from lab6.ipynb")
    else:
        print("LQR cell not found at the end of lab6.ipynb, checking logic...")
        # Check by source content if ID missing
        if "solve_continuous_are" in "".join(nb['cells'][-1]['source']):
             nb['cells'].pop()
             print("Removed last cell based on content.")

    with open(nb_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

except Exception as e:
    print(f"Error: {e}")
