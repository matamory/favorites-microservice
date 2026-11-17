import requests

BASE_URL = "http://localhost:5002"


# Helper functions
def send_post(data):
    response = requests.post(BASE_URL + "/favorites", json=data)

    print(f"\nREQUEST:\n     POST /favorites\n     {data}\n")
    print(f"RESPONSE:\n     Status Code: {response.status_code}\n     {response.json()}\n")

    return response


def send_get(params):
    response = requests.get(BASE_URL + "/favorites", params=params)

    print(f"\nREQUEST:\n     GET /favorites\n     {params}\n")
    print(f"RESPONSE:\n     Status Code: {response.status_code}\n     {response.json()}\n")

    return response


def send_delete(item_id, params):
    response = requests.delete(
        f"{BASE_URL}/favorites/{item_id}",
        params=params
    )

    print(f"\nREQUEST:\n     DELETE /favorites/{item_id}\n     {params}\n")
    print(f"RESPONSE:\n     Status Code: {response.status_code}\n     {response.json()}\n")

    return response

# ========================== USER STORY 1 ==========================
# Save a Favorite

print("================= USER STORY 1: Save a Favorite =================\n")


print("-----------------------------------------------------------")

print(
    "Functional Requirement 1 - Successfully save a favorite:\n\n"
    "Given an item that is not currently saved as a favorite,\n"
    "when the user saves the item, the microservice should save its item_id.\n"
)

print("Expected: 201")

send_post({
    "app_id": "fitness_tracker",
    "username": "testuser",
    "item_id": "workout_001"
})


print("-----------------------------------------------------------")

print(
    "Functional Requirement 2 - Save an existing favorite:\n\n"
    "Given an item that has already been saved as a favorite,\n"
    "when the same item is saved again, the microservice should prevent a duplicate.\n"
)

print("Expected: 409")

send_post({
    "app_id": "fitness_tracker",
    "username": "testuser",
    "item_id": "workout_001"
})


# ========================== USER STORY 2 ==========================
# View Favorites

print("================= USER STORY 2: View Favorites =================\n")


print("-----------------------------------------------------------")

print(
    "Functional Requirement 1 - Retrieve saved favorites:\n\n"
    "Given a user has saved favorites,\n"
    "when the user requests their favorites list,\n"
    "the microservice should return the saved item IDs.\n"
)

print("Expected: 200")

send_get({
    "app_id": "fitness_tracker",
    "username": "testuser"
})


print("-----------------------------------------------------------")

print(
    "Functional Requirement 2 - No saved favorites:\n\n"
    "Given a user has no saved favorites,\n"
    "when the user requests their favorites list,\n"
    "the microservice should return an empty list.\n"
)

print("Expected: 200")

send_get({
    "app_id": "fitness_tracker",
    "username": "emptyuser"
})


# ========================== USER STORY 3 ==========================
# Remove a Favorite

print("================= USER STORY 3: Remove a Favorite =================\n")


print("-----------------------------------------------------------")

print(
    "Setup - Add two more favorites so the user has three saved items.\n"
)

send_post({
    "app_id": "fitness_tracker",
    "username": "testuser",
    "item_id": "workout_002"
})

send_post({
    "app_id": "fitness_tracker",
    "username": "testuser",
    "item_id": "workout_003"
})


print("-----------------------------------------------------------")

print(
    "Functional Requirement 1 - Successfully remove a favorite:\n\n"
    "Given a user has three saved favorites,\n"
    "when one favorite is removed,\n"
    "the microservice should remove that item and leave the other favorites unchanged.\n"
)

print("Expected DELETE: 200")

send_delete(
    "workout_001",
    {
        "app_id": "fitness_tracker",
        "username": "testuser"
    }
)

print("Expected GET after delete: 200")

send_get({
    "app_id": "fitness_tracker",
    "username": "testuser"
})


print("-----------------------------------------------------------")

print(
    "Functional Requirement 2 - Remove an item that is not saved:\n\n"
    "Given an item is not currently saved as a favorite,\n"
    "when the user attempts to remove it,\n"
    "the microservice should return a not-found result and leave the favorites unchanged.\n"
)

print("Expected: 404")

send_delete(
    "workout_999",
    {
        "app_id": "fitness_tracker",
        "username": "testuser"
    }
)

print("Expected GET after failed delete: 200")

send_get({
    "app_id": "fitness_tracker",
    "username": "testuser"
})