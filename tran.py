import json
from deep_translator import GoogleTranslator, exceptions

INPUT_FILE = "194easy.json"
OUTPUT_FILE = "outputeasy.json"

# These fields should be translated *if they exist*
fields_to_translate = ["q", "optiona", "optionb", "optionc", "e"]

def safe_translate(text, target_lang):
    """Translate safely and return original text if translation fails."""
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"[WARN] Failed to translate '{text}' -> '{target_lang}': {e}")
        return text   # fallback: return original text

# Load input JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

output = []

for item in data:
    new_item = item.copy()

    for field in fields_to_translate:
        if field not in item:
            continue  # Skip missing fields

        text = item[field]

        # Translate to French and Dutch
        fr = safe_translate(text, "fr")
        nl = safe_translate(text, "nl")

        new_item[f"{field}_fr"] = fr
        new_item[f"{field}_nl"] = nl

    output.append(new_item)

# Save output JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print("✔ Translation complete! Saved to", OUTPUT_FILE)
