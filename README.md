# Favorites Microservice

## Description
The Favorites Microservice allows users to save items as favorites or bookmarks and retrieve or remove them later.

It uses a REST API and runs on port 5002.

The service uses:

- app_id to identify the application
- username to identify the user
- item_id to identify the item being saved or removed

The microservice supports:

- POST /favorites to save a favorite
- GET /favorites to retrieve a user's favorites
- DELETE /favorites/<item_id> to remove a favorite

## How to Request Data from the microservice

Other programs can request data from the Favorites Microservice by sending HTTP requests to:

http://localhost:5002/favorites

The required parameters are:

- app_id: identifies the application requesting the operation
- username: identifies the user whose favorites are being managed
- item_id: identifies the item being saved or removed. This is required for POST and DELETE, but not for GET

## Example call for requesting data
```python
import requests

url = "http://localhost:5002/favorites"

user = {
    "app_id": "fitness_tracker",
    "username": "testuser"
}
```


### Save a favorite
```python
save_response = requests.post(url, json={
    **user,
    "item_id": "workout_001"
})
```


### Retrieve favorites
```python
view_response = requests.get(url, params=user)
```

### Remove a favorite
```python
remove_response = requests.delete(
    f"{url}/workout_001",
    params=user
)
```

##  How to receive data from the microservice

The Favorites Microservice returns data in JSON format.

When an item is successfully saved or removed, the service returns a success result.

When a user's favorites are requested, the service returns a list of saved item IDs.

If the user has no saved favorites, the service returns an empty list.

If an application attempts to remove an item that is not saved, the service returns an error indicating that the item was not found.

## Example call for receiving data

### Check whether the favorite was saved
```python
print(save_response.json()["success"])
```

Output:

```text
True
```


### Display the user's saved favorites
```python
print(view_response.json()["favorites"])
```

Output:

```text
['workout_001']
```

### Check whether the favorite was removed
```python
print(remove_response.json()["success"])
```

Output:

```text
True
```

## UML sequence diagram that communicates how to request and receive data from the microservice


![UML Sequence diagram favorites.png](UML%20Sequence%20diagram%20favorites.png)