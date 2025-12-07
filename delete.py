import requests

# 1. API endpoints
GET_URL = "https://sachadigi.com/limanplatform/quiz"  # Endpoint to get the list of items
DELETE_URL = "https://sachadigi.com/limanplatform/admin/question/easy/"  # Endpoint to delete a specific item by ID
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaXNBZG1pbiI6dHJ1ZSwiaWF0IjoxNzY1MTMxNzMzLCJleHAiOjE3NjUxNDYxMzN9._TnFylhFi0JmLlDwF3XBUTKeJ2vBosecLeRVjE-Xzpg"
HEADERS = {"Authorization": f"Bearer {token}"}


# 3. Step 1: Get the list of IDs
response = requests.get(GET_URL, headers=HEADERS)
if response.status_code == 200:
    data = response.json()
    # Assuming the response is a list of items with an 'id' field
    ids_to_delete = [item['id'] for item in data]
else:
    print(f"Failed to get items: {response.status_code} {response.text}")
    ids_to_delete = []

# 4. Step 2: Delete each ID
for item_id in ids_to_delete:
    delete_response = requests.delete(f"{DELETE_URL}{item_id}", headers=HEADERS)
    if delete_response.status_code == 200 or delete_response.status_code == 204:
        print(f"Deleted item {item_id} successfully.")
    else:
        print(f"Failed to delete item {item_id}: {delete_response.status_code} {delete_response.text}")