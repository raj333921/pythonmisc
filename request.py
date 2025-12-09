import json
import os
import requests

# ---------------------------------------------
# 1. Convert old JSON structure to new one
# ---------------------------------------------
def convert_item(old):
    letter_to_index = {"a": 0, "b": 1, "c": 2, "d": 3}

    # Build options dynamically
    options = []

    # Option A
    options.append({
        "en": old.get("optiona", ""),
        "fr": old.get("optiona_fr", ""),
        "nl": old.get("optiona_nl", "")
    })

    # Option B
    options.append({
        "en": old.get("optionb", ""),
        "fr": old.get("optionb_fr", ""),
        "nl": old.get("optionb_nl", "")
    })

    # Option C (optional)
    if old.get("optionc"):
        options.append({
            "en": old.get("optionc", ""),
            "fr": old.get("optionc_fr", ""),
            "nl": old.get("optionc_nl", "")
        })

    # Option D (optional, if exists)
    if old.get("optiond"):
        options.append({
            "en": old.get("optiond", ""),
            "fr": old.get("optiond_fr", ""),
            "nl": old.get("optiond_nl", "")
        })

    # Correct answer index
    answer_letter = old.get("s", "a").lower()
    correct_option = letter_to_index.get(answer_letter, 0)

    if correct_option >= len(options):
        raise ValueError(f"Correct answer '{answer_letter}' does not exist in options")

    return {
        "level": "easy",
        "question": [{
            "en": old.get("q", ""),
            "fr": old.get("q_fr", ""),
            "nl": old.get("q_nl", "")
        }],
        "options": options,
        "correct_option": correct_option,
        "explanation": [
            {
                "en": old.get("e", ""),
                "fr": old.get("e_fr", ""),
                "nl": old.get("e_nl", "")
            }
        ]
    }

# ---------------------------------------------
# 2. Load old items
# ---------------------------------------------
INPUT_FILE = "outputeasy.json"
IMAGE_FOLDER = "193"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    old_items = json.load(f)

print(f"Loaded {len(old_items)} questions.")

# ---------------------------------------------
# 3. Upload JSON + PNG together
# ---------------------------------------------
API_URL = "https://sachadigi.com/limanplatform/admin/question"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaXNBZG1pbiI6dHJ1ZSwiaWF0IjoxNzY1MzAzMDk4LCJleHAiOjE3NjUzMTc0OTh9.Pvx0A1_93NGdXj34VImpUYlxp2Zj-A7zsWtByq-1258"

for item in old_items:
    qid = item.get("qid")
    image_path = os.path.join(IMAGE_FOLDER, f"{qid}.jpg")

    # Convert JSON
    try:
        new_item = convert_item(item)
    except Exception as e:
        print(f"❌ Error converting qid {qid}: {e}")
        continue

    # Prepare multipart/form-data
    files = {
        "level": (None, new_item["level"]),
        "question": (None, json.dumps(new_item["question"], ensure_ascii=False)),
        "options": (None, json.dumps(new_item["options"], ensure_ascii=False)),
        "explanation": (None, json.dumps(new_item["explanation"], ensure_ascii=False)),
        "correct_option": (None, str(new_item["correct_option"]))
    }

    # Add image if exists
    if os.path.exists(image_path):
        files["image"] = (os.path.basename(image_path), open(image_path, "rb"), "image/jpeg")
        print(f"📷 Attaching image for qid {qid}")
    else:
        print(f"⚠️ No image found for qid {qid}, sending JSON only")

    headers = {"Authorization": f"Bearer {token}"}

    # Send request
    response = requests.post(API_URL, files=files, headers=headers)

    print(f"qid {qid} → Status {response.status_code}")
    print("Response:", response.text)
