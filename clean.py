import json

with open("196.json", "r") as f:
    data = json.load(f)

seen = set()
unique_items = []

for item in data:
    item_id = item["qid"]
    if item_id not in seen:
        unique_items.append(item)
        seen.add(item_id)

# Save cleaned JSON
with open("cleaned.json", "w") as f:
    json.dump(unique_items, f, indent=4)

print("Duplicates removed. Saved to cleaned.json")