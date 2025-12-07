import json
from googletrans import Translator

INPUT_FILE = "194easy.json"
OUTPUT_FILE = "outputeasy.json"

translator = Translator()

# These fields should be translated *if they exist*
fields_to_translate = ["q", "optiona", "optionb", "optionc", "e"]

# Load input JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

output = []

for item in data:
    new_item = item.copy()

    for field in fields_to_translate:
        if field not in item:   # <--- skip missing fields
            continue

        text = item[field]

        fr = translator.translate(text, dest="fr").text
        nl = translator.translate(text, dest="nl").text

        new_item[f"{field}_fr"] = fr
        new_item[f"{field}_nl"] = nl

    output.append(new_item)

# Save output JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print("✔ Translation complete! Saved to", OUTPUT_FILE)
