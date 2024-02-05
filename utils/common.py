from typing import TypedDict
import requests


async def is_valid_token(token):
    """
    :description: Checks if the token is valid from jamshid main api
    :param token: pure token
    :return: True if the token is valid, False otherwise
    """
    headers = {'Authorization': f'Bearer {token}'}
    api_endpoint = 'https://api.mafia.jamshid.app/auth/check-token'
    response = requests.post(api_endpoint, headers=headers)
    response_json = response.json()
    print(response_json["status"])
    if response_json["status"] == 200 or response_json["status"] == 201:
        return True
    elif response_json["status"] == 500:
        return False


class RedisConnectioKeys(TypedDict):
    host: str
    port: str
    password: str
