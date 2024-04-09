import requests
def request_epic(template_doi):
    """Request the ePIC REST API
    """
    r = requests.get(template_doi + "?locatt=view:json")
    return r.json()
