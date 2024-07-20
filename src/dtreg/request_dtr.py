import requests


def request_dtr(route):
    """Request a dtr API
    """
    r = requests.get(route)
    return r.json()
