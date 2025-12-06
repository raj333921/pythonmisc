import json
import os
from collections import defaultdict

SPLIT_KEY = "qw"   # <-- put the field name you want to split by

with open("196.json", "r") as f:
    data = json.load(f)

groups = defaultdict(list)

# group items by SPLIT_KEY value
for item in data:
    value = str(item.get(SPLIT_KEY, "unknown"))
    groups[value].append(item)

# create output folder
os.makedirs("split_output", exist_ok=True)

# write each group to its own JSON file
for value, items in groups.items():
    filename = f"split_output/{value}.json"
    with open(filename, "w") as f:
        json.dump(items, f, indent=4)
    print(f"Saved {len(items)} items to {filename}")
