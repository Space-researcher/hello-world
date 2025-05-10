
import pytest
import requests
'''
Simple API test - post, get, delete.
'''


ENDPOINT = "https://api.restful-api.dev"  

payload = {
   "name": "HP ZenBook",
   "data": {
      "year": 2020,
      "price": 20000,
      "CPU model": "Ryzen",
      "Hard disk size": "1 TB"
   }
}

def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200, "Not expected response code during endpoint call"

@pytest.fixture(scope="module")
def created_task_id():
    # Setup: create the item
    create_task_response = requests.post(ENDPOINT + "/objects", json=payload)
    assert create_task_response.status_code == 200, "Not expected response code during creation"
    data = create_task_response.json()
    print()   
    print("Create new record:", data) 
    task_id = data["id"]
    yield task_id
    # Teardown: Delete the item
    delete_response = requests.delete(f"{ENDPOINT}/objects/{task_id}")
    assert delete_response.status_code == 200, "Not expected response code after deletion"
    message = delete_response.json()
    expected_message = f"Object with id = {task_id} has been deleted."
    assert message.get("message") == expected_message, "Not expected message after deletion"

def test_can_get_item(created_task_id):
    get_task_response = requests.get(f"{ENDPOINT}/objects/{created_task_id}")
    assert get_task_response.status_code == 200, "Run get - not expected response code" 
    get_task_data = get_task_response.json()

    assert get_task_data["name"] == payload["name"], "Run get - not expected name" 
    assert get_task_data["data"]["CPU model"] == payload["data"]["CPU model"], "Run get - not expected CPU model" 
    
    