def format_string(string):
    return string.lower().replace(" ", "_").replace("-", "_")


def get_prefix(url_string):
    part = url_string.split("/", 4)
    if "orkg.org" in url_string.split("/", 4)[2]:
        prefix = part[0] + "//" + part[2] + "/"
    elif url_string.split("/", 4)[3] == '21.T11969':
        prefix = part[0] + "//" + part[2] + "/" + part[3] + "/"
    return prefix


def specify_cardinality(cardinality_string):
    card_parts = cardinality_string.split(" - ")
    if len(card_parts) == 1:
        min_max = {
            "min": int(cardinality_string),
            "max": int(cardinality_string)}
    else:
        min_max = {
            "min": int(card_parts[0]),
            "max": None if card_parts[1] == "n" else int(card_parts[1])}
    return min_max


def generate_uid():
    i = 0

    def function():
        nonlocal i
        i += 1
        return i
    return function
