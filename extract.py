import requests

def extract_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd"
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data
