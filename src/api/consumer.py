import requests

from utils.constants import BASE_URL_API_CONSUMER


def consume_api_by_id(id):
    return requests.get(f"{BASE_URL_API_CONSUMER}/{id}")
