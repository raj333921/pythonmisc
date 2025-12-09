import json

# --- Input & Output files ---
input_file = "194easy.json"
output_file = "updated_data.json"

# --- Keys/Values you want to add to each object ---
# Add as many as you want here:
extra_fields = {
    "optiona": "",
    "optionb": "",
    "optionc": ""
}

# --- Read JSON file ---
with open(input_file, "r") as f:
    data = json.load(f)

# --- Add fields to each JSON object ---
for item in data:
    for key, value in extra_fields.items():
        item[key] = value

# --- Save updated file ---
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)

print("Done! Updated file saved as:", output_file)
