import requests

base_url = "http:/127.0.0.1/:8080"  # Update with your server's host and port

def send_add_request(first, second):
    url = f"{base_url}/calculator/add"
    data = {
        "first": first,
        "second": second
    }
    response = requests.post(url, json=data)
    return response.json()

def send_subtract_request(first, second):
    url = f"{base_url}/calculator/subtract"
    data = {
        "first": first,
        "second": second
    }
    response = requests.post(url, json=data)
    return response.json()

if __name__ == "__main__":
    first_number = 10
    second_number = 5

    # Send an add request
    add_response = send_add_request(first_number, second_number)
    print("Addition Result:", add_response["result"])

    # Send a subtract request
    subtract_response = send_subtract_request(first_number, second_number)
    print("Subtraction Result:", subtract_response["result"])
