import json

with open("196.json", "r") as f:
    data = json.load(f)

# --- Remove duplicates (keep first) ---
seen = set()
unique_items = []

for item in data:
    item_id = item["qid"]
    if item_id not in seen:
        unique_items.append(item)
        seen.add(item_id)

# --- Sort by qid as number ---
sorted_items = sorted(unique_items, key=lambda x: int(x["qid"]))

# --- Total count ---
print("Total items:", len(sorted_items))

# --- Find missing numbers ---
all_ids = [int(item["qid"]) for item in sorted_items]
min_id = min(all_ids)
max_id = max(all_ids)

missing = [i for i in range(min_id, max_id + 1) if i not in all_ids]

print("Missing sequence numbers:", missing)

# Save result
with open("sorted_cleaned.json", "w") as f:
    json.dump(sorted_items, f, indent=4)
