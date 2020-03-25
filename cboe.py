import json
import base64
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client_id = "cwcaizu@gmail.com_api_client_1584849514"
client_secret = "2180ebf4196d466eaa53b698ba66e2d9"

identity_url = "https://sandbox.livevol.com/id/connect/token"

encoded = base64.b64encode((client_id + ':' + client_secret).encode())
headers = {"Authorization": "Basic " + encoded.decode('ascii')}
payload = {"grant_type": "client_credentials"}

URL = "https://sandbox.livevol.com/api/v1/delayed/market/symbols/SPX/all-options-trades?date=2020-03-18&min_time=09:30:00.001&max_time=15:39:58.123&root=SPX&expiry=2020-03-25&strike=2750&option_type=C&exchange_id=5&min_size=5&max_size=1000&min_price=0.25&max_price=5&condition_id=0&order_by_time=ASC&start_sequence_number=0&limit=10"

# Requesting access token
token_data = requests.post(identity_url, data=payload, headers=headers)

if token_data.status_code == 200:
    token = token_data.json()['access_token']
    if len(token) > 0:
        print("Authenticated successfully")
        # Requesting data from API
        # result = requests.get("https://sandbox.livevol.com/api//v1/delayed/market/symbols/AAPL", headers={"Authorization": "Bearer " + token}, verify=False)
        # print(result.json())

        result = requests.get(URL, headers={"Authorization": "Bearer " + token}, verify=False)
        print(result.json())
else:
    print("Authentications failed")