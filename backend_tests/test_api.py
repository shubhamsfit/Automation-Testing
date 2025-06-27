import requests

def test_api_status_code():
    res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert res.status_code == 500

def test_api_data_content():
    res = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert res.json()["id"] == 2
