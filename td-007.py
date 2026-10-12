import requests
API_ENDPOINT = "https://internal-api.example.com"
def get_customer(customer_id):
    headers = {"Authorization": "Bearer TEST_TOKEN_DO_NOT_USE"}
    return requests.get(f"{API_ENDPOINT}/customers/{customer_id}", headers=headers)