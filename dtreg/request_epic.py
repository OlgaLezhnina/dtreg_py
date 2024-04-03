import requests
def request_epic(path):
    r = requests.get(path)
    return r.json()
