def format_string(text):
  return text.lower().replace(" ", "_").replace("-", "_")

def get_prefix(string):
    part = string.split("/", 4)
    if "orkg.org" in string.split("/", 4)[2]:
        prefix = part[0] + "//" + part[2] + "/"
    elif string.split("/", 4)[3] == '21.T11969':
        prefix = part[0] + "//" + part[2] + "/" + part[3] + "/"
    return prefix

def range_split(range_str):
    range_parts = range_str.split(" - ")
    if len(range_parts) == 1:
        output = {
            "min": int(range_str),
            "max": int(range_str)}
    else:
        output = {
            "min": int(range_parts[0]),
            "max": None if range_parts[1] == "n" else int(range_parts[1])}
    return output        

def generate_uid():
    i = 0
    def function():
        nonlocal i
        i += 1
        return i
    return function 