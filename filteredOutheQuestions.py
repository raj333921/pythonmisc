import json
import re

# --- File paths ---
input_file = "194easy.json"
filtered_file = "filtered_data.json"

# --- Read JSON file ---
with open(input_file, "r") as f:
    data = json.load(f)

filtered_questions = []
remaining_questions = []

# --- Regex pattern for options ---
option_pattern = re.compile(r"(A|B|C|D)\.\s*(.*?)\s*(<br\s*/?>|$)", re.IGNORECASE)

for item in data:
    q_text = item.get("q", "")

    # Find all options
    matches = option_pattern.findall(q_text)
    options = {"optiona": "", "optionb": "", "optionc": "", "optiond": ""}
    for opt_letter, opt_text, _ in matches:
        options[f"option{opt_letter.lower()}"] = opt_text.strip()

    # Check if A, B, C exist
    if options["optiona"] and options["optionb"] and options["optionc"]:
        # Remove all option texts from the question
        q_clean = option_pattern.sub("", q_text).strip()
        item["q"] = q_clean
        item.update(options)
        filtered_questions.append(item)
    else:
        remaining_questions.append(item)

# --- Save filtered questions ---
with open(filtered_file, "w") as f:
    json.dump(filtered_questions, f, indent=4)

# --- Save remaining questions back to original file ---
with open(input_file, "w") as f:
    json.dump(remaining_questions, f, indent=4)

print(f"Filtered {len(filtered_questions)} questions to {filtered_file}.")
print(f"Remaining {len(remaining_questions)} questions saved to {input_file}.")
