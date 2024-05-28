def format_string(text):
  return text.lower().replace(" ", "_").replace("-", "_")

def range_split(range_str):
    range_parts = range_str.split("-")
    if len(range_parts) == 1:
        output = {
            "min": range_str,
            "max": range_str}
    else:
        output = {
            "min": range_parts[0],
            "max": range_parts[1] if range_parts[1] != "n" else str(None)}
    return output        

def generate_uid():
    i = 0
    def function():
        nonlocal i
        i += 1
        return i
    return function 