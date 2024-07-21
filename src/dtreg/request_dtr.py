import requests


def request_dtr(route):
    """
    Request an API of a datatype registry
    :param route: the path for requesting a dtr API
    :return: requested information about a datatype schema
    """
    r = requests.get(route)
    return r.json()
