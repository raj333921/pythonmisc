import json

# --- Input & Output files ---
input_file = "194easy.json"
output_file = "updated_data.json"

# --- Starting ID number ---
start_id = 176

# --- Read JSON file ---
with open(input_file, "r") as f:
    data = json.load(f)   # this should be a list of objects

# --- Update IDs sequentially ---
current_id = start_id
for item in data:
    item["id"] = current_id
    current_id += 1

# --- Save updated file ---
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print("IDs updated! File saved as:", output_file)